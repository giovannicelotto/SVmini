ifeq ($(strip $(PyPhysicsToolsPatAlgos)),)
PyPhysicsToolsPatAlgos := self/src/PhysicsTools/PatAlgos/python
src_PhysicsTools_PatAlgos_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/PhysicsTools/PatAlgos/python)
PyPhysicsToolsPatAlgos_files := $(patsubst src/PhysicsTools/PatAlgos/python/%,%,$(wildcard $(foreach dir,src/PhysicsTools/PatAlgos/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyPhysicsToolsPatAlgos_LOC_USE := self cmssw 
PyPhysicsToolsPatAlgos_PACKAGE := self/src/PhysicsTools/PatAlgos/python
ALL_PRODS += PyPhysicsToolsPatAlgos
PyPhysicsToolsPatAlgos_INIT_FUNC        += $$(eval $$(call PythonProduct,PyPhysicsToolsPatAlgos,src/PhysicsTools/PatAlgos/python,src_PhysicsTools_PatAlgos_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyPhysicsToolsPatAlgos,src/PhysicsTools/PatAlgos/python))
endif
ALL_COMMONRULES += src_PhysicsTools_PatAlgos_python
src_PhysicsTools_PatAlgos_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_PhysicsTools_PatAlgos_python,src/PhysicsTools/PatAlgos/python,PYTHON))
src_PhysicsTools_PatAlgos_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/PhysicsTools/PatAlgos/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_PhysicsTools_PatAlgos_scripts,src/PhysicsTools/PatAlgos/scripts,$(SCRAMSTORENAME_BIN),*))
ALL_PACKAGES += PhysicsTools/PatAlgos
subdirs_src_PhysicsTools_PatAlgos := src_PhysicsTools_PatAlgos_plugins src_PhysicsTools_PatAlgos_python src_PhysicsTools_PatAlgos_scripts src_PhysicsTools_PatAlgos_interface src_PhysicsTools_PatAlgos_src src_PhysicsTools_PatAlgos_test
ALL_SUBSYSTEMS+=PhysicsTools
subdirs_src_PhysicsTools = src_PhysicsTools_data src_PhysicsTools_PatAlgos src_PhysicsTools_SimpleVertexTable
ifeq ($(strip $(PyPhysicsToolsSimpleVertexTable)),)
PyPhysicsToolsSimpleVertexTable := self/src/PhysicsTools/SimpleVertexTable/python
src_PhysicsTools_SimpleVertexTable_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/PhysicsTools/SimpleVertexTable/python)
PyPhysicsToolsSimpleVertexTable_files := $(patsubst src/PhysicsTools/SimpleVertexTable/python/%,%,$(wildcard $(foreach dir,src/PhysicsTools/SimpleVertexTable/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyPhysicsToolsSimpleVertexTable_LOC_USE := self cmssw 
PyPhysicsToolsSimpleVertexTable_PACKAGE := self/src/PhysicsTools/SimpleVertexTable/python
ALL_PRODS += PyPhysicsToolsSimpleVertexTable
PyPhysicsToolsSimpleVertexTable_INIT_FUNC        += $$(eval $$(call PythonProduct,PyPhysicsToolsSimpleVertexTable,src/PhysicsTools/SimpleVertexTable/python,src_PhysicsTools_SimpleVertexTable_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyPhysicsToolsSimpleVertexTable,src/PhysicsTools/SimpleVertexTable/python))
endif
ALL_COMMONRULES += src_PhysicsTools_SimpleVertexTable_python
src_PhysicsTools_SimpleVertexTable_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_PhysicsTools_SimpleVertexTable_python,src/PhysicsTools/SimpleVertexTable/python,PYTHON))
ifeq ($(strip $(runtestPhysicsToolsPatAlgos)),)
runtestPhysicsToolsPatAlgos := self/src/PhysicsTools/PatAlgos/test
runtestPhysicsToolsPatAlgos_files := $(patsubst src/PhysicsTools/PatAlgos/test/%,%,$(foreach file,runtestPhysicsToolsPatAlgos.cpp,$(eval xfile:=$(wildcard src/PhysicsTools/PatAlgos/test/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/PhysicsTools/PatAlgos/test/$(file). Please fix src/PhysicsTools/PatAlgos/test/BuildFile.))))
runtestPhysicsToolsPatAlgos_TEST_RUNNER_CMD :=  runtestPhysicsToolsPatAlgos  /bin/bash PhysicsTools/PatAlgos/test runtests.sh
runtestPhysicsToolsPatAlgos_BuildFile    := $(WORKINGDIR)/cache/bf/src/PhysicsTools/PatAlgos/test/BuildFile
runtestPhysicsToolsPatAlgos_LOC_USE := self cmssw FWCore/Utilities
runtestPhysicsToolsPatAlgos_PACKAGE := self/src/PhysicsTools/PatAlgos/test
ALL_PRODS += runtestPhysicsToolsPatAlgos
runtestPhysicsToolsPatAlgos_INIT_FUNC        += $$(eval $$(call Binary,runtestPhysicsToolsPatAlgos,src/PhysicsTools/PatAlgos/test,src_PhysicsTools_PatAlgos_test,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_TEST),test,$(SCRAMSTORENAME_LOGS)))
runtestPhysicsToolsPatAlgos_CLASS := TEST
else
$(eval $(call MultipleWarningMsg,runtestPhysicsToolsPatAlgos,src/PhysicsTools/PatAlgos/test))
endif
ifeq ($(strip $(PhysicsToolsPatAlgos_testAnalyzers)),)
PhysicsToolsPatAlgos_testAnalyzers := self/src/PhysicsTools/PatAlgos/test
PhysicsToolsPatAlgos_testAnalyzers_files := $(patsubst src/PhysicsTools/PatAlgos/test/%,%,$(foreach file,private/*.cc,$(eval xfile:=$(wildcard src/PhysicsTools/PatAlgos/test/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/PhysicsTools/PatAlgos/test/$(file). Please fix src/PhysicsTools/PatAlgos/test/BuildFile.))))
PhysicsToolsPatAlgos_testAnalyzers_BuildFile    := $(WORKINGDIR)/cache/bf/src/PhysicsTools/PatAlgos/test/BuildFile
PhysicsToolsPatAlgos_testAnalyzers_LOC_USE := self cmssw FWCore/Framework FWCore/ParameterSet DataFormats/BTauReco PhysicsTools/PatUtils DataFormats/PatCandidates root
PhysicsToolsPatAlgos_testAnalyzers_PRE_INIT_FUNC += $$(eval $$(call edmPlugin,PhysicsToolsPatAlgos_testAnalyzers,PhysicsToolsPatAlgos_testAnalyzers,$(SCRAMSTORENAME_LIB),src/PhysicsTools/PatAlgos/test))
PhysicsToolsPatAlgos_testAnalyzers_PACKAGE := self/src/PhysicsTools/PatAlgos/test
ALL_PRODS += PhysicsToolsPatAlgos_testAnalyzers
PhysicsToolsPatAlgos_testAnalyzers_INIT_FUNC        += $$(eval $$(call Library,PhysicsToolsPatAlgos_testAnalyzers,src/PhysicsTools/PatAlgos/test,src_PhysicsTools_PatAlgos_test,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS),edm))
PhysicsToolsPatAlgos_testAnalyzers_CLASS := TEST_LIBRARY
else
$(eval $(call MultipleWarningMsg,PhysicsToolsPatAlgos_testAnalyzers,src/PhysicsTools/PatAlgos/test))
endif
ALL_COMMONRULES += src_PhysicsTools_PatAlgos_test
src_PhysicsTools_PatAlgos_test_parent := PhysicsTools/PatAlgos
src_PhysicsTools_PatAlgos_test_INIT_FUNC += $$(eval $$(call CommonProductRules,src_PhysicsTools_PatAlgos_test,src/PhysicsTools/PatAlgos/test,TEST))
ALL_PACKAGES += plots/eventDisplay
subdirs_src_plots_eventDisplay := 
ALL_PACKAGES += plots/efficiency
subdirs_src_plots_efficiency := 
ALL_PACKAGES += PhysicsTools/SimpleVertexTable
subdirs_src_PhysicsTools_SimpleVertexTable := src_PhysicsTools_SimpleVertexTable_python src_PhysicsTools_SimpleVertexTable_plugins
ALL_PACKAGES += PhysicsTools/data
subdirs_src_PhysicsTools_data := 
ALL_SUBSYSTEMS+=plots
subdirs_src_plots = src_plots_efficiency src_plots_nSV_custom_vs_central src_plots_eventDisplay
ALL_PACKAGES += plots/nSV_custom_vs_central
subdirs_src_plots_nSV_custom_vs_central := 
ALL_SUBSYSTEMS+=config_cmssw
subdirs_src_config_cmssw = 
