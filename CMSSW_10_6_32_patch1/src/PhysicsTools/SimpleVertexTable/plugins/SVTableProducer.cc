#include "FWCore/Framework/interface/global/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/NanoAOD/interface/FlatTable.h"

class SVTableProducer : public edm::global::EDProducer<> {
public:
    explicit SVTableProducer(const edm::ParameterSet &iConfig)
        : svToken(consumes<std::vector<reco::Vertex>>(iConfig.getParameter<edm::InputTag>("src"))) 
    {
        produces<nanoaod::FlatTable>("SVTable");
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


        std::vector<float> x, y, z, chi2, ndof;
        std::vector<int> nTracks;

        //std::cout<<svs->size()<<" SVs to process\n";
        for (const auto &sv : *svs) {
            x.push_back(sv.x());
            y.push_back(sv.y());
            z.push_back(sv.z());
            chi2.push_back(sv.chi2());
            ndof.push_back(sv.ndof());
            nTracks.push_back(sv.tracksSize());
        }


        table->addColumn<float>("x", x, "X position of SV", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("y", y, "Y position of SV", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("z", z, "Z position of SV", nanoaod::FlatTable::FloatColumn);
        //std::cout<<"[DEBUG] SVTableProducer added x,y,z columns\n";
        table->addColumn<float>("chi2", chi2, "Chi2 of vertex fit", nanoaod::FlatTable::FloatColumn);
        table->addColumn<float>("ndof", ndof, "Degrees of freedom of vertex fit", nanoaod::FlatTable::FloatColumn);
        table->addColumn<int>("nTracks", nTracks, "Number of tracks in SV", nanoaod::FlatTable::IntColumn);

        iEvent.put(std::move(table), "SVTable");
    }

private:
    const edm::EDGetTokenT<std::vector<reco::Vertex>> svToken;
};

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(SVTableProducer);
