import FWCore.ParameterSet.Config as cms

def GenVertexProducer(**kwargs):
  mod = cms.EDProducer('GenVertexProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
