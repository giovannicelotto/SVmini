import FWCore.ParameterSet.Config as cms

def DummyTrackValueMap(**kwargs):
  mod = cms.EDProducer('DummyTrackValueMap',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
