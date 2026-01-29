#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/NanoAOD/interface/FlatTable.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"

#include <vector>
#include <unordered_set>
#include <limits>
#include <tuple>
#include <cmath>

class GenVertexProducer : public edm::EDProducer {
public:
    explicit GenVertexProducer(const edm::ParameterSet &);
    ~GenVertexProducer() override = default;

    void produce(edm::Event&, const edm::EventSetup&) override;

private:
    edm::EDGetTokenT<edm::View<reco::Candidate>> genToken_;

    int checkPDG(int abs_pdg);
    std::optional<std::tuple<float,float,float>> isAncestor(const reco::Candidate* mother, const reco::Candidate* daughter);
};

GenVertexProducer::GenVertexProducer(const edm::ParameterSet &iConfig) {
    genToken_ = consumes<edm::View<reco::Candidate>>(iConfig.getParameter<edm::InputTag>("genParticles"));
    produces<nanoaod::FlatTable>("GVTable");
    produces<nanoaod::FlatTable>("GVDaughtersTable");
}

//  produce() 
void GenVertexProducer::produce(edm::Event &iEvent, const edm::EventSetup &) {
    edm::Handle<edm::View<reco::Candidate>> genHandle;
    iEvent.getByToken(genToken_, genHandle);

    const auto& merged = genHandle;

    // Output vectors
    std::vector<float> Hadron_pt, Hadron_eta, Hadron_phi;
    std::vector<float> Hadron_GVx, Hadron_GVy, Hadron_GVz;
    std::vector<int> Hadron_Idx;
    std::vector<float> Daughters_pt, Daughters_eta, Daughters_phi;
    std::vector<int> Daughters_charge, Daughters_flag, Daughters_flav;

    int nhads=0, ngv=0;
    int ngv_b=0, ngv_d=0, ngv_s=0, ngv_tau=0;

    for(size_t i=0; i<merged->size(); ++i){
        const reco::Candidate* hadron = &(*merged)[i];
        //std::cout<<"Hadron "<<i<<" PDG ID: "<<hadron->pdgId()<<", pt: "<<hadron->pt()<<", eta: "<<hadron->eta()<<std::endl;
        if(!(hadron->pt()>10 && std::abs(hadron->eta())<2.5)) continue;

        int hadPDG = checkPDG(std::abs(hadron->pdgId()));
        if(hadPDG==0) continue;

        //  Collect stable charged daughters
        std::vector<float> temp_pt, temp_eta, temp_phi; // kinematics of gen daughters of the hadron in the loop
        std::vector<int> temp_charge, temp_flag, temp_flav;
        int nPack=0;
        float vx=std::numeric_limits<float>::quiet_NaN();
        float vy=std::numeric_limits<float>::quiet_NaN();
        float vz=std::numeric_limits<float>::quiet_NaN();

        for(size_t j=0; j<merged->size(); ++j){
            const reco::Candidate* dau = &(*merged)[j];
            if(dau==hadron) continue;
            if(!(dau->status()==1 && dau->charge()!=0 && dau->pt()>0.8 && std::abs(dau->eta())<2.5)) continue;

            auto GV = isAncestor(hadron,dau); //takes the x,y,z of the daughter (decay point of the hadron)
            if(GV.has_value()){
                std::tie(vx,vy,vz) = *GV;
                if(!std::isnan(vx)){
                    nPack++;
                    temp_pt.push_back(dau->pt());
                    temp_eta.push_back(dau->eta());
                    temp_phi.push_back(dau->phi());
                    temp_charge.push_back(dau->charge());
                    temp_flag.push_back(ngv); // hadron index
                    temp_flav.push_back(hadPDG);
                }
            }
        }
        // If has more than 2 good daughters, the Hadron is Good, we found a GV:
        if(nPack>=2){
            // Save hadron info
            nhads++;
            std::cout<<"Found hadron "<<nhads<<" PDG ID: "<<hadron->pdgId()<<", pt: "<<hadron->pt()<<", eta: "<<hadron->eta()<<std::endl;
            Hadron_pt.push_back(hadron->pt());
            Hadron_eta.push_back(hadron->eta());
            Hadron_phi.push_back(hadron->phi());

            // Save GenVertex
            ngv++;
            if(hadPDG==1) ngv_b++;
            if(hadPDG==2) ngv_d++;
            if(hadPDG==3) ngv_s++;
            if(hadPDG==4) ngv_tau++;
            Hadron_GVx.push_back(vx);
            Hadron_GVy.push_back(vy);
            Hadron_GVz.push_back(vz);
            Hadron_Idx.push_back(nhads-1);

            // Save daughters
            Daughters_pt.insert(Daughters_pt.end(), temp_pt.begin(), temp_pt.end());
            Daughters_eta.insert(Daughters_eta.end(), temp_eta.begin(), temp_eta.end());
            Daughters_phi.insert(Daughters_phi.end(), temp_phi.begin(), temp_phi.end());
            Daughters_charge.insert(Daughters_charge.end(), temp_charge.begin(), temp_charge.end());
            Daughters_flag.insert(Daughters_flag.end(), temp_flag.begin(), temp_flag.end());
            Daughters_flav.insert(Daughters_flav.end(), temp_flav.begin(), temp_flav.end());
        }
    }

    //  Build FlatTables 

    auto gvTable = std::make_unique<nanoaod::FlatTable>(ngv,"GV",false);
    gvTable->addColumn<float>("pt",Hadron_pt,"Hadron pt", nanoaod::FlatTable::FloatColumn);
    gvTable->addColumn<float>("eta",Hadron_eta,"Hadron eta", nanoaod::FlatTable::FloatColumn);
    gvTable->addColumn<float>("phi",Hadron_phi,"Hadron phi", nanoaod::FlatTable::FloatColumn);
    gvTable->addColumn<float>("x",Hadron_GVx,"GV x", nanoaod::FlatTable::FloatColumn);
    gvTable->addColumn<float>("y",Hadron_GVy,"GV y", nanoaod::FlatTable::FloatColumn);
    gvTable->addColumn<float>("z",Hadron_GVz,"GV z", nanoaod::FlatTable::FloatColumn);
    gvTable->addColumn<int>("hadronIndex",Hadron_Idx,"Hadron index", nanoaod::FlatTable::IntColumn);
//

    auto dauTable = std::make_unique<nanoaod::FlatTable>(Daughters_pt.size(),"GVDaughters",false);
    dauTable->addColumn<float>("pt",Daughters_pt,"Daughter pt",nanoaod::FlatTable::FloatColumn);
    dauTable->addColumn<float>("eta",Daughters_eta,"Daughter eta",nanoaod::FlatTable::FloatColumn);
    dauTable->addColumn<float>("phi",Daughters_phi,"Daughter phi",nanoaod::FlatTable::FloatColumn);
    dauTable->addColumn<int>("charge",Daughters_charge,"Daughter charge", nanoaod::FlatTable::IntColumn);
    dauTable->addColumn<int>("hadronIndex",Daughters_flag,"Hadron index", nanoaod::FlatTable::IntColumn);
    dauTable->addColumn<int>("hadronFlav",Daughters_flav,"Hadron flavor", nanoaod::FlatTable::IntColumn);
//
    iEvent.put(std::move(gvTable),"GVTable");
    iEvent.put(std::move(dauTable),"GVDaughtersTable");
}

//  checkPDG() 
int GenVertexProducer::checkPDG(int abs_pdg){
    std::vector<int> pdgList_B = {521,511,531,541,5122,5132,5232,5332,5142,5242,5342,5512,5532,5542,5554};
    std::vector<int> pdgList_D = {411,421,431,4122,4232,4132,4332,4412,4422,4432,4444};
    std::vector<int> pdgList_S = {3122,3222,3212,3312,3322,3334};
    std::vector<int> pdgList_Tau = {15};

    if(std::find(pdgList_B.begin(),pdgList_B.end(),abs_pdg)!=pdgList_B.end()) return 1;
    if(std::find(pdgList_D.begin(),pdgList_D.end(),abs_pdg)!=pdgList_D.end()) return 2;
    if(std::find(pdgList_S.begin(),pdgList_S.end(),abs_pdg)!=pdgList_S.end()) return 3;
    if(std::find(pdgList_Tau.begin(),pdgList_Tau.end(),abs_pdg)!=pdgList_Tau.end()) return 4;
    return 0;
}

//  isAncestor() 
std::optional<std::tuple<float, float, float>> GenVertexProducer::isAncestor(const reco::Candidate* ancestor, const reco::Candidate* particle)
    {
    const reco::Candidate* current = particle;
    //const reco::Candidate* child = nullptr;

    while (current != nullptr && current->numberOfMothers() > 0) {
        const reco::Candidate* mother = current->mother(0);
        if (mother == ancestor) {
            // Found the ancestor; return the vertex of the current particle (i.e., the direct daughter)
            return std::make_optional(std::make_tuple(current->vx(), current->vy(), current->vz()));
        }
        //child = current;
        current = mother;
    }

    // If we reached here, the ancestor was not found in the chain
    return std::nullopt;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(GenVertexProducer);
