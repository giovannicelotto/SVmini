# %%
import uproot
import matplotlib.pyplot as plt
import mplhep as hep
hep.style.use("CMS")
import numpy as np
import awkward as ak
from plot_efficiency_vs_variable import efficiencyVsVariable, efficiencyVsVariable_collections

# %%

# List of files and labels
fileNames = [
    ("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_minHits8_0p0.root", "NNcut0_8Hits"),
    ("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_0p001.root", "NNcut1e-3_8Hits"),
    #("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_minHits4.root", "NNcut0p0_4Hits"),
    ("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_minHits4_0p0001.root", "NNcut1e-4_4Hits"),

    ("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_minHits4_0p00005.root", "NNcut5e-5_4Hits"),
    ("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_minHits4_0p00001.root", "NNcut1e-6_4Hits"),
    
    
    #("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_minHits4_0p0001.root", "minHits4_0p0001"),
    #("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_0p01.root", "NNcut0p01"),
    #("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_0p001.root", "NNcut0p001"),
    #("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_0p0005.root", "NNcut0p0005"),
    #("/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_0p0001.root", "NNcut0p0001"),
]

# Dictionaries to store branches and computed values
branches = {}
matched = {}
totSV = {}
totGV = {}
eff_values = {}
fr_values = {}

# Load all files and store branches
for fname, label in fileNames:
    f = uproot.open(fname)
    tree = f["Events"]
    branches[label] = tree.arrays()

# Convenience function
def get_efficiency_fakerate(GV_Hadron_SV_Idx, nSV, GVtrack_Hadron_pdgId, pdgs=None):
    if pdgs is not None:
        pdgs_dict = {
            "b": [521,511,531,541,5122,5132,5232,5332,5142,5242,5342,5512,5532,5542,5554],
            "d": [411,421,431,4122,4232,4132,4332,4412,4422,4432,4444],
            "s": [3122,3222,3212,3312,3322,3334],
            "tau": [15]
        }
        flat = ak.flatten(GVtrack_Hadron_pdgId)
        mask = ak.any(flat[..., None] == pdgs_dict[pdgs], axis=-1)
        counts = ak.num(GVtrack_Hadron_pdgId)
        GV_Hadron_SV_Idx = GV_Hadron_SV_Idx[ak.unflatten(mask, counts)]
    n_tot = ak.sum(GV_Hadron_SV_Idx > -2)
    eff = ak.sum(GV_Hadron_SV_Idx > -1) / n_tot
    err_eff = np.sqrt(eff * (1 - eff) / n_tot)
    fr = 1 - ak.sum(GV_Hadron_SV_Idx > -1) / ak.sum(nSV)
    err_fr = np.sqrt(fr * (1 - fr) / n_tot)
    return eff, err_eff, fr, err_fr

# Compute matched, totals, efficiency, fake rate
rows = []
for label in [l for _, l in fileNames]:
    b = branches[label]
    GV_idx = b["GV_Hadron_SVIdx"]
    nSV = b["nmySV"]
    nGV = b["nGV"]
    GV_pdg = b["GV_Hadron_pdgId"]
    GV_pdg = b["GV_Hadron_pdgId"]

    matched[label] = ak.sum(GV_idx > -1)
    totSV[label] = ak.sum(nSV)
    totGV[label] = ak.sum(nGV)

    eff, err_eff, fr, err_fr = get_efficiency_fakerate(GV_idx, nSV, GV_pdg)
    rows.append((label, matched[label], totSV[label], totGV[label], eff, err_eff, fr, err_fr))

# %%

# Print summary
print("\nSV Matching Summary")
print("-" * 103)
print(f"{'Collection':<12}     {'Matched SV':>12}     {'Total SV':>12}       {'Total GV':>12}     {'Efficiency [%]':>15}     {'Fake Rate [%]':>12}")
print("-" * 103)
for name, matched_val, totalSV_val, totalGV_val, eff_val, err_eff_val, fr_val, err_fr_val in rows:
    print(f"{name:<12}     {matched_val:>12.0f}     {totalSV_val:>12.0f}     {totalGV_val:>12.0f}     {eff_val*100:8.2f}+-{err_eff_val*100:>.5f}      {fr_val*100:>8.2f}+-{err_fr_val*100:>.5f}")
print("-" * 103)

# %%

# Efficiency vs Fake Rate plot
fig, ax = plt.subplots(1, 1)
for name, _, _, _, eff_val, err_eff_val, fr_val, err_fr_val in rows:
    ax.errorbar(eff_val, fr_val, xerr=err_eff_val, yerr=err_fr_val, marker='o', linestyle='none', label=name)

ax.errorbar(x=0.494, y=0.539, xerr=0.003, yerr=0.003, label="Central IVF", marker="o")
ax.legend()
ax.set_xlim(0.45, 0.58)
ax.set_ylim(0.45, 0.58)
ax.plot([0,1], [0,1], ls="--", c=".3")
ax.set_xlabel("Efficiency")
ax.set_ylabel("Fake Rate")

    # %%

# Efficiency - Fake Rate vs minHits
fig, ax = plt.subplots(1, 1)
for name, _, _, _, eff_val, _, fr_val, _ in rows:
    minHits = int(name.replace("minHits", ""))
    ax.errorbar(minHits, eff_val - fr_val, marker='o', linestyle='none', label=name)
ax.legend()
ax.set_ylabel("Efficiency - Fake Rate")
ax.set_xlabel("Min Hits")
# %%
