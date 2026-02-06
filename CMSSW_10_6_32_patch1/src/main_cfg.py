# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --eventcontent NANOEDMAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --conditions 106X_upgrade2018_realistic_v16_L1v1 --step NANO --era Run2_2018,run2_nanoAOD_106Xv2 --python_filename HIG-RunIISummer20UL18NanoAODv9-12707_1_cfg.py --fileout file:HIG-RunIISummer20UL18NanoAODv9-12707.root --filein dbs:/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM --number 1395 --number_out 1395 --no_exec --mc


import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2
from FWCore.ParameterSet.VarParsing import VarParsing
from PhysicsTools.NanoAOD.common_cff import P4Vars, Var, CandVars
process = cms.Process('NANO',Run2_2018,run2_nanoAOD_106Xv2)
options = VarParsing('python')

#options.register('outputName', "",
#    VarParsing.multiplicity.singleton,
#    VarParsing.varType.string,
#    "output Name"
#)
options.parseArguments()
print(options)
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
    input = cms.untracked.int32(500),
    output = cms.untracked.int32(500)
)

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
processName = "outputBTV.root" if options.outputFile=="" else options.outputFile
process.NANOEDMAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:'+processName),
    outputCommands = cms.untracked.vstring(
        #'keep *',   
    'drop *',  # Drop everything by default
    "keep *_svTable_*_*",  # Keep event-level FlatTables
    "keep *_svCandidateTable_*_*",  # Keep event-level FlatTables
    'keep *_genVertexProducer_*_*',
    "keep nanoaodFlatTable_*Table*_*_*",  # Keep event-level FlatTables
    "keep nanoaodUniqueString_nanoMetadata_*_*",  # Keep basic metadata
    "keep nanoaodMergeableCounterTable_*_*_*"

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






#process.nanoSequenceMC += process.svTable
from mergedGenParticles import mergedGenParticles
process.mergedGenParticles = mergedGenParticles


from genVertices import genVertexProducer
process.genVertexProducer = genVertexProducer
#process.nanoSequenceMC += process.genVertexProducer



from sv_candidate_cff import inclusiveCandidateVertexFinder, candidateVertexMerger, CandidateVertexArbitrator, myCandidateInclusiveSecondaryVertices, vertexTable, svCandidateTable
process.inclusiveCandidateVertexFinder = inclusiveCandidateVertexFinder
process.candidateVertexMerger = candidateVertexMerger
process.CandidateVertexArbitrator = CandidateVertexArbitrator
process.myCandidateInclusiveSecondaryVertices = myCandidateInclusiveSecondaryVertices
process.vertexTable = vertexTable
process.svCandidateTable = svCandidateTable










process.nanoAOD_step = cms.Path(
    process.mergedGenParticles+
    process.inclusiveCandidateVertexFinder *
    process.candidateVertexMerger *
    process.CandidateVertexArbitrator *
    process.myCandidateInclusiveSecondaryVertices *
    process.vertexTable *
    process.svCandidateTable *
    process.genVertexProducer 

    #process.nanoSequenceMC
)















process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOEDMAODSIMoutput_step = cms.EndPath(process.NANOEDMAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(
                                process.nanoAOD_step,    # central nanoAOD step already included in nanoSequenceMC
                                process.endjob_step,
                                process.NANOEDMAODSIMoutput_step)
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
