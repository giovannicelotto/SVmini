import FWCore.ParameterSet.Config as cms
genVertexProducer = cms.EDProducer("GenVertexCandidateProducer",
    genParticles = cms.InputTag("mergedGenParticles"),
    secondaryVertices = cms.InputTag("myCandidateInclusiveSecondaryVertices"),
    nRequiredCommonTracks = cms.int32(1),        # number of tracks required to match the genDaughters
    dR_max = cms.double(0.03),                                   # dR between tracks and daughters to be considered matched
    relPt_max = cms.double(0.5)                                 # dPt/pt between tracks and daughters to be considered matched
)