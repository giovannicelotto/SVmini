#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Common/interface/ValueMap.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "TrackingTools/IPTools/interface/IPTools.h"
#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"
#include "TLorentzVector.h"
#include "TrackingTools/PatternTools/interface/TwoTrackMinimumDistance.h"
#include "TrackingTools/GeomPropagators/interface/AnalyticalImpactPointExtrapolator.h"
#include "PhysicsTools/ONNXRuntime/interface/ONNXRuntime.h"
class ONNXRuntime;

class DummyTrackValueMap : public edm::stream::EDProducer<> {
public:
  explicit DummyTrackValueMap(const edm::ParameterSet&, const ONNXRuntime*);
    void produce(
                edm::Event &iEvent,
                const edm::EventSetup &iSetup) override;

private:
  edm::EDGetTokenT<reco::TrackCollection> tracksToken_;
  edm::EDGetTokenT<std::vector<reco::Vertex>> pvsToken_;
  edm::ESGetToken<TransientTrackBuilder, TransientTrackRecord> theTTBToken;
};

DummyTrackValueMap::DummyTrackValueMap(const edm::ParameterSet& iConfig, const ONNXRuntime *cache):
  tracksToken_(consumes<reco::TrackCollection>(iConfig.getParameter<edm::InputTag>("src"))),
  pvsToken_(consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("pvSrc"))),
  theTTBToken(esConsumes<TransientTrackBuilder, TransientTrackRecord>(edm::ESInputTag("", "TransientTrackBuilder")))
{
    produces<edm::ValueMap<float>>("SVscore");
    produces<edm::ValueMap<float>>("SVscore_B");
    produces<edm::ValueMap<float>>("SVscore_C");
    produces<edm::ValueMap<float>>("SVscore_CfromB");
}
std::unique_ptr<ONNXRuntime> DemoAnalyzer::initializeGlobalCache(const edm::ParameterSet &iConfig) 
{
    return std::make_unique<ONNXRuntime>(iConfig.getParameter<edm::FileInPath>("model_path").fullPath());
}

void DemoAnalyzer::globalEndJob(const ONNXRuntime *cache) {}

void DummyTrackValueMap::produce(edm::Event& iEvent,const edm::EventSetup &iSetup)
{

    edm::Handle<reco::TrackCollection> tracks;
    iEvent.getByToken(tracksToken_, tracks);
    edm::Handle<std::vector<reco::Vertex>> pvs;
    iEvent.getByToken(pvsToken_, pvs);


    const auto& PV0 = pvs->front();
    const auto& ttBuilder = iSetup.getData(theTTBToken);
    

    // retrieve information of tracks
    std::vector<float> trk_pt, trk_eta, trk_phi, trk_weight;
    std::vector<float> trk_ip_z, trk_ip_z_sig, trk_ip2d, trk_ip3d, trk_ip2d_sig, trk_ip3d_sig, trk_p, trk_charge, trk_numberOfValidHits, trk_numberOfValidPixelHits, trk_numberOfValidStripHits;

    // dummy feature = 1 for each track
    std::vector<float> track_SVscore;
    std::vector<float> track_SVscore_B;
    std::vector<float> track_SVscore_C;
    std::vector<float> track_SVscore_CfromB;

    std::vector<float> edge_score;
    
    track_SVscore.reserve(tracks->size());
    track_SVscore_B.reserve(tracks->size());
    track_SVscore_C.reserve(tracks->size());
    track_SVscore_CfromB.reserve(tracks->size());

    edge_score.reserve(tracks->size() * tracks->size() / 2);

    for (const auto& trk : *tracks) {
            trk_pt.push_back(trk.pt());
            //trk_weight.push_back(w);
            trk_eta.push_back(trk.eta());
            trk_phi.push_back(trk.phi());
            trk_p.push_back(trk.p());
            trk_charge.push_back(trk.charge());
            trk_numberOfValidHits.push_back(trk.numberOfValidHits());
            trk_numberOfValidPixelHits.push_back(trk.hitPattern().numberOfValidPixelHits());
            trk_numberOfValidStripHits.push_back(trk.hitPattern().numberOfValidStripHits());
            double ip_z = trk.dz(PV0.position());
            double ip_z_sig = ip_z / trk.dzError();
            trk_ip_z.push_back(ip_z);
            trk_ip_z_sig.push_back(ip_z_sig);

            GlobalVector direction(1,0,0);
            direction = direction.unit();
            const auto& ttBuilder = iSetup.getData(theTTBToken);
            reco::TransientTrack ttrk = ttBuilder.build(trk);
            auto ip2d_val = IPTools::signedTransverseImpactParameter(ttrk, direction, PV0).second;
            auto ip3d_val = IPTools::signedImpactParameter3D(ttrk, direction, PV0).second;

            trk_ip2d.push_back(ip2d_val.value());
            trk_ip3d.push_back(ip3d_val.value());
            trk_ip2d_sig.push_back(ip2d_val.significance());
            trk_ip3d_sig.push_back(ip3d_val.significance());
    }







        // retrieve information of tracks
    std::vector<int> trk_idxs, trk_jdxs;
    std::vector<float> deltaR, dca, dca_sig, cptopv, pvtoPCA_j, pvtoPCA_i, dotprod_j, dotprod_i, pair_mom, pair_invmass, dotprodTrack, dotprodSeed;

    const float PION_MASS = 0.13957018;
    int idx = 0;
    int jdx = 0;
    for (const auto& trk_i : *tracks) {
        reco::TransientTrack ttrk_i = ttBuilder.build(trk_i);
        if (!ttrk_i.isValid()) continue;
            
        for (const auto& trk_j : *tracks) {
            reco::TransientTrack ttrk_j = ttBuilder.build(trk_j);
            if (!ttrk_j.isValid()) continue;
            
            // Definition of TLorentzVectors
            TLorentzVector p4_i;
            TLorentzVector p4_j;
            p4_i.SetPtEtaPhiM(trk_i.pt(), trk_i.eta(), trk_i.phi(), PION_MASS);
            p4_j.SetPtEtaPhiM(trk_j.pt(), trk_j.eta(), trk_j.phi(), PION_MASS);
            TLorentzVector pair = p4_i + p4_j;

            // cut
            float inv_mass = pair.M();
            if (inv_mass>20.0) continue;
            float delta_r_val = (p4_i.DeltaR(p4_j));
            if (delta_r_val > 1.0); continue;


            float dca_val = -1.0;  // Default invalid value
	        float cptopv_val = -1.0;
            float pvToPCAseed_val = -1.0;
            float pvToPCAtrack_val = -1.0;
            float dotprodTrack_val = -999.0;
            float dotprodSeed_val = -999.0;
            float dcaSig_val = -1.0;
            float pairMomentumMag = -1.0;
            // filling vectors

            TwoTrackMinimumDistance minDist;
            
            if (minDist.calculate(ttrk_i.impactPointState(), ttrk_j.impactPointState())) {
            	VertexDistance3D distanceComputer;
            	auto m = distanceComputer.distance(
            	VertexState(minDist.points().second, ttrk_i.impactPointState().cartesianError().position()),
            	VertexState(minDist.points().first, ttrk_j.impactPointState().cartesianError().position()));
            	dca_val = m.value();

	    	if(m.error() > 0){
	    	    dcaSig_val = m.value() / m.error();
	    	}

            GlobalPoint cp(minDist.crossingPoint());
            GlobalPoint pvp(PV0.position().x(), PV0.position().y(), PV0.position().z());
   	    	 
	    	GlobalPoint seedPCA = minDist.points().second;  // PCA of track i (seed)
	    	GlobalPoint trackPCA = minDist.points().first;  // PCA of track j
   	    	
	    	pvToPCAseed_val = (seedPCA - pvp).mag();      // Distance PV to seed track's PCA
	    	pvToPCAtrack_val = (trackPCA - pvp).mag();    // Distance PV to other track's PCA
            	
            	// Calculate additional variables
            cptopv_val = (cp - pvp).mag();
            dotprodTrack_val = (trackPCA - pvp).unit().dot(ttrk_j.impactPointState().globalDirection().unit());
            dotprodSeed_val = (seedPCA - pvp).unit().dot(ttrk_i.impactPointState().globalDirection().unit());
            	
            	// Pair momentum
            GlobalVector pairMomentum((Basic3DVector<float>)(ttrk_i.track().momentum() + ttrk_j.track().momentum()));
            pairMomentumMag = pairMomentum.mag();
            }

            if (dca_val > 1 or dcaSig_val > 100 or cptopv_val > 20 or pvToPCAseed_val > 20 or pvToPCAtrack_val > 20) continue;	
            if (pairMomentumMag < 0.05 or pairMomentumMag > 100) continue;
    
            #pragma omp critical{
            trk_idxs.push_back(idx);
            trk_jdxs.push_back(jdx);
            deltaR.push_back(delta_r_val);
            dca.push_back(dca_val);
            dca_sig.push_back(dcaSig_val);
            cptopv.push_back(cptopv_val);
            pvtoPCA_j.push_back(pvToPCAtrack_val);
            pvtoPCA_i.push_back(pvToPCAseed_val);
            dotprod_j.push_back(dotprodTrack_val);
            dotprod_i.push_back(dotprodSeed_val);
            pair_mom.push_back(pairMomentumMag);
            pair_invmass.push_back(inv_mass);
            }
        }
    }







































    std::vector<std::vector<float>> track_features;
   	std::vector<std::vector<float>> edge_features;
   	std::vector<int64_t> edge_i, edge_j;
	
	   // Step 1: Build track_features, and track bad ones
   	for (size_t i = 0; i < static_cast<size_t>(ntrk); ++i) {
   	    std::vector<float> features = {
   	        trk_eta[i],
   	        trk_phi[i],
   	        trk_ip2d[i],
   	        trk_ip3d[i],
   	        trk_ipz[i],
   	        trk_ipzsig[i],
   	        trk_ip2dsig[i],
   	        trk_ip3dsig[i],
   	        trk_p[i],
   	        trk_pt[i],
   	        static_cast<float>(trk_nValid[i]),
   	        static_cast<float>(trk_nValidPixel[i]),
   	        static_cast<float>(trk_nValidStrip[i]),
   	        static_cast<float>(trk_charge[i])
   	    };
   	
   	    bool has_nan = false;
   	    for (float val : features) {
   	        if (!std::isfinite(val)) {
   	            has_nan = true;
   	            break;
   	        }
   	    }
   	
   	    if (has_nan) {
   	        features = {
   	         -999.0f, -999.0f, -999.0f, -999.0f, -999.0f, -999.0f, -999.0f, -999.0f, -999.0f, -999.0f,  // 10 dummy float features
   	         -1.0f, -1.0f, -1.0f,  // 3 dummy int features as float
   	         -3.0f          // charge dummy
   	        };
   	    }
   	
   	    track_features.push_back(features);
   	}

   	 
   	
   	for (size_t idx = 0; idx < trk_i.size(); ++idx) {
   	    int oi = trk_i[idx];
   	    int oj = trk_j[idx];

	    int ni = origToNode[oi];
	    int nj = origToNode[oj];

   	    edge_i.push_back(ni);
   	    edge_j.push_back(nj);
   	    
   	     edge_features.push_back({
   	     dca[idx],
   	     deltaR[idx],
   	     dca_sig[idx],
   	     cptopv[idx],
   	     pvtoPCA_i[idx],
   	     pvtoPCA_j[idx],
   	     dotprod_i[idx],
   	     dotprod_j[idx],
   	     pair_mom[idx],
   	     pair_invmass[idx]
   	     }); 
   	 }

   	std::vector<float> x_in_flat;
   	x_in_flat.reserve(track_features.size() * 14);
   	for (const auto& feat : track_features)
   	    x_in_flat.insert(x_in_flat.end(), feat.begin(), feat.end());

   	std::vector<float> edge_index_flat_f;
   	edge_index_flat_f.reserve(edge_i.size() * 2);
   	for (size_t k = 0; k < edge_i.size(); ++k) {
   	    edge_index_flat_f.push_back(static_cast<float>(edge_i[k]));
   	}

   	for (size_t k = 0; k < edge_j.size(); ++k) {
   	    edge_index_flat_f.push_back(static_cast<float>(edge_j[k]));
   	}

   	std::vector<float> edge_attr_flat;
   	edge_attr_flat.reserve(edge_features.size() * 10);
   	for (const auto& feat : edge_features)
   	    edge_attr_flat.insert(edge_attr_flat.end(), feat.begin(), feat.end());
   	   
   	// === 4. Set input names and feed data ===
   	std::vector<std::string> input_names_ = {"x_in", "edge_index", "edge_attr"};

   	std::vector<std::vector<int64_t>> input_shapes_ = {
   	 {1, static_cast<int64_t>(track_features.size()), 14},        // x_in
   	 {1, 2, static_cast<int64_t>(edge_i.size())},                // edge_index
   	 {1, static_cast<int64_t>(edge_features.size()), 10}         // edge_attr
   	};
   	   
   	std::vector<std::vector<float>> data_ = {
   	 x_in_flat,
   	 edge_index_flat_f,
   	 edge_attr_flat
   	};


   	std::vector<std::vector<float>> output = globalCache()->run(input_names_, data_, input_shapes_);

   	const std::vector<float>& sv_logits_flat = output[0];
   	const std::vector<float>& sv_sub_logits_flat = output[1];
   	const std::vector<float>& edge_logits_flat  = output[2]; // [E]

















// evaluation of edge features
    for (const auto& trk_i : *tracks) {
        for (const auto& trk_j : *tracks) {
            //
            // code here  now placeholder
            //evaluator(i, j)
            edge_score.push_back(1.0); 
            }
        }

// GNN evaluation placeholder
    for (const auto& trk : *tracks) {
            float feature = 1.0;    // placeholder
            track_SVscore.push_back(feature);
            track_SVscore_B.push_back(feature);
            track_SVscore_C.push_back(feature);
            track_SVscore_CfromB.push_back(feature);
      }

    auto valMap = std::make_unique<edm::ValueMap<float>>();
    edm::ValueMap<float>::Filler filler(*valMap);
    
    auto putMap = [&](const std::vector<float>& values, const std::string& name) {
        auto valMap = std::make_unique<edm::ValueMap<float>>();
        edm::ValueMap<float>::Filler filler(*valMap);
        filler.insert(tracks, values.begin(), values.end());
        filler.fill();
        iEvent.put(std::move(valMap), name);
    };

    putMap(track_SVscore, "SVscore");
    putMap(track_SVscore_B, "SVscore_B");
    putMap(track_SVscore_C, "SVscore_C");
    putMap(track_SVscore_CfromB, "SVscore_CfromB");
}

DEFINE_FWK_MODULE(DummyTrackValueMap);