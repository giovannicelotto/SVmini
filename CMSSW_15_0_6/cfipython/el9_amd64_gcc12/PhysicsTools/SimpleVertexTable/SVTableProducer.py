import FWCore.ParameterSet.Config as cms

def SVTableProducer(*args, **kwargs):
  mod = cms.EDProducer('SVTableProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
