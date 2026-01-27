# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --eventcontent NANOEDMAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step NANO --era Run2_2018,run2_nanoAOD_106Xv2 --python_filename HIG-RunIISummer20UL18NanoAODv9-12707_1_cfg.py --fileout file:HIG-RunIISummer20UL18NanoAODv9-12707.root --filein dbs:/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM --number 1395 --number_out 1395 --no_exec --mc


import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2

print("Import done")
process = cms.Process('NANO',Run2_2018,run2_nanoAOD_106Xv2)
print("Import done2")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000),
    output = cms.untracked.int32(1000)
)
print("Max events done")
# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( (
        'file:/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/mini_1.root', 
     ) ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet()

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--eventcontent nevts:1395'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOEDMAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:HIG-RunIISummer20UL18NanoAODv9-12707.root'),
    outputCommands = cms.untracked.vstring(
        #'keep *',   
    'drop *',  # Drop everything by default
    "keep *_svTable_*_*",  # Keep event-level FlatTables
    "keep nano_svTable_*_*",  # Keep event-level FlatTables
    "keep nanoaodFlatTable_*Table*_*_*",  # Keep event-level FlatTables
    #"keep *_*_*_*",  # Keep event-level FlatTables
    #"keep nanoaodUniqueString_nanoMetadata_*_*",  # Keep basic metadata
    #"keep nanoaodMergeableCounterTable_*_*_*",
    #"keep TTree_Runs_*_*",
)
)
# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v16_L1v1', '')

#
#   START
#   SECONDARY VERTICES
#
#

process.load("RecoVertex.AdaptiveVertexFinder.inclusiveVertexing_cff")

process.unpackedTracksAndVertices = cms.EDProducer('PATTrackAndVertexUnpacker',
    slimmedVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    slimmedSecondaryVertices = cms.InputTag("slimmedSecondaryVertices"),
    additionalTracks = cms.InputTag("lostTracks"),
    packedCandidates = cms.InputTag("packedPFCandidates")
)

process.inclusiveVertexFinder = cms.EDProducer('InclusiveVertexFinder',
  beamSpot = cms.InputTag('offlineBeamSpot'),
  primaryVertices = cms.InputTag('unpackedTracksAndVertices'),
  tracks = cms.InputTag('unpackedTracksAndVertices'),
  minHits = cms.uint32(8),
  maximumLongitudinalImpactParameter = cms.double(0.3),
  maximumTimeSignificance = cms.double(3),
  minPt = cms.double(0.8),
  maxNTracks = cms.uint32(30),
  clusterizer = cms.PSet(
    seedMax3DIPSignificance = cms.double(9999),
    seedMax3DIPValue = cms.double(9999),
    seedMin3DIPSignificance = cms.double(1.2),
    seedMin3DIPValue = cms.double(0.005),
    clusterMaxDistance = cms.double(0.05),
    clusterMaxSignificance = cms.double(4.5),
    distanceRatio = cms.double(20),
    clusterMinAngleCosine = cms.double(0.5),
    maxTimeSignificance = cms.double(3.5)
  ),
  vertexMinAngleCosine = cms.double(0.95),
  vertexMinDLen2DSig = cms.double(2.5),
  vertexMinDLenSig = cms.double(0.5),
  fitterSigmacut = cms.double(3),
  fitterTini = cms.double(256),
  fitterRatio = cms.double(0.25),
  useDirectVertexFitter = cms.bool(True),
  useVertexReco = cms.bool(True),
  vertexReco = cms.PSet(
    finder = cms.string('avr'),
    primcut = cms.double(1),
    seccut = cms.double(3),
    smoothing = cms.bool(True)
  ),
  mightGet = cms.optional.untracked.vstring
)

#Vertex Merger step1 https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_X/RecoVertex/AdaptiveVertexFinder/python/vertexMerger_cfi.py
process.vertexMerger = cms.EDProducer( "VertexMerger",
    secondaryVertices = cms.InputTag("inclusiveVertexFinder"),  
    maxFraction = cms.double(0.7), 
    minSignificance = cms.double(2.0)
)

#Arbitrator step
process.trackVertexArbitrator = cms.EDProducer("TrackVertexArbitrator",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    primaryVertices = cms.InputTag("unpackedTracksAndVertices"),
    tracks = cms.InputTag("unpackedTracksAndVertices"),
    secondaryVertices = cms.InputTag("vertexMerger"),
    dLenFraction = cms.double(0.333),
    dRCut = cms.double(0.4),
    distCut = cms.double(0.04),
    sigCut = cms.double(5),
    fitterSigmacut =  cms.double(3),
    fitterTini = cms.double(256),
    fitterRatio = cms.double(0.25),
    trackMinLayers = cms.int32(4),
    trackMinPt = cms.double(0.4),
    trackMinPixels = cms.int32(1)
    # plus any additional parameters it requires
)

#Vertex Merger step2 https://github.com/cms-sw/cmssw/blob/557f39bce1d5cba35316c2358a89e888901a07e5/RecoVertex/AdaptiveVertexFinder/python/inclusiveVertexing_cff.py#L7
process.myInclusiveSecondaryVertices = process.vertexMerger.clone(
    secondaryVertices = "trackVertexArbitrator",
    maxFraction = cms.double(0.2), 
    minSignificance = cms.double(10) )

process.svTable = cms.EDProducer("SVTableProducer", src = cms.InputTag("myInclusiveSecondaryVertices") )
process.nanoSequenceMC += process.myInclusiveSecondaryVertices
process.nanoSequenceMC += process.svTable
#process.nanoSequence += process.svTable
#process.myVertexTable = cms.EDProducer(
#    "VertexTableProducer",
#    pvSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
#    goodPvCut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"),
#    svSrc = cms.InputTag("myInclusiveSecondaryVertexCandidates"),
#    svCut = cms.string(""),
#    dlenMin = cms.double(0),
#    dlenSigMin = cms.double(3),
#    pvName = cms.string("PV"),
#    svName = cms.string("mySV"),
#    svDoc  = cms.string("secondary vertices from custom vertexMerger"),
#    storeCharge = cms.bool(False)
#)


#
#   END
#   SECONDARY VERTICES
#
#


from PhysicsTools.NanoAOD.common_cff import P4Vars, Var, CandVars




# https://github.com/cms-sw/cmssw/blob/7507310cad2a51edad7517f124d1e8993ce0e1c8/RecoVertex/AdaptiveVertexFinder/python/inclusiveVertexing_cff.py#L7
process.nanoAOD_step = cms.Path(
    process.unpackedTracksAndVertices *
    process.inclusiveVertexFinder *
    process.vertexMerger *
    process.trackVertexArbitrator *
    #process.myInclusiveSecondaryVertices*
    #process.svTable*
    process.nanoSequenceMC
    #process.svCandidateTable
)
#process.NANOEDMAODSIMoutput.outputCommands += [
    #'drop *',
    #'keep nanoaodFlatTable_SVTable_*_*',
    #'keep nanoaodFlatTable_svCandidateTable_*_*',
#]
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOEDMAODSIMoutput_step = cms.EndPath(process.NANOEDMAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOEDMAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
#print("Start")
#print(process.dumpPython())
#print("End of Dump")
# End adding early deletion
