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

# %%
#fileName = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/HIG-RunIISummer20UL18NanoAODv9-12707.root"
fileName_cand = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/candidate.root"
f_cand = uproot.open(fileName_cand)
tree_cand = f_cand["Events"]
branches_cand = tree_cand.arrays()

fileName_central = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/central.root"
f_central = uproot.open(fileName_central)
tree_central = f_central["Events"]
branches_central = tree_central.arrays()

fileName_track = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/track.root"
f_track = uproot.open(fileName_track)
tree_track = f_track["Events"]
branches_track = tree_track.arrays()
# %%


ev=6
for ev in range(0,20):


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
        ax.scatter(mySV_cand_x, mySV_cand_y, label='Reco SV (IVF RunCandidate): %d Matched'%(np.sum(GV_Hadron_SV_candIdx>-1)), marker="s", color='lightgreen', s=80)
    else:
        pass

    if nSV_central>0:
        ax.scatter(SV_central_x, SV_central_y, label='Reco SV (IVF slimmed central): %d Matched'%(np.sum(GV_Hadron_SV_centralIdx>-1)), marker="s", color='C2', s=20)
    else:
        pass

    if nmySV_track>0:
        ax.scatter(mySV_track_x, mySV_track_y, label='Reco SV (IVF RunTrack): %d Matched'%(np.sum(GV_Hadron_SV_trackIdx>-1)), marker=">", color='C3', s=50, alpha=0.7)
    else:
        pass

    ax.set_xlabel("X [cm]")
    ax.set_ylabel("Y [cm]")


    for genIdx, svIdx in enumerate(GV_Hadron_SV_candIdx):
        if svIdx==-1:
            continue
        x_values = [mySV_cand_x[svIdx], GV_x[genIdx]]
        y_values = [mySV_cand_y[svIdx], GV_y[genIdx]]
        ax.plot(x_values, y_values, color='black', marker='none')


    ax.legend(bbox_to_anchor=(1,1.05))
    fig.savefig("/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/plotsPerEvent/EventDisplay_ev%d.png"%ev, bbox_inches='tight')
    plt.close()

# %%



# %%
fig, ax = plt.subplots(1, 1)
xmin, xmax = -3, 5
bins = np.linspace(xmin, xmax, xmax-xmin+1)
values = np.clip(np.array(nmySV) +-1*np.array(nSV), bins[0], bins[-1])

counts, edges, patches = ax.hist(values, bins=bins-0.5, density=False, edgecolor='black')
for count, edge in zip(counts, edges[:-1]):
    if count > 0:
        ax.text(edge + 0.5*(edges[1]-edges[0]), count, f'{int(count)}',
                ha='center', va='bottom', fontsize=18)
ax.set_xlabel("nSV(IVF@mini) - nSV(IVF@reco)")
ax.set_ylabel("Counts")  # switched to counts, since density=False
plt.show()
# %%
fig, ax = plt.subplots(1, 1)
counts, edges, patches = ax.hist(ak.flatten(branches["mySVtrks_trk_weight"]),bins=np.linspace(0, 1, 10),density=False, edgecolor='black')
for count, edge in zip(counts, edges[:-1]):
    if count > 0:
        ax.text(edge + 0.5*(edges[1]-edges[0]), count, f'{int(count)}',
                ha='center', va='bottom', fontsize=18)
ax.set_xlabel("Track weight in SV (IVF@mini)")
# %%
