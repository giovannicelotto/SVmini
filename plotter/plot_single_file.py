# %%
import uproot
import matplotlib.pyplot as plt
import mplhep as hep
hep.style.use("CMS")
from plot_efficiency_vs_variable import efficiencyVsVariable
import numpy  as np
import awkward as ak
# %%
fileName = "/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/central.root"
f = uproot.open(fileName)
tree = f["Events"]
branches = tree.arrays()
# %%
GV_isB = branches["GV_isB"]
GV_isD = branches["GV_isD"]
GV_Hadron_SVIdx = branches["GV_Hadron_SVIdx"]
GV_Hadron_pdgId = branches["GV_Hadron_pdgId"]

# %%
def map_to_groups(value):
    if abs(value) in [411, 421, 431]:
        # Bmesons
        return 0
    elif abs(value) in [511, 521, 531, 541]:
        # Dmesons
        return 1
    elif ((abs(value) > 3000) & (abs(value) < 4000)):
        # S baryon
        return 5
    elif ((abs(value) > 4000) & (abs(value) < 5000)):
        return 2
    elif ((abs(value) > 5000) & (abs(value) < 6000)):
        return 3
    elif (abs(value) == 15):
        return 4
    # Add more conditions as needed
    else:
        return -1  # or any default value for unmatched cases
map_to_groups_vec = np.vectorize(map_to_groups)
mesons = map_to_groups_vec(ak.flatten(GV_Hadron_pdgId))

efficiencyVsVariable(num=mesons[(ak.flatten(GV_Hadron_SVIdx)>-1)], den=mesons,
                    bins=np.linspace(-0.5, 4.5, 6), xlabel="Hadron Flavor",
                    outName="/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/plots/efficiency/eff_pdgDiff.png", title = "All particles",
                    #tick_positions = [0, 1, 2, 3, 4, 5],
                    #tick_labels = ['D mesons', 'B mesons', 'Strange Baryons', 'Charmed Baryons', 'Bottom Baryons', 'Tau'],)
                    tick_positions = [0, 1, 2, 3, 4],
                    tick_labels = ['D mesons', 'B mesons',  'Charmed Baryons', 'Bottom Baryons', 'Tau'],)
                    
# %%

efficiencyVsVariable(num=ak.flatten(ak.run_lengths(branches["GVDaughters_hadronIndex"])[(GV_Hadron_SVIdx>-1)]), den=ak.flatten(ak.run_lengths(branches["GVDaughters_hadronIndex"])),
                    bins=np.arange(0, 10), xlabel="Number of hadron daughters",
                    outName="/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/plots/efficiency/eff_nGenTracksDiff.png", title = "All particles",)

efficiencyVsVariable(num=ak.flatten(branches["GV_pt"][(GV_Hadron_SVIdx>-1)]), den=ak.flatten(branches["GV_pt"][(GV_Hadron_SVIdx>-2)]),
                    bins=np.linspace(10, 20, 31), xlabel="p$_T$ [GeV]",
                    outName="/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/plots/efficiency/eff_pT.png", title = "All particles",)
# %%
