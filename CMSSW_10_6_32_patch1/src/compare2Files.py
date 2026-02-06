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



# %%
#fileName = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/HIG-RunIISummer20UL18NanoAODv9-12707.root"
central = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/central.root"
custom = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/custom.root"
f_central = uproot.open(central)
f_custom = uproot.open(custom)
tree_central = f_central["Events"]
tree_custom = f_custom["Events"]
branches_central = tree_central.arrays()
branches_custom = tree_custom.arrays()


# %%

nSV = branches_central["nSV"]
SV_x = branches_central["SV_x"]
SV_y = branches_central["SV_y"]
SV_z = branches_central["SV_z"]
# %%
mySV_chi2 = branches_custom["nmySV"]
mySV_x = branches_custom["mySV_x"]
mySV_y = branches_custom["mySV_y"]
mySV_z = branches_custom["mySV_z"]

# %%
fig, ax = plt.subplots(1, 1)
xmin, xmax = -3, 5
bins = np.linspace(xmin, xmax, xmax-xmin+1)
values = np.clip(np.array(mySV_chi2) +-1*np.array(nSV), bins[0], bins[-1])

counts, edges, patches = ax.hist(values, bins=bins-0.5, density=False, edgecolor='black')
for count, edge in zip(counts, edges[:-1]):
    if count > 0:
        ax.text(edge + 0.5*(edges[1]-edges[0]), count, f'{int(count)}',
                ha='center', va='bottom', fontsize=18)
ax.set_xlabel("nSV(IVF@mini) - nSV(IVF@reco)")
ax.set_ylabel("Counts")  # switched to counts, since density=False
ax.text(x=0.95, y=0.95, s=f'Events: {len(values)}', transform=ax.transAxes,
        ha='right', va='top', fontsize=18)
plt.show()
# %%
