# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --eventcontent MINIAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier MINIAODSIM --conditions 106X_mcRun2_asymptotic_v17 --step PAT --procModifiers run2_miniAOD_UL --geometry DB:Extended --era Run2_2016 --python_filename HIG-RunIISummer20UL16MiniAODv2-12236_1_cfg.py --fileout file:HIG-RunIISummer20UL16MiniAODv2-12236.root --filein dbs:/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/RunIISummer20UL16RECO-106X_mcRun2_asymptotic_v13-v2/AODSIM --number 965 --number_out 965 --runUnscheduled --no_exec --mc
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.ProcessModifiers.run2_miniAOD_UL_cff import run2_miniAOD_UL

process = cms.Process('PAT',Run2_2016,run2_miniAOD_UL)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.PatAlgos.slimming.metFilterPaths_cff')
process.load('Configuration.StandardSequences.PATMC_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(965),
    output = cms.untracked.int32(965)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( (
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/0141AFA3-A3FD-F541-AFFE-9D6350E69FDB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/077AA751-DEA0-DF4E-977E-8788111F48CC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/0C4A5BF0-06CA-4047-95B6-112F87F737A9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/2A954001-54B4-8442-B3DE-D819CF08726C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/335AFA16-32AD-D340-84BB-DD06CA165C27.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/341E7749-D5EF-9E4C-A141-C69A7BA434E4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/3515EDBB-8490-7C40-89E2-2D27DBEC4092.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/40FD6922-E03A-5E46-B425-248F354DF1C8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/450E86A9-A227-5F42-8658-F1939D8ED774.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/46C620DD-D8E2-5A4B-81E7-E44F494A0747.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/4843C0D6-FC81-D844-BEBE-72FA73DC3B59.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/4B6A8DB1-87D2-3F41-BBA9-3C549A484B64.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/5396D592-89ED-AC4C-969D-54397EDD941F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/56CD3BBF-7517-2E49-BFD7-E26902BD436F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/5EB8EF95-49C9-C646-B6FD-A7D389E47E98.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/5FE61DF0-AACB-084A-A05A-1D0F533DB134.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/60DF01AB-72BD-D24D-B7B9-67BF6861F6E3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/635C84E0-5573-E047-875A-A59CDF915E98.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/654CD61B-EB9F-5949-BD47-21D22832CA14.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/6877ABF4-2C96-AA4F-B879-88496E73B355.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/692EEF5D-8344-6E47-9CC5-69A5B2D2C89D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/6CFB6F86-4C4C-B346-BEF4-1EDAB99B5DDC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/75E26D70-9652-B948-AEB1-C80AE7442A0C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/83DE567F-9801-724C-990C-E916145761D1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/85A51BE8-6C74-EB4A-BB21-D67328E6A8D4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/950B3403-930F-0741-BF98-76929A532CCD.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/97368BB4-A89E-C349-96BF-D2144029C1C9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/A2611232-A193-3E45-ABAC-50C6B35FBA1E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/A4E407F6-47A2-EE4D-B10B-3741FB4DCEA9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/B92B3330-6873-2040-9269-36254BB9296A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/BFB95384-EB37-9F45-89A1-57A9F64AD6C9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/C15C6990-66D3-DC4E-9C8B-D385B2A69645.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/C9D7A1C2-F043-4F43-8931-22467B787422.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/D72A16F8-785F-9644-AA00-95F294393CA9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/DA41024F-8EBC-ED43-8EBD-6C85A4AC4D48.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/E25E95C8-517A-8B4E-B43B-6BD177069AE6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/E2F6EF6F-07E3-B74E-8430-E52E679BA1C7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/E3C5DAE0-3BBD-1742-8B6B-A21DC2A1356C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/E6D15B80-8EE7-8348-B70A-6ADDE44A202D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/F03612C4-47C4-FA4A-BBA1-147FEBA9B1AF.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/FD3B0C74-BDDE-7244-A5FF-1AA5A1F44978.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2810000/FD8283DD-8BD7-474B-9509-D22076201400.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/0098C87A-A55D-9E48-AC6C-C661DD107861.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/023810B2-6AF9-9F4F-A0A1-580047117EC6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/02B39990-17E2-FE4C-B8D5-4862978B96BF.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/039872FD-1E4A-9F41-B89D-A15132389BD1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/04E856D0-DD86-2547-9D8A-AA1BE82CA62C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/07D8F6DA-E821-344F-90CC-065D093DA6A1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/08A617F8-5B1E-DC4B-9DD3-03B692BBF73A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/0BD70B2D-CAD5-1140-AE52-AF8E0E7929AF.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/0C226561-9574-5B4B-B134-15950F96931E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/0DE78222-F519-654C-B883-F0E01DAAD17F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/0E7B5677-54D1-014B-8252-AD0C01825D44.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/0F39BC85-34B1-2444-A51E-5C1101AEDEF6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/102349CD-5C21-294F-A45A-7D12CD7C62EA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/16ADAB2E-155A-FB45-8B3D-0AAB1148F610.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/197501DC-BA13-C147-8FB5-893A071F8993.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/19ECB678-8C60-6D49-B2B9-86DE889536AF.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/1A6FA48E-E551-5942-9E47-5C531D7524D1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/1A898E2F-BF00-BD4E-ADA3-5BBB184568E1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/1B51BB2B-2A58-7C4F-9652-BFF7DF5400E6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/1D2B450A-23CF-EE48-AA98-952521AD36E9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/1D58DC20-C2E4-4243-9F8B-6C17C73C642B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/20C1F4F7-F633-E843-B798-4F221A9F6244.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/213C9222-0CDD-8645-A87D-37CDD236476D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/21FC679E-2035-3748-9810-3CFCA95D3E3C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/226B479E-26F0-9E46-ACEE-A3536448A637.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/23B8C64B-E673-0D4E-B327-720328C0334C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/255618CE-5212-7A40-94AD-FA514F225175.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/25957401-0503-FC4F-B7A8-99ECDCD896B3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/25FF23D8-B3AA-2442-9F4C-EAADD1B92DA5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/26F57A2F-B9A4-4C47-BAD9-2DFCFF811447.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/27AE3504-C092-244A-A19D-10BCA98E311C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2966B18A-9DCB-9743-9118-9FC30B2A9F00.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2A2A9EE5-A53A-3649-818C-2D0FC513F3AE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2A3A5E49-1B9C-BF49-A2A1-CE9898B40B8F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2A4CCCF1-40F8-9D45-B0ED-5F80BF6655C6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2AEDBF84-107E-9544-A8DE-12B59D5FD806.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2AF46C14-45E7-534D-8EC4-2B7C66CBA404.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2BFE63B9-0A97-194E-A343-860493614A01.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2F599A03-3AF6-EF42-B106-0A27ED490712.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/2FD979E1-CA33-3946-85F1-35323D6D1E28.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3022CE66-7A81-8D4B-BDD3-832D085F19E9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/30FAA123-EFB6-254D-837E-68B539E915A2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/32CA9D2F-8C63-2B48-A90A-DEB5EEC81384.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/34A25ADD-D403-804F-ACFA-318AC7830E5F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/352F4B0A-7C2B-0245-90C1-B286C4B688BC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/35C0F296-CD1D-F849-914C-FFE2DBA216F4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/36444575-779B-FE4C-8211-EF9CC897773A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/369FFBA7-AE53-534E-9A45-4518284F87C4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/383F4D97-30EF-184B-ADD3-EB494CBEBCA6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3928403D-3541-4D41-BA23-AEF1EE10730E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3A8F8AF0-546E-1C41-A2D4-2DE41F284A31.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3B1070F2-34C8-084E-8EE7-19D7B4B4CEC7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3B1BCF43-C9BF-EA4E-A90D-7B861A721B49.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3DDFE17E-E4DD-974E-A701-CF8D760DADDA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3E6CFA84-2F1C-E645-A16E-7632067F92FC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3EF16FB7-0F07-E140-AF99-941515A28483.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/3FB179E8-CFD9-3C4D-A858-435BE2D70E66.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/403FE6F3-5D3F-A849-9D43-7F341A971DF5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/44A7CC04-A116-5B48-9C37-33276394BCDA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/466D27A8-4E9C-DA42-9987-916B79AA8A1F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/480C638B-328B-484E-9D5F-D3719B0ED5C3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/4BD72101-C625-594F-A9CF-5E8AF03E6FDD.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/4C5A46AE-BAF4-964D-AC4C-99BFC7A741D6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/4D97CC0C-FE80-A14A-AEEB-F4B5DBE7DCA7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/4E0FB2E4-5E3E-B74D-9E3B-BB63B544768A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/4E2B4C87-E4D0-D241-9ABB-1D0B36F4598C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/4E7E9C7A-DCD4-EA42-AB1E-9F14952D67A1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/4EC45C7C-48AE-8940-912A-2C5D89251ECB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/53DC288A-C3DE-A348-B989-3336399D92F1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/5756F96C-301C-8C45-801F-91A9722A5EB7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/59B8B873-274D-824E-959A-98F44229D9EC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/5A990688-BCA7-CF47-AACE-EFF8F8BAF9D0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/5E0D4581-DB1C-3848-9AF6-FAFB20A34021.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/60B1D872-0A25-1D4A-A704-F4988A18A3D9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/645AC55D-A6C9-C442-8AA9-358BF0E37D82.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/64BF6877-8B05-8246-BCC2-D0E938EAA878.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/65210CBA-3AA7-BF4A-8EDB-A8BD18C40558.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/6560DED5-C6D1-CC4B-B162-0E9F4CEACC45.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/65CCCA79-96DA-174C-AE24-FAC9B0D20459.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/68E764AC-275E-CF48-A41A-3BAE8E65E0AB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/6B852291-7418-5343-8815-89A90223B41B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/6E341063-F5F8-E947-908A-E2172C497423.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/6ED39E36-05D0-E849-976A-E531E77DEAE8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/71970697-A1CA-1F4B-B8CC-F349743D2AD1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/71AAFA47-2699-C14A-8BA1-A83394630132.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/72E42830-1AA9-6941-B52F-0898AEB61960.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/736D6362-E78A-8A48-98E5-8BFB28CE607E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/73E6A723-900F-8042-A959-74E8A26E8357.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/76A464D2-59E6-A340-80D6-D5AE23294C7D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7711EFF1-54BC-7F48-92CD-A5A40FEE77F7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/79CAF1D7-82D6-6041-A7ED-F7891C03BA5D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/79CB04FC-AC37-3749-B06E-0F1DA6519246.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7A267F84-47B0-DA4D-AA83-0C4347BB571A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7A5D14C9-ECB7-6048-AAD3-9D6FA1FA99A1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7D58F8D0-AEDA-9D45-B352-BE5F98A40B19.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7D7DCA08-7A5A-0940-BAD1-3EFC9BFDAFE2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7E50FC62-5629-2148-8F05-C122173253ED.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7E93CD68-CF7B-DC43-8029-BBB2A63CB7B9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7F4894D2-1170-A84F-A15C-72B851398C97.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7F983477-C620-3A44-B3E1-ABECD0880106.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/7FC5BEDE-A624-564A-B807-BA4A2F3D004C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/834F99E9-F305-1544-9BCA-A0B04EAD3421.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/844B51C7-B076-DC4A-A5CB-1A85C3238F87.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/845AE16E-6F82-214C-A049-7A4729CCAFF5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/8468F88B-4596-F14E-A0F7-808FBA469513.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/85340C0C-A97B-6B49-85C2-82B848589593.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/85D63323-D801-F74C-BF8E-AFCF94781203.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/86D3FC79-00BD-6F49-90D5-E96E694BF146.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/88423341-EF43-2A4B-AED2-04E5F0519A35.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/88AAD7A3-0471-2E47-8B50-1CD6BB5C49D8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/8921E04B-CBCD-E045-87AA-7FA49C8D8937.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/89A1380C-4B55-C24F-B54A-7D3DFB9CDB16.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/8BED15B4-2006-9C4B-A579-9CF781BB6381.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/8CE2EDAB-95E9-4C44-8544-6383A6C0CA8A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/925B0BD3-2991-EB49-8E57-CDBC1D9596A7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/95D60F7B-43C5-3746-8DC7-28E82AD49FC2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/967A25DE-6B73-CE45-A492-B2E046650F62.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/96E021D6-406D-804E-9380-E9603EF66227.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/973DCDFF-114B-1D40-83F4-FF6590A2C8CE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/974CDF90-08A8-444F-A33C-E281444DDA89.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/9980ACF1-DA56-B749-A60A-C8E1F0BF6F49.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/99882952-534C-FE4E-B98F-FE6BBDE58078.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/99C575E3-21FE-2546-A449-219EB0B0AF4C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/9BA05660-B587-574E-BD22-6068D4AE6AFC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/9EC9A010-ED1F-A043-AECF-4837C0B1D5F3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A1F401C8-5BBC-0045-A600-85593A5AC496.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A21B0096-CF81-E04B-969E-5896C9384E43.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A447A630-D3D2-BC48-B051-2E589EB85225.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A47024B3-7602-664C-943D-C0D9D29D6843.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A4AD8FA9-E397-8145-992D-53C5FB033DDE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A4C297CC-FBDD-184E-B169-ED6399FC5DF5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A5604158-4CFB-7049-BC32-97BBBABFB3DA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A5902B9D-6CE4-6440-A4C7-08E7AEB03B94.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A61FB7A4-3371-4945-962E-C29B10B0CC5E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A638EFC0-762C-3944-B7D1-B24FB797E2CE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A6594EFA-69E5-424D-B195-13EB4AF7156C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/A7558F29-5A91-7A42-90A5-8B9DAF04B0A9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/AB381C7E-6FAA-E248-BF93-872900D31A0F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/AB753A2D-4273-A647-98AA-8F91DDB6B315.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/AD4E3849-EBB8-DC4F-81B8-99D58D1E4F5E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/AEFDB642-0F4E-F746-912A-B43A899DD02E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/AF6236B4-70B0-024B-BB26-917A2FF2FF79.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/AF869A33-F2E9-B44A-89E1-2F18A805B3EA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/AFE3062F-9B59-D44D-8627-795947B2531C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/B2A33877-6108-2C4E-8BBF-B8AE84D62737.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/B2BA2BCD-07C5-7046-8F1E-622655453D59.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/B3F51A9D-6773-8F41-8B81-79E2A38FA35A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/B6A295DD-E2EF-174C-84B7-3E73A9D55EE5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/B70468FA-7603-7F4D-B6B5-DB4A2039A3C5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/B9ECBB90-97E6-4643-97E7-79BB533FBDE0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/BA2D6503-BDA5-054D-876A-AC53D08B7125.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/BABFA202-DAF8-1749-9EBC-66C4ED4F7835.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/BAF85DDB-D4DD-8545-B4B4-2E5A4EE687DE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/BD705C0E-84D2-264D-BF25-9877C98B9377.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/BDA67125-0E30-C74B-B3A5-59429DBEFF99.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/BDE317E3-A856-1D44-AF2E-207B163741F8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C223A188-1B65-5248-AE9B-2A5FA3E4A071.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C2695868-0631-8D42-9FD6-AE8EEFCA05E8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C4546730-957C-284D-B5B6-7CEF1875CE45.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C50B9BCC-56F4-5144-A078-4D07EFFEE0AD.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C5B043A1-0D49-FD4A-9933-1F53E9381333.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C69B4B83-BA75-4744-9FE9-C676FCBCAEC8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C6D629E0-D083-1B4A-BE81-A7075717049F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C6E95E30-5518-DB43-BF52-0EE47474FF7B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C7208633-D0C9-7045-9920-6FE685F8A417.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/C9AEDB04-61D0-E545-96C5-16EBEB4B36A3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/CACAA13E-9127-4142-929F-5D88054DFD05.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/CAFFDD41-DFE6-E04E-A0D3-A91045CC938F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/CC7C99C0-AD4A-B349-BD9E-2875375795F0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/CC806314-57EE-6742-930C-4189952C605E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/CC962FAC-26B3-5846-A614-7CA4C6C6413E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/CD080113-1097-5342-81CB-D48F2C94F5C2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/CF6ABDEB-AB88-A742-9034-FD4C2BEA2FDE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/D23581D7-522B-434B-9A87-DD6570C1E5C4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/D337D1E8-C1DF-DE48-97DD-A0953FD27344.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/D37F5CE8-74F7-1445-8500-1F052ABCE16F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/D53C151C-196C-214F-84CF-DE9BAB0A24C5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/D7F52547-91CC-0642-88FC-EBC68D824C14.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/D8299D9A-E2C0-7448-AEFE-0D303EFE5F68.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/D8414EBB-73FF-B947-94C5-BA6DC165FA65.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/DAA88E7A-3772-8A44-A0A2-B9B2628E4881.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/DC25DB7D-5B7E-6E45-B83B-6CCBA67770FF.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/DC4297E7-5111-A940-A55B-50E6DAE79D6D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/DD38FDC0-C6E3-DE49-8E5D-B5B9928064A0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/E0D62FE2-FC5F-1C48-9374-B6A5BE8BA682.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/E30C0329-BFED-9D43-88F4-F4B5E01F8D23.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/E4EBDCE1-FAC8-3A41-BDD0-13B91E00F9EE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/E543D078-D37B-0040-A2D8-38BA9715729C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/E6C88550-C13E-D347-AD47-AD696E1A2FA6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/EB777795-8E55-A247-A5B4-6F7C622815DC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/ED239597-AEA5-2842-A076-2FBF39D019A2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/EE60D188-D3BB-A244-B913-F8F973DEA7F9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/F0045A79-4EFF-364E-B83F-C338A031CC86.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/F1D2793B-B025-6D44-A6F9-DE992275D5B2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/F902EC18-E65E-5B4F-BBCA-EB75008B3ACB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/F985DC8E-F204-8740-8776-116C932F3452.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/FA6B467D-EEDB-4F4A-AC8D-A3429BD2B74F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/FB4DF9D6-2E65-9C4B-9F7B-9080D5857C06.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/FB724714-80B3-5345-B2D2-A573A405B624.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/2820000/FF6508DE-6CB8-6A41-9E05-0552E285588F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/0003A975-E69F-A046-A4F9-0A954A03A0FE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/00250652-81FD-F549-A5F5-237FBD597688.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/02A4FA1C-8E44-0B48-875C-210C57A75EA1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/0303057D-5484-B94C-8CC2-46E85CB64A2B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/048DBD15-62D1-EF42-A3D8-16276170AC67.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/04F1CCBD-B177-F243-A229-87A84C72ED91.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/06052336-A603-4549-98A8-8C0C2C230FB8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/06DA6624-633A-6F41-89FB-C6C6CD027BC4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/06DCEF94-5348-4842-925F-051EEC21B00A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/15C132DD-4739-2C44-968C-D0D869B9D7C8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/175ED367-8A7B-2B44-98B4-13DBD0A79668.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/19080DCF-1BCB-1647-A67F-3C53283FCB62.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/1991FD51-ACFB-704B-9713-982545C123A7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/19BAD2E4-F762-5945-BABB-FC61BE27B015.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/208B3DCA-382F-1A40-B890-D45D7C9C0AE5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/2141E0FF-F023-0B48-A7DD-515332DFEDAC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/214BC133-0673-7242-B4DF-19E24D44950D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/22E7FC39-0B3F-3A40-AA2C-830C52BB0185.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/23938CC0-AE87-D541-8644-2371B0D410B5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/23AD7056-0DC9-A749-AF72-06CDD9D7662A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/23F4C54D-C8EE-9B4E-A9A1-F7CCE40CDAF5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/2501D216-75C9-F843-AC3F-CAC8B66D2D71.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/26A9E6B1-9D22-0D43-B814-38D94B913BF5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/274EB3DD-C41F-3642-A1C3-F8BF04EEFB0D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/28106569-49EE-814C-84E1-89C66F366AAB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/28722302-F32E-1D46-9A14-20B017208189.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/29122898-78BF-B540-AD22-66A2CA9769EB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/291D3C46-9B2A-4C4C-8723-FC8AB877EC98.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/2A865EF1-C0ED-6242-8768-64839C80CF03.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/2ABA8071-6CD7-4A4F-8AF7-7785C0FE8584.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/2ADE571B-9016-6F4A-B975-51802EAB72A0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/2B1286A6-45C7-454E-B9B2-1A0AA27830CD.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3004F314-8F99-EE48-9671-4F6129D5493E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/31064FF8-9887-A14B-83BC-70F5221614FE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/315CA5C2-A1E3-4D49-93C1-2464789A8641.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/34281B7B-CC1A-6743-A97A-FBB15A5FD0D9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/34F8E43B-8018-854F-92CA-B4491657AB93.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/356896D7-053B-5745-B09C-FA3E677644AD.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/38008B05-C1AD-164A-A69C-D5315913291D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/393A4877-1C7C-4C44-9F09-4D55FDE5CECC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/39F5E48D-86DC-5B4C-9A8A-BE4D3D27C8CB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3BFEA6CA-3909-5143-B25A-8ED8AC090292.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3D8C3E2E-E8A4-334B-A694-F0BE03F4399A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3D97AED7-D212-1C4E-A779-E87BC266585E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3F238547-1AFC-8646-A378-B827D38206B4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3F9F67CE-952C-DE48-BD77-D35E76D405D0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/3FCB3778-5ABF-5E42-B005-99B0890A4A58.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/44ACCC8D-3343-8947-810F-CD969EE53D32.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/45F32702-BB89-744F-BEDA-4ACDFE0CDF3A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/460B1598-591D-BE43-B0C9-4089F106E89E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/48FB24AC-0368-6E4F-9386-B3CD77714678.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/4A4B8E5E-F59D-5640-B3A4-2DDECCBBC433.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/4B07EBE6-0AE7-B340-BFDA-D9ED6FB10706.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/4F874C0E-D0E8-0E42-9427-FF57F65B3874.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/51E8194C-E49E-9343-8901-80E0990716F4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/530F94C0-233C-F44D-ADC3-740E592F120C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/539E8D8E-FCD0-F545-9583-C1A0B2CC14F5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/54A74E41-AEE1-8749-96FB-D3D6AB3ECF0B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/54DF20E8-697A-3D47-B902-8C4CA208709B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/599C2F21-DEE3-B844-9CF2-BCE69F682D3D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/5F1049E1-0A7B-7249-9D07-44827FA0E843.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/60271BC0-CB96-8D44-ACE6-66F0D6FE31FB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/6241A355-7E4C-824F-B782-4A3D2CC74C4E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/62EC67DD-3192-DA48-8C04-60DBFABF154D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/62F36E6F-70F4-8044-B1D4-488BFD2A156B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/65139CBF-F55E-AE47-BDB5-08A2CFABFBD8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/66070680-131D-004E-9CA1-E984175ABF53.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/68A81716-6039-2540-B5D6-F2B73D93B191.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/695CFD01-9FF5-A941-A18F-D159F2CB65B9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/698D43F0-C887-A647-8004-4FAC163744B5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/69DBB537-4822-9648-BB83-96EAEDF4F218.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/6A776408-7D52-244D-983C-27517012F21C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/6E1DC9D5-A84B-0348-9821-BC541F492FFC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/6E5F292F-27B8-7B43-8EDE-352A24BE743C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/6FF810E0-4907-8E41-AF12-DEB0082CF36D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/704A9FAB-90BA-BF42-A563-B6B49FEE7168.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/70F249C9-8052-3E4F-BBC1-70B6EEEC98E0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/725B8634-19AA-0640-9B1B-E35CCFE99493.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/74D760FB-2BEA-C745-B366-4C769E6C0D86.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/75B15EB7-D28E-344D-AAC3-138B6A891FC8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7701B902-24C5-5442-85C7-8C1DF15B7130.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/776AA111-A071-A942-A1FC-EE00EF42433F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/78D66A9A-F81B-8D46-BE16-2FA0036D59D3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/793652BD-D5F1-E444-A966-6C2D2C2AD74C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/799A0566-D490-A343-BCA9-562E608884FC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7A23413A-AC01-AA48-92CD-EE73F8AEC618.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7B788ABA-6FD3-154B-AEA1-D4CD836265FD.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7C4EEC4D-DF79-0B4F-911A-4EE4F88347C1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7CA3F5E8-208D-2441-A73E-52ED3EED578A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7CBAD1AB-B2BF-BF48-B933-158B191B8D07.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7E2C86A9-9C00-6943-8814-F41FFE86B95A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/7EFCA662-A6FB-2A4F-BDD6-1637169184A7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8442E5D0-49DD-9841-950E-B5870F4DD528.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/85D1CE89-A870-7644-9C5E-42DC62DC2743.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/88365A05-35E5-8E49-9C1D-17304A822BC6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/886A5AD9-0DE8-2B4F-90F7-E2BFB4C78A48.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8B531608-4B51-724B-BB11-3926DC05551D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8C7B2E06-71AF-5743-8727-941445D5524E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8CEC5857-A53D-CA4B-A3BC-DADDC5F30254.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8D0571E8-3C47-4447-9DCC-2710936D7D8E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8D89EBCE-D64D-4D4F-93C5-6FE088255D19.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8DAC0B2B-5F3F-6048-8D63-5BE1949C228A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8E8AD11A-0A91-F84C-934E-2C17C9DB44B4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8ED5C4F6-3A6F-2642-82F9-37C8BA387457.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/8F2E8751-CFCA-4E4E-912D-EBCBE38AA8DE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/91C6675B-E13A-904A-9B42-2D28BCB388A0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/92B86A44-F657-7741-88FE-1FEFDFF840E2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/956E7DC7-D3F4-7744-91FC-7E1E54519D0E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/9916F43F-B990-2842-870A-97052C0BABAF.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A491A761-2B8E-A048-98B8-182B7E381898.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A5C04E4F-5338-6148-810F-92DAA0362492.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A5D013EC-38E7-FC4D-93F2-6601C045CE96.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A8B77E6D-FC2F-184F-9E54-45BC1FB1AB64.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A935B76B-44B2-9049-896D-D3C1E31537A1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/A99A2AEB-A35D-0A4A-B36A-8FD87CBA9992.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/AA27C41B-D518-1746-8A17-DEB55A8A8947.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/AAD0D04E-3C23-C145-82C4-D6C8C630E254.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/AC7C9943-3806-644E-AC3E-82269D4D7846.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/ADCA2C15-552F-4B4C-898C-A6240ED378CA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/AF65A7E3-C9C9-494F-8F58-3E965DC98E91.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B02D08A1-79CC-6C41-979B-9956F884ACDC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B13F45F9-8B9C-2F4A-BE92-1F5585D5339F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B2F71B79-6A44-634D-A0FB-83D0CA44306A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B3A61E2D-0DEE-614A-8278-F8F296D0F7C5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B428B460-52B3-A340-97C6-5ECDAB9FBA7C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B47534CB-6960-D948-A0C4-EE7A960A5DE9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B5FFFBF8-E941-D045-80B2-FB90F30060DF.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B6CD2B37-602D-7E4A-8292-1FB48630AEAF.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/B8859670-CE24-BA4A-B81D-EC32B8E5AA3E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/BA02867F-7684-0446-8FBF-4E76CF9E624B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/BA92DA92-B52C-744A-BDF2-57611477F8AE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/BB5E7117-2026-AD40-9382-D9548998FD0F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/BF1DE85E-E399-9844-BA4E-F7E504E640CE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C141640A-DD61-3E47-A8E6-8445D4D24D0B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C222A43B-26B8-1142-87D2-E8E20CFE0736.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C31B976B-9A31-E849-A786-135C090BD09B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C3396A04-E591-9B44-94BC-9734E5CF270C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C54D68FB-5DFB-C343-80F6-4DDC8C6757E2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C5A42361-278D-A140-AD79-8A31B63FA1A7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C5CE4540-1A71-894D-AE59-2009826E5F57.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C6C198D0-01AB-254A-B1C5-14CD9D71A6BD.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/C7444BA6-0AF7-1549-8E8D-AC508490D0C5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/CAE37F81-C638-B94D-9A7A-E31ADA879CAD.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/CFBC9555-6E24-2E4E-AA44-6DA7F48A36C9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/D030EABC-A2EA-754C-8F7B-D0BEA686B7BB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/D0992F71-82A5-AE44-B446-D53D72F65A19.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/D1EDE3E8-F899-584C-A883-32B369125AF5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/D66C6F9F-9AF9-D247-A223-6228D21FC0B2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/D776862B-A425-EB46-AEA1-0B73B3D7E5CB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/D8F618E0-12A5-F345-BE1C-B24EFF393A11.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/D8F66768-4467-444C-93D8-2960AE1AC719.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/DA522950-7EB3-F441-948D-EA2B8ABAE70E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/DA807873-B13E-C545-ADA7-984DDF659C53.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/DB7FDFD9-F13E-1B40-AAC9-F663157C426F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/DC157306-4B2E-4C46-82CE-F143E0D39215.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/DC3AACF5-E66F-D840-8F8E-790B480DD568.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/DDC1D3BB-6A94-4C4C-A3A7-866A5568BFD5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/DFF5413A-CFFC-C149-B41E-86FA4A29B6CC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E032A7AB-52A9-D34D-AFEB-74B11EE4096E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E0E038F7-5DD5-7748-BE31-18D70D1135BE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E1F1759A-E3A0-024F-8516-F2C6B5B8443C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E2B83C6D-0341-2144-87A0-DE58424C03C6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E2FC4721-F01A-0D48-A34B-C6E673714C0D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E3235F8E-9D33-014D-90A9-59785DB56A77.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E33F202C-A9F9-5440-949A-0B7557BF13F6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E542A6EA-E54F-0A4D-B173-40CA953A8506.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E5B1B0BD-8F34-2148-BCC3-4C9A4551D214.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/E88E82DA-5AD5-DD42-954E-AC591A054C5D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/EE4ACED7-9E14-3D46-8BDD-4E09FEA8D81D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F000FA9A-4542-5D4C-B8D5-294CA553F114.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F34D684D-E5C1-DD4E-85FC-614A7B29E6C6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F4062C15-2318-9B4B-9523-13B5A049CC68.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F4207760-5E70-7D46-9654-FDC47E61309E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F4A5B77E-FFA2-6F4B-B958-85B1D8B50F09.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F6A9266C-EFF6-F043-BFF0-F04312E821F3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/70000/F89EE5E6-A66A-2548-AA2A-979058CC4DE9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/017218A4-E0E1-8F4B-8146-823685546FC5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/04E8E96D-08DA-834E-902B-ACB4623CF044.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/069BBBA1-3EE4-0942-B4F2-A33229A56BBB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/09379AB7-0A0D-EE4F-8AB7-6798B3F4A698.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/0BC6CBA2-7913-C643-9C84-265173C3B1A9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/0C803B34-654F-F646-A9B7-E9CF14C8B981.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/0E6C3565-FDEF-C54C-8A63-C668DD4AF3F6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/13717F35-C560-DF45-9CCE-9B767B149F06.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/17806EE0-669E-774F-BCE3-C5E7BCE09CC1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/191BB3D9-395A-8647-AE1F-6587DDEA563E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/1A9FADC5-C704-BD4E-ACDE-45D58D9F9CE9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/1B7A94DC-AAF9-5E4D-B8C7-C09A706AD1B2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/1C80B878-3A7B-404C-9730-441AEAB4D943.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/1CFAC578-E9D4-5D42-9E89-04D758284132.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/26D6DC7C-72F1-4C42-9724-DD0884DC1D37.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/2E7F94C7-B959-D64A-B042-FD630F8264FE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/31643463-5478-A843-AD8D-C8A049A3912C.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/36F1283F-F7A4-6043-B6A7-1B8EFEC5300E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/36FE7724-444D-6043-89F0-923B63676394.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/37A76C90-5A69-F545-B10F-387C6CABCAA2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/38C0D702-659F-0840-B433-36EE5E1834F6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/39AAC2D2-3633-A04B-8B6B-B899D91C2539.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/3B0549BF-D549-234C-B645-7CC4BD953FAB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/3B92087A-4FD2-FE44-AA48-EA9BB552A8A5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/3C2FA5D1-49E9-2B40-92F1-C67C36695DD5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/3DCEE37B-29CB-3942-9C0D-C0850875BE02.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/3FAD44A3-96B6-924C-B9DD-C25ED7233448.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/3FB12362-2D46-054D-A3FC-CDBDC14249B9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/40C1EEDB-A3D7-DD45-8F34-8AC8272B5B88.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/410BDAA2-63C6-9E4B-B2FF-7982A70781E6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/438F80C9-86B5-0947-92D6-672620E75FC5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/452004E9-C7CD-CA44-AC65-D37B694583DA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/4649D564-9864-4E4B-93DE-0A6E78F6223D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/4B6F8EA7-3F2D-B944-BFB0-AF9C7EE25B16.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/4C86B029-4FBA-6947-AD35-E3C7974FF072.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/4E2D9F04-C121-144A-B7F5-43A06B31E2AB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/4FBF6EF2-6ADF-7745-BFB3-528382F694CB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/516EA075-C8D8-0247-8F08-67E1087F39B0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/52CC568E-F3A4-0441-BDED-3BE3B1E96F63.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/55D6BD40-051F-AA49-A813-B9B9E8FB2168.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/5D502960-55B9-1744-A06E-CAA2A7346BC2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/5D5C4FD7-EBC4-0442-A698-86F3CA131D37.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/60A405BE-BA4C-3C42-A0D9-CFF4E36A195E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/61089308-6438-9D46-B0E9-A19739CA6E75.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/62EF2790-98EE-6F44-B1F1-BAA9CE64624E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/63771592-76FA-E447-B93C-5723450782B7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/64A8D6DE-4BD9-A744-8201-2DA84403E7D2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/64F26F29-BBDC-494B-A874-842026F4B80F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/660E6C6B-B813-EF40-91AB-1DA4728935BC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/67F6F777-C665-BF4F-A478-2E51053E7992.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/690DF8CA-20BD-EA44-BAB7-4FD913716A2D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/6A5DBA00-7336-684B-9F61-35B7B4AF108D.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/6AD7691F-13A0-A44C-ACD4-108E8369D0BA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/6B5E9C39-1EB6-F347-8178-E525A60401F2.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/6BEFBE8F-7FF6-A24F-AA01-30BFD1651828.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/6C9AE5F2-525A-AE4B-84FD-66F8F46D7CA7.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/6CDD560D-3DED-3D46-829D-6944397F879F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/6D4DF5D2-A6C9-AB46-8161-4C0FFA43F372.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/6E19E642-BA58-D54C-B1C9-A056BA135AC8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/722AD197-0A24-264E-BEAC-AF893CC8072E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/755CBD6E-7DAF-5D4C-A7B9-BD45AA04FD33.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/757254A0-55FD-1542-BCD1-B3F82B6776DB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/76126798-3F77-B54B-8FAC-E24F13D8CC68.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/763A53AF-D344-EB43-AE7F-B074742EE8D0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/76521791-AECD-0E4A-A1F4-1A9E10BD2071.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/7680C4AA-4497-FB43-AD01-A6CE0ABDF7A0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/791E58F4-F781-A84F-84D3-7E4985A8626B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/7957713E-5EB6-5747-9EEC-EB95F6C7EF97.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/7FA13C28-1C22-1C43-BF9A-BDD6FC2958B0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/806D6479-D047-F147-A08D-8AB9902AF641.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/8221F858-4B8C-D34D-A8F3-598FE3C379D8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/85771CC2-4ECB-624B-A4F9-BB48440768EC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/878D3CE9-C7D7-F545-B4A2-67EFC4EB960F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/8B69606D-6A73-EE4B-B6E0-1C0072BE214A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/8C7B66A3-CD20-564B-BAB1-FACBDFEE7A53.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/8D0DD04E-DEDE-0B4C-9211-8D9A9A614E41.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/8DA1B2F7-9D52-0845-8AA0-9B57BB5AD95A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/91A40781-FEC1-4C4E-A4EE-5B27FB237F02.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/92258BC3-5F8D-A44F-84C1-324EF32ADCF3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/935A6BE1-E7C9-384E-815A-328437EFAF32.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/939AEDBE-B10F-8D44-89F3-312EF9C10C82.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/94E3D3A2-E3E7-5646-AFA7-01AA14669241.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/9CD41A96-2710-6D42-B599-F898C1C37983.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/9D441B13-4D63-BD4D-9E8E-CE852A8CF679.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/A0E82004-23D7-B145-84CB-D7C218ADA399.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/A162FC83-2044-2443-857F-DCB5E22A488B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/A3B82016-1249-8249-8969-B086948512C8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/A4EA7525-D7CD-B349-8243-D7B10527F39B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/A5522DF1-B946-4F41-80E8-E0C57A8B7DE0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/A631EA4D-DF91-E74F-BF34-E913367289B6.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/A9976102-37BF-2F48-888F-38D894A878E4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/AAD9620D-F825-AE41-9370-B62BB3DEE2F3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/AC95232D-A9B8-D244-B046-D9915E8A7E6F.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/AE727B93-C777-D545-891E-98F4157B5233.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/AF6D2D21-CE5F-F447-9708-D5757F3694E5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/AFBD1030-D8DD-1348-9166-38C672416520.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/B046C4A6-186F-5B48-9D9B-E84D69EF001B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/B354A81B-B66C-4B48-AAE7-188BA057E4B9.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/B838BE4F-CA08-DE4B-9D51-D69C4F3035EC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/BCE5CDAF-1F1F-0E41-A5DB-1CC1F9EDBAE5.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/BD847071-FFB4-3447-B9D4-9353B954D52E.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/BD95D9E3-8E5F-3446-AC74-1A68E81A0F59.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/BF922FEF-0836-6547-821F-423521665F85.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/C71B3D80-5481-984C-8F32-CF9D7A74E587.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/CC369850-7022-014A-BCBE-931001075CA4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/CC36F9CE-5A5A-4E49-BAE0-B77593773574.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/CEBB7ADD-6F45-E14C-8CA7-98AA9291E254.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/CF9CB30E-2126-DD4C-8F4B-7680A9BB4C87.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/D3A569E3-70BA-2042-A389-42CB44DC2091.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/DBC481D0-DF85-7441-8B93-2BBC09F28733.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/DD2C935D-769E-694A-A376-AD2B376378FC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/DEB80E72-7AB4-1A4A-84B3-55100B7ECC74.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/DF6DEC8F-D3A8-1F4C-B7F8-57553F9454E0.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/E075EF9B-8D19-F04A-BE5D-4EFF3B8A2CD1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/E10BE4D9-02C4-094E-B3AD-9FB1927E5B5A.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/E2A34A4F-59EC-FC4E-B9E7-BD5676F97DAE.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/E2A6F1D8-51FF-2749-9F2F-25BE1078CEE1.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/E5388903-59BD-8942-984F-D736A8154050.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/E7B8926F-E808-6943-9F3A-358A94E9D1A8.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/E7CF81BF-D205-5D47-8572-337A74015971.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/E8C5FEF5-2BCC-E745-B8C4-9132FC6ADD30.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/EA69C1F5-D2A2-644C-AADA-14B90622BB11.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/EB6B879C-5CEC-EC48-9117-5B4A22720674.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/EC73FF73-35D8-7F43-B31C-A3D21801A434.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/F03065F2-BBF3-104C-A1FC-486B6795502B.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/F0B13CDF-4E2A-4D47-8996-8754F743FCFB.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/F459529C-7FC6-9E4D-AF5F-91CDCA505AED.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/F65FB165-8678-8E48-9856-4A48E07475E3.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/F80D5896-681E-474B-AC7E-68A746C5C3AC.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/FAFF65DE-EC88-5B4C-95E3-F5A6501E55B4.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/FB0148AB-7CCE-1144-A209-B3B18135BBCA.root', 
        '/store/mc/RunIISummer20UL16RECO/GluGluHToBB_M-125_TuneCP5_MINLO_NNLOPS_13TeV-powheg-pythia8/AODSIM/106X_mcRun2_asymptotic_v13-v2/80000/FE4C1FF7-FE29-934B-BC00-97A0EB956C3C.root'
     ) ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--eventcontent nevts:965'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('MINIAODSIM'),
        filterName = cms.untracked.string('')
    ),
    dropMetaData = cms.untracked.string('ALL'),
    eventAutoFlushCompressedSize = cms.untracked.int32(-900),
    fastCloning = cms.untracked.bool(False),
    fileName = cms.untracked.string('file:HIG-RunIISummer20UL16MiniAODv2-12236.root'),
    outputCommands = process.MINIAODSIMEventContent.outputCommands,
    overrideBranchesSplitLevel = cms.untracked.VPSet(
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedCandidates_packedPFCandidates__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenParticles_prunedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patTriggerObjectStandAlones_slimmedPatTrigger__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patPackedGenParticles_packedGenParticles__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoVertexs_offlineSlimmedPrimaryVertices__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoCaloClusters_reducedEgamma_reducedESClusters_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEBRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedEERecHits_*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('recoGenJets_slimmedGenJets__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('patJets_slimmedJetsPuppi__*'),
            splitLevel = cms.untracked.int32(99)
        ), 
        cms.untracked.PSet(
            branch = cms.untracked.string('EcalRecHitsSorted_reducedEgamma_reducedESRecHits_*'),
            splitLevel = cms.untracked.int32(99)
        )
    ),
    overrideInputFileSplitLevels = cms.untracked.bool(True),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun2_asymptotic_v17', '')

# Path and EndPath definitions
process.Flag_trackingFailureFilter = cms.Path(process.goodVertices+process.trackingFailureFilter)
process.Flag_goodVertices = cms.Path(process.primaryVertexFilter)
process.Flag_CSCTightHaloFilter = cms.Path(process.CSCTightHaloFilter)
process.Flag_trkPOGFilters = cms.Path(process.trkPOGFilters)
process.Flag_HcalStripHaloFilter = cms.Path(process.HcalStripHaloFilter)
process.Flag_trkPOG_logErrorTooManyClusters = cms.Path(~process.logErrorTooManyClusters)
process.Flag_hfNoisyHitsFilter = cms.Path(process.hfNoisyHitsFilter)
process.Flag_EcalDeadCellTriggerPrimitiveFilter = cms.Path(process.EcalDeadCellTriggerPrimitiveFilter)
process.Flag_ecalLaserCorrFilter = cms.Path(process.ecalLaserCorrFilter)
process.Flag_globalSuperTightHalo2016Filter = cms.Path(process.globalSuperTightHalo2016Filter)
process.Flag_eeBadScFilter = cms.Path(process.eeBadScFilter)
process.Flag_METFilters = cms.Path(process.metFilters)
process.Flag_chargedHadronTrackResolutionFilter = cms.Path(process.chargedHadronTrackResolutionFilter)
process.Flag_globalTightHalo2016Filter = cms.Path(process.globalTightHalo2016Filter)
process.Flag_CSCTightHaloTrkMuUnvetoFilter = cms.Path(process.CSCTightHaloTrkMuUnvetoFilter)
process.Flag_HBHENoiseIsoFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseIsoFilter)
process.Flag_BadChargedCandidateSummer16Filter = cms.Path(process.BadChargedCandidateSummer16Filter)
process.Flag_hcalLaserEventFilter = cms.Path(process.hcalLaserEventFilter)
process.Flag_BadPFMuonFilter = cms.Path(process.BadPFMuonFilter)
process.Flag_ecalBadCalibFilter = cms.Path(process.ecalBadCalibFilter)
process.Flag_HBHENoiseFilter = cms.Path(process.HBHENoiseFilterResultProducer+process.HBHENoiseFilter)
process.Flag_trkPOG_toomanystripclus53X = cms.Path(~process.toomanystripclus53X)
process.Flag_EcalDeadCellBoundaryEnergyFilter = cms.Path(process.EcalDeadCellBoundaryEnergyFilter)
process.Flag_BadChargedCandidateFilter = cms.Path(process.BadChargedCandidateFilter)
process.Flag_trkPOG_manystripclus53X = cms.Path(~process.manystripclus53X)
process.Flag_BadPFMuonSummer16Filter = cms.Path(process.BadPFMuonSummer16Filter)
process.Flag_muonBadTrackFilter = cms.Path(process.muonBadTrackFilter)
process.Flag_CSCTightHalo2015Filter = cms.Path(process.CSCTightHalo2015Filter)
process.Flag_BadPFMuonDzFilter = cms.Path(process.BadPFMuonDzFilter)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.MINIAODSIMoutput_step = cms.EndPath(process.MINIAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.Flag_HBHENoiseFilter,process.Flag_HBHENoiseIsoFilter,process.Flag_CSCTightHaloFilter,process.Flag_CSCTightHaloTrkMuUnvetoFilter,process.Flag_CSCTightHalo2015Filter,process.Flag_globalTightHalo2016Filter,process.Flag_globalSuperTightHalo2016Filter,process.Flag_HcalStripHaloFilter,process.Flag_hcalLaserEventFilter,process.Flag_EcalDeadCellTriggerPrimitiveFilter,process.Flag_EcalDeadCellBoundaryEnergyFilter,process.Flag_ecalBadCalibFilter,process.Flag_goodVertices,process.Flag_eeBadScFilter,process.Flag_ecalLaserCorrFilter,process.Flag_trkPOGFilters,process.Flag_chargedHadronTrackResolutionFilter,process.Flag_muonBadTrackFilter,process.Flag_BadChargedCandidateFilter,process.Flag_BadPFMuonFilter,process.Flag_BadPFMuonDzFilter,process.Flag_hfNoisyHitsFilter,process.Flag_BadChargedCandidateSummer16Filter,process.Flag_BadPFMuonSummer16Filter,process.Flag_trkPOG_manystripclus53X,process.Flag_trkPOG_toomanystripclus53X,process.Flag_trkPOG_logErrorTooManyClusters,process.Flag_METFilters,process.endjob_step,process.MINIAODSIMoutput_step)
process.schedule.associate(process.patTask)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.PatAlgos.slimming.miniAOD_tools
from PhysicsTools.PatAlgos.slimming.miniAOD_tools import miniAOD_customizeAllMC 

#call to customisation function miniAOD_customizeAllMC imported from PhysicsTools.PatAlgos.slimming.miniAOD_tools
process = miniAOD_customizeAllMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
