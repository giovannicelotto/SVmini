import FWCore.ParameterSet.Config as cms

def SVTableProducer(**kwargs):
  mod = cms.EDProducer('SVTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
