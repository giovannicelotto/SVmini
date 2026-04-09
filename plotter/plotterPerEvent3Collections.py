# %%
import uproot
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math, sys
import awkward as ak
import mplhep as hep
hep.style.use("CMS")
#from tuplizer.utilsForScript import distance_3d, getPdgMask
#from helpers import getTreeAndBranches, criterion0, criterion1, eventDisplay, getTreeAndBranches
#sys.path.append("/t3home/gcelotto/BTV/scripts/tuplizer")
#from ntupleLinker import getMesons, getParams, getOneDaughter, matchingEvent


def map_to_groups_letter(value):
    if abs(value) in [511, 521, 531, 541]:
        return 'B'
    elif abs(value) in [411, 421, 431]:
        return 'D'
    elif ((abs(value) > 3000) & (abs(value) < 4000)):
        return 'SB'
    elif ((abs(value) > 4000) & (abs(value) < 5000)):
        return 'CB'
    elif ((abs(value) > 5000) & (abs(value) < 6000)):
        return 'BB'
    # Add more conditions as needed
    else:
        return -1  # or any default value for unmatched cases
def map_to_groups(value):
    if abs(value) in [411, 421, 431]:
        return 0
    elif abs(value) in [511, 521, 531, 541]:
        return 1
    elif ((abs(value) > 3000) & (abs(value) < 4000)):
        return 2
    elif ((abs(value) > 4000) & (abs(value) < 5000)):
        return 3
    elif ((abs(value) > 5000) & (abs(value) < 6000)):
        return 4
    elif (abs(value) == 15):
        return 5
    # Add more conditions as needed
    else:
        return -1 
# %%
#fileName = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/HIG-RunIISummer20UL18NanoAODv9-12707.root"
fileName_cand = "/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_minHits4_0p0.root"
f_cand = uproot.open(fileName_cand)
tree_cand = f_cand["Events"]
branches_cand = tree_cand.arrays()

fileName_central = "/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/central.root"
f_central = uproot.open(fileName_central)
tree_central = f_central["Events"]
branches_central = tree_central.arrays()

fileName_track = "/work/gcelotto/btv_mini_rerun/CMSSW_15_0_6/src/track_cov.root"
f_track = uproot.open(fileName_track)
tree_track = f_track["Events"]
branches_track = tree_track.arrays()
# %%


ev=0
for ev in [0,1,2,3,4]:


    nGV = branches_central["nGV"][ev]
    GV_x = branches_central["GV_x"][ev]
    GV_y = branches_central["GV_y"][ev]
    GV_z = branches_central["GV_z"][ev]
    GV_x_i = branches_central["GV_x_i"][ev]
    GV_y_i = branches_central["GV_y_i"][ev]
    GV_z_i = branches_central["GV_z_i"][ev]
    GV_Hadron_pdgId = branches_central["GV_Hadron_pdgId"][ev]
    GenVtx_x = branches_central["GenVtx_x"][ev]   # What is this? It is not perfectly equal to PV_x
    GenVtx_y = branches_central["GenVtx_y"][ev]   # What is this? It is not perfectly equal to PV_y


    nmySV_cand = branches_cand["nmySV"][ev]
    mySV_cand_x = branches_cand["mySV_x"][ev]
    mySV_cand_y = branches_cand["mySV_y"][ev]
    mySV_cand_z = branches_cand["mySV_z"][ev]
    GV_Hadron_SV_candIdx = branches_cand["GV_Hadron_SVIdx"][ev]


    nSV_central = branches_central["nSV"][ev]
    SV_central_x = branches_central["SV_x"][ev]
    SV_central_y = branches_central["SV_y"][ev]
    SV_central_z = branches_central["SV_z"][ev]
    GV_Hadron_SV_centralIdx = branches_central["GV_Hadron_SVIdx"][ev]

    nmySV_track = branches_track["nmySV"][ev]
    mySV_track_x = branches_track["mySV_x"][ev]
    mySV_track_y = branches_track["mySV_y"][ev]
    mySV_track_z = branches_track["mySV_z"][ev]
    GV_Hadron_SV_trackIdx = branches_track["GV_Hadron_SVIdx"][ev]


    # matching is done
    fig, ax = plt.subplots(1, 1)
    ax.scatter(GV_x, GV_y, label='GenVertices', s=80)
    for i in range(nGV):
        x = [GV_x_i[i], GV_x[i]]
        y = [GV_y_i[i], GV_y[i]]
        ax.plot(x, y,linestyle='dotted',alpha=0.8, marker='none')
    ax.scatter(GenVtx_x, GenVtx_y,alpha=1, label="PV", color='black', s=80)


    for gp in range(nGV):
        ax.text(x=GV_x[gp], y=GV_y[gp], s=map_to_groups_letter(GV_Hadron_pdgId[gp]), fontsize=18)

    if nmySV_cand>0:
        ax.scatter(mySV_cand_x, mySV_cand_y, label='Reco SV (IVF Track): %d Matched'%(np.sum(GV_Hadron_SV_candIdx>-1)), marker="s", color='lightgreen', s=80)
    else:
        pass

    if nSV_central>0:
        ax.scatter(SV_central_x, SV_central_y, label='Reco SV (IVF slimmed central): %d Matched'%(np.sum(GV_Hadron_SV_centralIdx>-1)), marker="s", color='C2', s=20)
    else:
        pass

    if nmySV_track>0:
        ax.scatter(mySV_track_x, mySV_track_y, label='Reco SV (IVF track cov): %d Matched'%(np.sum(GV_Hadron_SV_trackIdx>-1)), marker=">", color='C3', s=50, alpha=0.7)
    else:
        pass

    ax.set_xlabel("X [cm]")
    ax.set_ylabel("Y [cm]")


    #for genIdx, svIdx in enumerate(GV_Hadron_SV_trackIdx):
    #    if svIdx==-1:
    #        continue
    #    x_values = [mySV_track_x[svIdx], GV_x[genIdx]]
    #    y_values = [mySV_track_y[svIdx], GV_y[genIdx]]
    #    ax.plot(x_values, y_values, color='black', marker='none')
    for genIdx, svIdx in enumerate(GV_Hadron_SV_candIdx):
        if svIdx==-1:
            continue
        x_values = [mySV_cand_x[svIdx], GV_x[genIdx]]
        y_values = [mySV_cand_y[svIdx], GV_y[genIdx]]
        ax.plot(x_values, y_values, color='black', marker='none')


    ax.legend(bbox_to_anchor=(1,1.05))
    outname = "/work/gcelotto/btv_mini_rerun/plots/EventDisplay_ev%d.png"%ev
    fig.savefig(outname, bbox_inches='tight')
    print("saved ", outname)
    plt.close()

# %%
# Efficiency calculations
nGV = branches_central["nGV"]
GV_x = branches_central["GV_x"]
GV_y = branches_central["GV_y"]
GV_z = branches_central["GV_z"]
GV_x_i = branches_central["GV_x_i"]
GV_y_i = branches_central["GV_y_i"]
GV_z_i = branches_central["GV_z_i"]
GV_Hadron_pdgId = branches_central["GV_Hadron_pdgId"]
GenVtx_x = branches_central["GenVtx_x"]   # What is this? It is not perfectly equal to PV_x
GenVtx_y = branches_central["GenVtx_y"]   # What is this? It is not perfectly equal to PV_y

#cand
nmySV_cand = branches_cand["nmySV"]
mySV_cand_x = branches_cand["mySV_x"]
mySV_cand_y = branches_cand["mySV_y"]
mySV_cand_z = branches_cand["mySV_z"]
GV_Hadron_SV_candIdx = branches_cand["GV_Hadron_SVIdx"]
nmyGV_cand = branches_cand["nGV"]
GVcand_Hadron_pdgId = branches_cand["GV_Hadron_pdgId"]
SVDaughters_cand_pt = branches_cand["SVDaughters_pt"]
SVDaughters_cand_eta = branches_cand["SVDaughters_eta"]

#central
nSV_central = branches_central["nSV"]
nGV_central = branches_central["nGV"]
SV_central_x = branches_central["SV_x"]
SV_central_y = branches_central["SV_y"]
SV_central_z = branches_central["SV_z"]
GV_Hadron_SV_centralIdx = branches_central["GV_Hadron_SVIdx"]
GVcentral_Hadron_pdgId = branches_central["GV_Hadron_pdgId"]
SVDaughters_central_pt = branches_central["SVDaughters_pt"]
SVDaughters_central_eta = branches_central["SVDaughters_eta"]

# track
nmySV_track = branches_track["nmySV"]
mySV_track_x = branches_track["mySV_x"]
mySV_track_y = branches_track["mySV_y"]
mySV_track_z = branches_track["mySV_z"]
GV_Hadron_SV_trackIdx = branches_track["GV_Hadron_SVIdx"]
nmyGV_track = branches_track["nGV"]
GVtrack_Hadron_pdgId = branches_track["GV_Hadron_pdgId"]
mySVtrks_trk_pt = branches_track["mySVtrks_trk_pt"]
mySVtrks_trk_eta = branches_track["mySVtrks_trk_eta"]


# %%

def get_efficiency_fakerate(GV_Hadron_SV_Idx, nSV, pdgs=None):
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


matched_cand = ak.sum(GV_Hadron_SV_candIdx>-1)
matched_central = ak.sum(GV_Hadron_SV_centralIdx>-1)
matched_track = ak.sum(GV_Hadron_SV_trackIdx>-1)

totSV_cand = ak.sum(nmySV_cand)
totSV_central = ak.sum(nSV_central)
totSV_track = ak.sum(nmySV_track)

totGV_cand = ak.sum(nmyGV_cand)
totGV_central = ak.sum(nGV_central)
totGV_track = ak.sum(nmyGV_track)

# Efficiency
eff_cand = matched_cand / totGV_cand
eff_central = matched_central / totGV_central
eff_track = matched_track / totGV_track

# Fake Rate
fr_cand = 1 - matched_cand / totSV_cand
fr_central = 1 - matched_central / totSV_central
fr_track = 1 - matched_track / totSV_track
eff_central, err_eff_central, fr_central, err_fr_central = get_efficiency_fakerate(GV_Hadron_SV_centralIdx, nSV_central)
eff_track, err_eff_track, fr_track, err_fr_track = get_efficiency_fakerate(GV_Hadron_SV_trackIdx, nmySV_track)
eff_cand, err_eff_cand, fr_cand, err_fr_cand = get_efficiency_fakerate(GV_Hadron_SV_candIdx, nmySV_cand)
rows = [
    ("Central", matched_central, totSV_central, totGV_central, eff_central, err_eff_central, fr_central, err_fr_central),
    ("Cand",    matched_cand,    totSV_cand, totGV_cand, eff_cand, err_eff_cand, fr_cand, err_fr_cand),
    ("Track",   matched_track,   totSV_track, totGV_track, eff_track, err_eff_track, fr_track, err_fr_track),
]
# %%
print("\nSV Matching Summary")
print("-" * 103)
print(f"{'Collection':<12}     {'Matched SV':>12}     {'Total SV':>12}       {'Total GV':>12}     {'Efficiency [%]':>15}     {'Fake Rate [%]':>12}")
print("-" * 103)

for name, matched, totalSV, totalGV, eff, err_eff, fr, err_fr in rows:
    print(f"{name:<12}     {matched:>12.0f}     {totalSV:>12.0f}     {totalGV:>12.0f}     {eff*100:8.2f}+-{err_eff*100:>.5f}      {fr*100:>8.2f}+-{err_fr*100:>.5f}")

print("-" * 103)
# %%
for ev in range(50):
    if ak.sum(GV_Hadron_SV_trackIdx[ev]>-1) > ak.sum(GV_Hadron_SV_candIdx[ev]>-1):
        print(ev, ak.sum(GV_Hadron_SV_trackIdx[ev]>-1), ak.sum(GV_Hadron_SV_centralIdx[ev]>-1))

        
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
track   = ak.ravel(ak.run_lengths(branches_track["mySVtrks_trk_SVidx"]))

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
hist_vals_track, _ = np.histogram(track, bins=bins, density=True)
bin_centers = (bins[:-1] + bins[1:]) / 2

for x, y in zip(bin_centers, hist_vals_central):
    if y > 0:
        ax.text(x, 0.6, f"{y*100:.1f}%", ha='center', va='bottom', color="C0", fontsize=16)
for x, y in zip(bin_centers, hist_vals_cand):
    if y > 0:
        ax.text(x, 0.57, f"{y*100:.1f}%", ha='center', va='bottom', color="C1", fontsize=16)
for x, y in zip(bin_centers, hist_vals_track):
    if y > 0:
        ax.text(x, 0.54, f"{y*100:.1f}%", ha='center', va='bottom', color="C2", fontsize=16)
ax.set_ylim(0, 0.8)
plt.show()
# %%
