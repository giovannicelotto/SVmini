import FWCore.ParameterSet.Config as cms

def GenVertexCandidateProducer(**kwargs):
  mod = cms.EDProducer('GenVertexCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
