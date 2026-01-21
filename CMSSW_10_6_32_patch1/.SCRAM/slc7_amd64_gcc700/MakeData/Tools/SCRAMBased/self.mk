ifeq ($(strip $(FWCore/Version)),)
FWCoreVersion := self/FWCore/Version
FWCore/Version := FWCoreVersion
FWCoreVersion_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
FWCoreVersion_EX_USE := $(foreach d, self cmssw ,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
FWCoreVersion_EX_LIB   := FWCoreVersion
ALL_EXTERNAL_PRODS += FWCoreVersion
FWCoreVersion_CLASS := LIBRARY
FWCore/Version_relbigobj+=FWCoreVersion
endif
ifeq ($(strip $(GeneratorInterfaceCore_plugins)),)
GeneratorInterfaceCore_plugins := self/src/GeneratorInterface/Core/plugins
GeneratorInterfaceCore_plugins_LOC_USE := self cmssw FWCore/Framework FWCore/ParameterSet FWCore/MessageLogger FWCore/Utilities SimDataFormats/GeneratorProducts GeneratorInterface/Core FWCore/SharedMemory
ALL_EXTERNAL_PLUGIN_PRODS += GeneratorInterfaceCore_plugins
GeneratorInterface/Core_relbigobj+=GeneratorInterfaceCore_plugins
endif
ifeq ($(strip $(GeneratorInterface/Core)),)
GeneratorInterfaceCore := self/GeneratorInterface/Core
GeneratorInterface/Core := GeneratorInterfaceCore
GeneratorInterfaceCore_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
GeneratorInterfaceCore_EX_USE := $(foreach d, self cmssw FWCore/Concurrency FWCore/ServiceRegistry FWCore/Utilities FWCore/Framework SimDataFormats/GeneratorProducts GeneratorInterface/LHEInterface heppdt boost clhep lhapdf f77compiler root,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
GeneratorInterfaceCore_EX_LIB   := GeneratorInterfaceCore
ALL_EXTERNAL_PRODS += GeneratorInterfaceCore
GeneratorInterfaceCore_CLASS := LIBRARY
GeneratorInterface/Core_relbigobj+=GeneratorInterfaceCore
endif
ifeq ($(strip $(GeneratorInterfaceGenFiltersPlugins)),)
GeneratorInterfaceGenFiltersPlugins := self/src/GeneratorInterface/GenFilters/plugins
GeneratorInterfaceGenFiltersPlugins_LOC_USE := self cmssw FWCore/ParameterSet FWCore/Framework FWCore/Utilities SimDataFormats/GeneratorProducts DataFormats/HepMCCandidate DataFormats/JetReco
ALL_EXTERNAL_PLUGIN_PRODS += GeneratorInterfaceGenFiltersPlugins
GeneratorInterface/GenFilters_relbigobj+=GeneratorInterfaceGenFiltersPlugins
endif
ifeq ($(strip $(GeneratorInterface/GenFilters)),)
GeneratorInterfaceGenFilters := self/GeneratorInterface/GenFilters
GeneratorInterface/GenFilters := GeneratorInterfaceGenFilters
GeneratorInterfaceGenFilters_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
GeneratorInterfaceGenFilters_EX_USE := $(foreach d, self cmssw fastjet boost FWCore/PluginManager FWCore/ParameterSet FWCore/Framework FWCore/Utilities SimDataFormats/GeneratorProducts heppdt clhep root GeneratorInterface/Pythia6Interface GeneratorInterface/Core pythia8 SimGeneral/HepPDTRecord DataFormats/GeometryVector DataFormats/GeometrySurface TrackPropagation/SteppingHelixPropagator MagneticField/Records TrackingTools/TrajectoryState TrackingTools/TrajectoryParametrization TrackingTools/Records CommonTools/UtilAlgos FWCore/ServiceRegistry CommonTools/BaseParticlePropagator TrackingTools/GeomPropagators DataFormats/HepMCCandidate DataFormats/JetReco DataFormats/EgammaReco DataFormats/Math,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
ALL_EXTERNAL_PRODS += GeneratorInterfaceGenFilters
GeneratorInterfaceGenFilters_CLASS := LIBRARY
GeneratorInterface/GenFilters_relbigobj+=GeneratorInterfaceGenFilters
endif
ifeq ($(strip $(PhysicsTools/NanoAOD)),)
src_PhysicsTools_NanoAOD := self/PhysicsTools/NanoAOD
PhysicsTools/NanoAOD  := src_PhysicsTools_NanoAOD
src_PhysicsTools_NanoAOD_BuildFile    := $(RELEASETOP)/.SCRAM/$(SCRAM_ARCH)/MakeData/DirCache.mk
src_PhysicsTools_NanoAOD_EX_USE := $(foreach d, DataFormats/NanoAOD boost DataFormats/Common self cmssw DataFormats/Candidate fastjet-contrib fastjet DataFormats/StdDictionaries FWCore/Common FWCore/Utilities,$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
ALL_EXTERNAL_PRODS += src_PhysicsTools_NanoAOD
endif

ifeq ($(strip $(PhysicsToolsNanoAODPlugins)),)
PhysicsToolsNanoAODPlugins := self/src/PhysicsTools/NanoAOD/plugins
PhysicsToolsNanoAODPlugins_LOC_USE := self cmssw PhysicsTools/TensorFlow FWCore/Framework FWCore/ParameterSet FWCore/ServiceRegistry FWCore/Utilities DataFormats/Candidate DataFormats/PatCandidates CommonTools/MVAUtils RecoEgamma/EgammaTools PhysicsTools/JetMCUtils DataFormats/NanoAOD roothistmatrix RecoVertex/VertexTools RecoVertex/VertexPrimitives DataFormats/L1TGlobal IOPool/Provenance DQMServices/Core CondFormats/BTauObjects CondTools/BTau DataFormats/CTPPSDetId DataFormats/CTPPSReco DataFormats/ProtonReco CondFormats/RunInfo CondFormats/DataRecord fastjet fastjet-contrib
ALL_EXTERNAL_PLUGIN_PRODS += PhysicsToolsNanoAODPlugins
PhysicsTools/NanoAOD_relbigobj+=PhysicsToolsNanoAODPlugins
endif
