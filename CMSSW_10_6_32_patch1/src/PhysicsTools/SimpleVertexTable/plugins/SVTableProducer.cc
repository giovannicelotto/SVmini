#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TLorentzVector.h"
#include "TVector3.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/NanoAOD/interface/FlatTable.h"

class SVTableProducer : public edm::global::EDProducer<> {
public:
    explicit SVTableProducer(const edm::ParameterSet &iConfig)
        : svToken(consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("src"))) 
    {
        produces<nanoaod::FlatTable>("SVTable");
        produces<nanoaod::FlatTable>("SVtrksTable");
    }

    void produce(edm::StreamID,
                 edm::Event &iEvent,
                 const edm::EventSetup &) const override 
    {
        edm::Handle<std::vector<reco::Vertex>> svs;
        iEvent.getByToken(svToken, svs);

        //std::cout<<"[DEBUG] SVTableProducer " << "Number of SVs: " << svs->size()<< "\n";
        //for (size_t i = 0; i < svs->size(); ++i) {
        //    const auto &sv = svs->at(i);
        //    //std::cout<<"SVTableProducer\n" 
        //    //    << "SV " << i 
        //    //    << ": x=" << sv.x() 
        //    //    << " y=" << sv.y() 
        //    //    << " z=" << sv.z()
        //    //    << " nTracks=" << sv.tracksSize()<<"\n";
        //}

        auto table = std::make_unique<nanoaod::FlatTable>(static_cast<unsigned int>(svs->size()), "mySV", false);
        unsigned int nSVtracks = 0;
        int nTrksCurrentSV = 0;
        for (auto const& sv : *svs) {
            nTrksCurrentSV = 0;
            for (auto it = sv.tracks_begin(); it != sv.tracks_end(); ++it) {
                const edm::RefToBase<reco::Track>& trkRef = *it;
                if (trkRef.isNull()) continue;
                double w = sv.trackWeight(trkRef);   // <-- weight comes from vertex
                //if (w < 0.5) continue;               // skip low-weight tracks
                nTrksCurrentSV++;
            }
            if (nTrksCurrentSV < 2) continue; // skip SVs with less than 2 high-weight tracks
            nSVtracks += nTrksCurrentSV;
        }
        auto trk_table = std::make_unique<nanoaod::FlatTable>(static_cast<unsigned int>(nSVtracks), "mySVtrks", false);


        std::vector<float> x, y, z, chi2, ndof, pt, eta, phi, mass;
        std::vector<float> trk_pt, trk_eta, trk_phi, trk_weight;
        std::vector<int> nTracks;
        std::vector<int> trk_SVidx;

        int nTrksPerSV = 0;
        //std::cout<<svs->size()<<" SVs to process\n";
        for (const auto &sv : *svs) {
            nTrksPerSV = 0;
            // First count tracks with weight >= 0.5
            for (auto it = sv.tracks_begin(); it != sv.tracks_end(); ++it) {
                const edm::RefToBase<reco::Track>& trkRef = *it;
                if (trkRef.isNull()) continue;
                double w = sv.trackWeight(trkRef);   // <-- weight comes from vertex
                //if (w < 0.5) continue;               // skip low-weight tracks
                nTrksPerSV++;
            }
            if (nTrksPerSV < 2) continue; // skip SVs with less than 2 high-weight tracks

            x.push_back(sv.x());
            y.push_back(sv.y());
            z.push_back(sv.z());
            chi2.push_back(sv.chi2());
            ndof.push_back(sv.ndof());
            nTracks.push_back(nTrksPerSV);
            

            TLorentzVector p4s_SV;
            for (auto it = sv.tracks_begin(); it != sv.tracks_end(); ++it) {
                const edm::RefToBase<reco::Track>& trkRef = *it;
                if (trkRef.isNull()) continue;
                double w = sv.trackWeight(trkRef);
                //if (w < 0.5) continue;



                TLorentzVector p4;
                p4.SetPtEtaPhiM(trkRef->pt(),trkRef->eta(),trkRef->phi(),0.13957039);
                trk_pt.push_back(trkRef->pt());
                trk_weight.push_back(w);
                trk_eta.push_back(trkRef->eta());
                trk_phi.push_back(trkRef->phi());
                trk_SVidx.push_back(x.size()-1); 
                p4s_SV += p4;
            }
            pt.push_back(p4s_SV.Pt());
            eta.push_back(p4s_SV.Eta());
            phi.push_back(p4s_SV.Phi());
            mass.push_back(p4s_SV.M());


            //std::cout<<"SV: x=" << sv.x() 
            //    << " y=" << sv.y() 
            //    << " z=" << sv.z()
            //    << " nTracks=" << sv.tracksSize()
            //    << " pt=" << p4s_SV.Pt();
        }


        table->addColumn<float>("x", x, "X position of SV", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("y", y, "Y position of SV", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("z", z, "Z position of SV", nanoaod::FlatTable::FloatColumn);
        //std::cout<<"[DEBUG] SVTableProducer added x,y,z columns\n";
        table->addColumn<float>("chi2", chi2, "Chi2 of vertex fit", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("ndof", ndof, "Degrees of freedom of vertex fit", nanoaod::FlatTable::FloatColumn);
        table->addColumn<int>("nTracks", nTracks, "Number of tracks in SV", nanoaod::FlatTable::IntColumn);
        table->addColumn<float>("pt", pt, "pt", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("eta", eta, "eta ", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("phi", phi, "phi", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("mass", mass, "mass", nanoaod::FlatTable::FloatColumn);
        trk_table->addColumn<float>("trk_pt", trk_pt, "trk_pt", nanoaod::FlatTable::FloatColumn);
        trk_table->addColumn<float>("trk_weight", trk_weight, "trk_weight", nanoaod::FlatTable::FloatColumn);
        trk_table->addColumn<float>("trk_eta", trk_eta, "trk_eta ", nanoaod::FlatTable::FloatColumn);
        trk_table->addColumn<float>("trk_phi", trk_phi, "trk_phi", nanoaod::FlatTable::FloatColumn);
        trk_table->addColumn<int>("trk_SVidx", trk_SVidx, "trk_SVidx", nanoaod::FlatTable::IntColumn);

        iEvent.put(std::move(table), "SVTable");
        iEvent.put(std::move(trk_table), "SVtrksTable");
    } 

private:
    const edm::EDGetTokenT<std::vector<reco::Vertex>> svToken;
};
    
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SVTableProducer);
