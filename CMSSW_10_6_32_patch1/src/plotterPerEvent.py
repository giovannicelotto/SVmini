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
fileName = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/withoutCut.root"
f = uproot.open(fileName)
tree = f["Events"]
branches = tree.arrays()
# %%
ev=6
nGV = branches["nGV"][ev]
GV_x = branches["GV_x"][ev]
GV_y = branches["GV_y"][ev]
GV_z = branches["GV_z"][ev]
GV_x_i = branches["GV_x_i"][ev]
GV_y_i = branches["GV_y_i"][ev]
GV_z_i = branches["GV_z_i"][ev]
GenVtx_x = branches["GenVtx_x"][ev]   # What is this? It is not perfectly equal to PV_x
GenVtx_y = branches["GenVtx_y"][ev]   # What is this? It is not perfectly equal to PV_y
GV_Hadron_pdgId = branches["GV_Hadron_pdgId"][ev]
nmySV = branches["nmySV"][ev]
mySV_x = branches["mySV_x"][ev]
mySV_y = branches["mySV_y"][ev]
mySV_z = branches["mySV_z"][ev]
nSV = branches["nSV"][ev]
SV_x = branches["SV_x"][ev]
SV_y = branches["SV_y"][ev]
SV_z = branches["SV_z"][ev]
GV_Hadron_SVIdx = branches["GV_Hadron_SVIdx"][ev]




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

if nmySV>0:
    ax.scatter(mySV_x, mySV_y, label='Reco SV (IVF@mini): %d Matched'%(np.sum(GV_Hadron_SVIdx>-1)), marker="s", color='lightgreen', s=80)
else:
    pass

if nSV>0:
    ax.scatter(SV_x, SV_y, label='Reco SV (IVF@reco)', marker="s", color='C2', s=20)
else:
    pass

ax.set_xlabel("X [cm]")
ax.set_ylabel("Y [cm]")


for genIdx, svIdx in enumerate(GV_Hadron_SVIdx):
    if svIdx==-1:
        continue
    x_values = [mySV_x[svIdx], GV_x[genIdx]]
    y_values = [mySV_y[svIdx], GV_y[genIdx]]
    ax.plot(x_values, y_values, color='black', marker='none')


ax.legend()
#fig.savefig("/t3home/gcelotto/BTV/plots/newEventDisplay_ev%d.png"%ev, bbox_inches='tight')
#plt.close()

# %%
nGV = branches["nGV"]
GV_x = branches["GV_x"]
GV_y = branches["GV_y"]
GV_z = branches["GV_z"]
GV_x_i = branches["GV_x_i"]
GV_y_i = branches["GV_y_i"]
GV_z_i = branches["GV_z_i"]
GenVtx_x = branches["GenVtx_x"]   # What is this? It is not perfectly equal to PV_x
GenVtx_y = branches["GenVtx_y"]   # What is this? It is not perfectly equal to PV_y
GV_Hadron_pdgId = branches["GV_Hadron_pdgId"]
nmySV = branches["nmySV"]
mySV_x = branches["mySV_x"]
mySV_y = branches["mySV_y"]
mySV_z = branches["mySV_z"]
mySV_pt = branches["mySV_pt"]
mySV_eta = branches["mySV_eta"]
mySV_phi = branches["mySV_phi"]
nSV = branches["nSV"]
SV_x = branches["SV_x"]
SV_y = branches["SV_y"]
SV_z = branches["SV_z"]
GV_Hadron_SVIdx = branches["GV_Hadron_SVIdx"]
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
