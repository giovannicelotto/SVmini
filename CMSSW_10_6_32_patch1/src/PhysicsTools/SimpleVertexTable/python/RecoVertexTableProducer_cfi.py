import FWCore.ParameterSet.Config as cms

myVertexTable = cms.EDProducer("RecoVertexTableProducer",
    src = cms.InputTag("offlineSlimmedPrimaryVertices"),  # or another reco::Vertex collection
    name = cms.string("mySV"),
    singleton = cms.bool(False),
    extension = cms.bool(False),
)
