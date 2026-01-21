# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --eventcontent NANOEDMAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step NANO --era Run2_2018,run2_nanoAOD_106Xv2 --python_filename HIG-RunIISummer20UL18NanoAODv9-12707_1_cfg.py --fileout file:HIG-RunIISummer20UL18NanoAODv9-12707.root --filein dbs:/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM --number 1395 --number_out 1395 --no_exec --mc

print("Start")
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
    input = cms.untracked.int32(30),
    output = cms.untracked.int32(30)
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

process.NANOEDMAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:HIG-RunIISummer20UL18NanoAODv9-12707.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v16_L1v1', '')

# Path and EndPath definitions
unpackedTracksAndVertices = cms.EDProducer('PATTrackAndVertexUnpacker',
    slimmedVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    slimmedSecondaryVertices = cms.InputTag("slimmedSecondaryVertices"),
    additionalTracks = cms.InputTag("lostTracks"),
    packedCandidates = cms.InputTag("packedPFCandidates")
)

process.load("RecoVertex.AdaptiveVertexFinder.inclusiveVertexing_cff")

process.unpackedTracksAndVertices = unpackedTracksAndVertices

process.inclusiveCandidateVertexFinder.tracks = cms.InputTag(     "packedPFCandidates" ) #https://github.com/cms-sw/cmssw/blob/712e925576cdaabfc2bc3abfb2162b38756f09ee/PhysicsTools/PatAlgos/plugins/TrackAndVertexUnpacker.cc#L54
process.inclusiveCandidateVertexFinder.primaryVertices = cms.InputTag(     "unpackedTracksAndVertices" )

process.candidateVertexMerger.secondaryVertices = cms.InputTag(     "inclusiveCandidateVertexFinder" )

process.candidateVertexArbitrator.tracks = cms.InputTag(     "packedPFCandidates" )
process.candidateVertexArbitrator.primaryVertices = cms.InputTag(     "unpackedTracksAndVertices" )
process.candidateVertexArbitrator.secondaryVertices = cms.InputTag(     "candidateVertexMerger" )

process.inclusiveCandidateSecondaryVertices.secondaryVertices = cms.InputTag(     "candidateVertexArbitrator" )




from PhysicsTools.NanoAOD.common_cff import P4Vars, Var, CandVars
process.vertexTable = cms.EDProducer("VertexTableProducer",
    pvSrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    goodPvCut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.Rho <= 2"), 
    svSrc = cms.InputTag("inclusiveCandidateSecondaryVertices"),
    svCut = cms.string(""),
    dlenMin = cms.double(0),
    dlenSigMin = cms.double(3),
    pvName = cms.string("PV"),
    svName = cms.string("SV"),
    svDoc  = cms.string("secondary vertices from IVF algorithm"),
    storeCharge = cms.bool(False)
)





process.svCandidateTable =  cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("vertexTable"),
    cut = cms.string(""),  #DO NOT further cut here, use vertexTable.svCut
    name = cms.string("SV_AVF"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(True), 
    variables = cms.PSet(P4Vars,
        x   = Var("position().x()", float, doc = "secondary vertex X position, in cm",precision=10),
        y   = Var("position().y()", float, doc = "secondary vertex Y position, in cm",precision=10),
        z   = Var("position().z()", float, doc = "secondary vertex Z position, in cm",precision=14),
        ndof    = Var("vertexNdof()", float, doc = "number of degrees of freedom",precision=8),
        chi2    = Var("vertexNormalizedChi2()", float, doc = "reduced chi2, i.e. chi/ndof",precision=8),
        ntracks = Var("numberOfDaughters()", "uint8", doc = "number of tracks"),
    ),
)

process.nanoAOD_step = cms.Path(
    process.unpackedTracksAndVertices *
    process.inclusiveCandidateVertexFinder *
    process.candidateVertexMerger *
    process.candidateVertexArbitrator *
    process.inclusiveCandidateSecondaryVertices *
    process.nanoSequenceMC*
    process.vertexTable *
    process.svCandidateTable
)
process.NANOEDMAODSIMoutput.outputCommands += [
    'drop *',
    'keep nanoaodFlatTable_vertexTable_*_*',
    'keep nanoaodFlatTable_svCandidateTable_*_*',
]
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
# End adding early deletion
