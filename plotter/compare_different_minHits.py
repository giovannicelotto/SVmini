# %%
import uproot
import matplotlib.pyplot as plt
import mplhep as hep
hep.style.use("CMS")
from plot_efficiency_vs_variable import efficiencyVsVariable
import numpy  as np
import awkward as ak
from plot_efficiency_vs_variable import efficiencyVsVariable_collections
# %%

fileName_minHits2 = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/track_tt_2_minHits2.root"
f_minHits2 = uproot.open(fileName_minHits2)
tree_minHits2 = f_minHits2["Events"]
branches_minHits2 = tree_minHits2.arrays()

fileName_minHits4 = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/track_tt_2_minHits4.root"
f_minHits4 = uproot.open(fileName_minHits4)
tree_minHits4 = f_minHits4["Events"]
branches_minHits4 = tree_minHits4.arrays()

fileName_minHits6 = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/track_tt_2_minHits6.root"
f_minHits6 = uproot.open(fileName_minHits6)
tree_minHits6 = f_minHits6["Events"]
branches_minHits6 = tree_minHits6.arrays()

fileName_minHits10 = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/track_tt_2_minHits10.root"
f_minHits10 = uproot.open(fileName_minHits10)
tree_minHits10 = f_minHits10["Events"]
branches_minHits10 = tree_minHits10.arrays()

fileName_minHits8 = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/track_tt_2.root"
f_minHits8 = uproot.open(fileName_minHits8)
tree_minHits8 = f_minHits8["Events"]
branches_minHits8 = tree_minHits8.arrays()




# Efficiency calculations
nGV_minHits6 = branches_minHits6["nGV"]
nmySV_minHits6 = branches_minHits6["nmySV"]
mySV_minHits6_x = branches_minHits6["mySV_x"]
mySV_minHits6_y = branches_minHits6["mySV_y"]
mySV_minHits6_z = branches_minHits6["mySV_z"]
GV_Hadron_SV_minHits6Idx = branches_minHits6["GV_Hadron_SVIdx"]
nmyGV_minHits6 = branches_minHits6["nGV"]
GVtrack_minHits6_Hadron_pdgId = branches_minHits6["GV_Hadron_pdgId"]
mySVtrks_minHits6_trk_pt = branches_minHits6["mySVtrks_trk_pt"]
mySVtrks_minHits6_trk_eta = branches_minHits6["mySVtrks_trk_eta"]


nGV_minHits2 = branches_minHits2["nGV"]
nmySV_minHits2 = branches_minHits2["nmySV"]
mySV_minHits2_x = branches_minHits2["mySV_x"]
mySV_minHits2_y = branches_minHits2["mySV_y"]
mySV_minHits2_z = branches_minHits2["mySV_z"]
GV_Hadron_SV_minHits2Idx = branches_minHits2["GV_Hadron_SVIdx"]
nmyGV_minHits2 = branches_minHits2["nGV"]
GVtrack_minHits2_Hadron_pdgId = branches_minHits2["GV_Hadron_pdgId"]
mySVtrks_minHits2_trk_pt = branches_minHits2["mySVtrks_trk_pt"]
mySVtrks_minHits2_trk_eta = branches_minHits2["mySVtrks_trk_eta"]

nGV_minHits4 = branches_minHits4["nGV"]
nmySV_minHits4 = branches_minHits4["nmySV"]
mySV_minHits4_x = branches_minHits4["mySV_x"]
mySV_minHits4_y = branches_minHits4["mySV_y"]
mySV_minHits4_z = branches_minHits4["mySV_z"]
GV_Hadron_SV_minHits4Idx = branches_minHits4["GV_Hadron_SVIdx"]
nmyGV_minHits4 = branches_minHits4["nGV"]
GVtrack_minHits4_Hadron_pdgId = branches_minHits4["GV_Hadron_pdgId"]
mySVtrks_minHits4_trk_pt = branches_minHits4["mySVtrks_trk_pt"]
mySVtrks_minHits4_trk_eta = branches_minHits4["mySVtrks_trk_eta"]
# track
nGV_minHits10 = branches_minHits10["nGV"]
nmySV_minHits10 = branches_minHits10["nmySV"]
mySV_minHits10_x = branches_minHits10["mySV_x"]
mySV_minHits10_y = branches_minHits10["mySV_y"]
mySV_minHits10_z = branches_minHits10["mySV_z"]
GV_Hadron_SV_minHits10Idx = branches_minHits10["GV_Hadron_SVIdx"]
nmyGV_minHits10 = branches_minHits10["nGV"]
GVtrack_minHits10_Hadron_pdgId = branches_minHits10["GV_Hadron_pdgId"]
mySVtrks_minHits10_trk_pt = branches_minHits10["mySVtrks_trk_pt"]
mySVtrks_minHits10_trk_eta = branches_minHits10["mySVtrks_trk_eta"]


nGV_minHits8 = branches_minHits8["nGV"]
nmySV_minHits8 = branches_minHits8["nmySV"]
mySV_minHits8_x = branches_minHits8["mySV_x"]
mySV_minHits8_y = branches_minHits8["mySV_y"]
mySV_minHits8_z = branches_minHits8["mySV_z"]
GV_Hadron_SV_minHits8Idx = branches_minHits8["GV_Hadron_SVIdx"]
nmyGV_minHits8 = branches_minHits8["nGV"]
GVtrack_minHits8_Hadron_pdgId = branches_minHits8["GV_Hadron_pdgId"]
mySVtrks_minHits8_trk_pt = branches_minHits8["mySVtrks_trk_pt"]
mySVtrks_minHits8_trk_eta = branches_minHits8["mySVtrks_trk_eta"]


# %%

def get_efficiency_fakerate(GV_Hadron_SV_Idx, nSV, GVtrack_Hadron_pdgId, pdgs=None):
    if pdgs is not None:
        if pdgs=="b":
            pdgs_numbers = [521,511,531,541,5122,5132,5232,5332,5142,5242,5342,5512,5532,5542,5554]
        elif pdgs=="d":
            pdgs_numbers= [411,421,431,4122,4232,4132,4332,4412,4422,4432,4444]
        elif pdgs=="s":
            pdgs_numbers= [3122,3222,3212,3312,3322,3334]
        elif pdgs=="tau":
            pdgs_numbers= [15]
        flat = ak.flatten(GVtrack_Hadron_pdgId)
        flat_mask = ak.any(flat[..., None] == pdgs_numbers, axis=-1)
        counts = ak.num(GVtrack_Hadron_pdgId)
        mask = ak.unflatten(flat_mask, counts)
        GV_Hadron_SV_Idx = GV_Hadron_SV_Idx[mask]
    n_tot = ak.sum(GV_Hadron_SV_Idx>-2)
    eff = ak.sum(GV_Hadron_SV_Idx>-1)/n_tot
    err_eff = np.sqrt(eff * (1 - eff)/n_tot)
    fr = 1 - ak.sum(GV_Hadron_SV_Idx>-1) / ak.sum(nSV)
    err_fr = np.sqrt(fr * (1 - fr)/n_tot)
    return eff, err_eff, fr, err_fr


matched_minHits2 = ak.sum(GV_Hadron_SV_minHits2Idx>-1)
matched_minHits4 = ak.sum(GV_Hadron_SV_minHits4Idx>-1)
matched_minHits6 = ak.sum(GV_Hadron_SV_minHits6Idx>-1)
matched_minHits8 = ak.sum(GV_Hadron_SV_minHits8Idx>-1)
matched_minHits10 = ak.sum(GV_Hadron_SV_minHits10Idx>-1)

totSV_minHits2 = ak.sum(nmySV_minHits2)
totSV_minHits4 = ak.sum(nmySV_minHits4)
totSV_minHits6 = ak.sum(nmySV_minHits6)
totSV_minHits8 = ak.sum(nmySV_minHits8)
totSV_minHits10 = ak.sum(nmySV_minHits10)

totGV_minHits2 = ak.sum(nmyGV_minHits2)
totGV_minHits4 = ak.sum(nmyGV_minHits4)
totGV_minHits6 = ak.sum(nGV_minHits6)
totGV_minHits8 = ak.sum(nmyGV_minHits8)
totGV_minHits10 = ak.sum(nmyGV_minHits10)

# Efficiency
eff_minHits2 = matched_minHits2 / totGV_minHits2
eff_minHits4 = matched_minHits4 / totGV_minHits4
eff_minHits6 = matched_minHits6 / totGV_minHits6
eff_minHits8 = matched_minHits8 / totGV_minHits8
eff_minHits10 = matched_minHits10 / totGV_minHits10

# Fake Rate
fr_minHits2 = 1 - matched_minHits2 / totSV_minHits2
fr_minHits4 = 1 - matched_minHits4 / totSV_minHits4
fr_minHits6 = 1 - matched_minHits6 / totSV_minHits6
fr_minHits8 = 1 - matched_minHits8 / totSV_minHits8
fr_minHits10 = 1 - matched_minHits10 / totSV_minHits10

eff_minHits2, err_eff_minHits2, fr_minHits2, err_fr_minHits2 = get_efficiency_fakerate(GV_Hadron_SV_minHits2Idx, nmySV_minHits2, GVtrack_minHits6_Hadron_pdgId)
eff_minHits4, err_eff_minHits4, fr_minHits4, err_fr_minHits4 = get_efficiency_fakerate(GV_Hadron_SV_minHits4Idx, nmySV_minHits4, GVtrack_minHits6_Hadron_pdgId)
eff_minHits6, err_eff_minHits6, fr_minHits6, err_fr_minHits6 = get_efficiency_fakerate(GV_Hadron_SV_minHits6Idx, nmySV_minHits6, GVtrack_minHits6_Hadron_pdgId)
eff_minHits8, err_eff_minHits8, fr_minHits8, err_fr_minHits8 = get_efficiency_fakerate(GV_Hadron_SV_minHits8Idx, nmySV_minHits8, GVtrack_minHits8_Hadron_pdgId)
eff_minHits10, err_eff_minHits10, fr_minHits10, err_fr_minHits10 = get_efficiency_fakerate(GV_Hadron_SV_minHits10Idx, nmySV_minHits10, GVtrack_minHits10_Hadron_pdgId)

rows = [
    ("minHits2",    matched_minHits2,    totSV_minHits2, totGV_minHits2, eff_minHits2, err_eff_minHits2, fr_minHits2, err_fr_minHits2),
    ("minHits4",    matched_minHits4,    totSV_minHits4, totGV_minHits4, eff_minHits4, err_eff_minHits4, fr_minHits4, err_fr_minHits4),
    ("minHits6", matched_minHits6, totSV_minHits6, totGV_minHits6, eff_minHits6, err_eff_minHits6, fr_minHits6, err_fr_minHits6),
    ("minHits8",   matched_minHits8,   totSV_minHits8, totGV_minHits8, eff_minHits8, err_eff_minHits8, fr_minHits8, err_fr_minHits8),
    ("minHits10",   matched_minHits10,   totSV_minHits10, totGV_minHits10, eff_minHits10, err_eff_minHits10, fr_minHits10, err_fr_minHits10),
]
# %%
print("\nSV Matching Summary")
print("-" * 103)
print(f"{'Collection':<12}     {'Matched SV':>12}     {'Total SV':>12}       {'Total GV':>12}     {'Efficiency [%]':>15}     {'Fake Rate [%]':>12}")
print("-" * 103)

for name, matched, totalSV, totalGV, eff, err_eff, fr, err_fr in rows:
    print(f"{name:<12}     {matched:>12.0f}     {totalSV:>12.0f}     {totalGV:>12.0f}     {eff*100:8.2f}+-{err_eff*100:>.5f}      {fr*100:>8.2f}+-{err_fr*100:>.5f}")

print("-" * 103)
fig, ax = plt.subplots(1, 1)
labels = [row[0] for row in rows]
eff_values = [row[4] for row in rows]
eff_errors = [row[5] for row in rows]
fr_values = [row[6] for row in rows]
fr_errors = [row[7] for row in rows]
fig, ax = plt.subplots(1, 1)
for i in range(len(labels)):
    ax.errorbar(eff_values[i], fr_values[i], xerr=eff_errors[i], yerr=fr_errors[i], marker='o', linestyle='none', label=labels[i])


ax.errorbar(x=0.494,y=0.539, xerr=0.003, yerr=0.003, label="Central IVF", marker="o")
ax.legend()
ax.set_xlim(0.48, 0.56)
ax.set_ylim(0.48, 0.56)
ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
ax.set_xlabel("Efficiency")
ax.set_ylabel("Fake Rate")
# %%
fig, ax = plt.subplots(1, 1)
for i in range(len(labels)):
    minHits = int(labels[i].replace("minHits", ""))
    print(labels[i], minHits, eff_values[i], fr_values[i])
    ax.errorbar(minHits, eff_values[i] - fr_values[i], marker='o', linestyle='none', label=labels[i])
ax.legend()
ax.set_ylabel("Efficiency - Fake Rate")
ax.set_xlabel("Min Hits")
# %%
for ev in range(50):
    if ak.sum(GV_Hadron_SV_minHits10Idx[ev]>-1) > ak.sum(GV_Hadron_SV_candIdx[ev]>-1):
        print(ev, ak.sum(GV_Hadron_SV_minHits10Idx[ev]>-1), ak.sum(GV_Hadron_SV_centralIdx[ev]>-1))

        
# %%
fig, ax = plt.subplots(1, 1)        
ax.hist(ak.ravel(SVDaughters_central_pt), bins=np.linspace(0, 5, 101), histtype='step', density=True, label="Central")
ax.hist(ak.ravel(SVDaughters_cand_pt), bins=np.linspace(0, 5, 101), histtype='step', density=True, label="Candidate")
ax.hist(ak.ravel(mySVtrks_trk_pt), bins=np.linspace(0, 5, 101), histtype='step', density=True, label="Track")
ax.set_xlabel(r"SV Daughter $p_T$ [GeV]")
ax.set_ylabel("Normalized Events")
ax.legend()


fig, ax = plt.subplots(1, 1)        
ax.hist(ak.ravel(SVDaughters_central_eta), bins=np.linspace(-2.5, 2.5, 101), histtype='step', density=True, label="Central")
ax.hist(ak.ravel(SVDaughters_cand_eta), bins=np.linspace(-2.5, 2.5, 101), histtype='step', density=True, label="Candidate")
ax.hist(ak.ravel(mySVtrks_trk_eta), bins=np.linspace(-2.5, 2.5, 101), histtype='step', density=True, label="Track")
ax.set_xlabel(r"SV Daughter $\eta$")
ax.set_ylabel("Normalized Events")
ax.legend()


# %%
fig, ax = plt.subplots(1, 1)

central = ak.ravel(ak.run_lengths(branches_central["SVDaughters_SVIdx"]))
cand    = ak.ravel(ak.run_lengths(branches_cand["SVDaughters_SVIdx"]))
track   = ak.ravel(ak.run_lengths(branches_minHits10["mySVtrks_trk_SVidx"]))

bins = np.arange(2, 8)

ax.hist(central, bins=bins, histtype='step', density=True, label="Central")
ax.hist(cand,    bins=bins, histtype='step', density=True, label="Candidate")
ax.hist(track,   bins=bins, histtype='step', density=True, label="Track")

ax.set_xlabel("nSVDaughters")
ax.set_ylabel("Normalized Events")
ax.legend()

# Entry counters
ax.text(0.95, 0.94, f"Central Entries {len(central)}",
        transform=ax.transAxes, ha='right')
ax.text(0.95, 0.89, f"Candidate Entries {len(cand)}",
        transform=ax.transAxes, ha='right')
ax.text(0.95, 0.84, f"Track Entries {len(track)}",
        transform=ax.transAxes, ha='right')

# Optional bin labels (example using Central)
hist_vals_central, _ = np.histogram(central, bins=bins, density=True)
hist_vals_cand, _ = np.histogram(cand, bins=bins, density=True)
hist_vals_minHits10, _ = np.histogram(track, bins=bins, density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2

for x, y in zip(bin_centers, hist_vals_central):
    if y > 0:
        ax.text(x, 0.6, f"{y*100:.1f}%", ha='center', va='bottom', color="C0", fontsize=16)
for x, y in zip(bin_centers, hist_vals_cand):
    if y > 0:
        ax.text(x, 0.57, f"{y*100:.1f}%", ha='center', va='bottom', color="C1", fontsize=16)
for x, y in zip(bin_centers, hist_vals_minHits10):
    if y > 0:
        ax.text(x, 0.54, f"{y*100:.1f}%", ha='center', va='bottom', color="C2", fontsize=16)
ax.set_ylim(0, 0.8)
plt.show()
# %%
