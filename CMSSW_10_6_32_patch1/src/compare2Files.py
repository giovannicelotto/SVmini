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
#custom = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/custom.root"
custom = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/candidate.root"
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
SV_eta = branches_central["SV_eta"]
SV_phi = branches_central["SV_phi"]
# %%
nmySV = branches_custom["nmySV"]
mySV_x = branches_custom["mySV_x"]
mySV_y = branches_custom["mySV_y"]
mySV_z = branches_custom["mySV_z"]
mySV_eta = branches_custom["mySV_eta"]
mySV_phi = branches_custom["mySV_phi"]

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
ax.set_xlabel("nSV(custom) - nSV(IVFcentral)")
ax.set_ylabel("Counts")  # switched to counts, since density=False
ax.text(x=0.95, y=0.95, s=f'Events: {len(values)}', transform=ax.transAxes,
        ha='right', va='top', fontsize=18)
plt.show()
# %%
from scipy.optimize import linear_sum_assignment
def deltaR_matrix(eta1, phi1, eta2, phi2):

    eta1 = np.array(eta1)
    phi1 = np.array(phi1)
    eta2 = np.array(eta2)
    phi2 = np.array(phi2)

    dphi = np.abs(phi1[:, None] - phi2[None, :])
    dphi = np.where(dphi > np.pi, 2*np.pi - dphi, dphi)

    deta = eta1[:, None] - eta2[None, :]

    return np.sqrt(deta**2 + dphi**2)


dR_t = 0.05
total_valid_matches = []
total_central = []
total_dr_match = []
for i in range(tree_central.num_entries):
    n_central = nSV[i]
    n_custom  = nmySV[i]
    print("Event {}: nSV_central = {}, nSV_custom = {}".format(i, n_central, n_custom))
    if True:
        
        print("Same number of SV → one-to-one matching")

        eta_central = SV_eta[i]
        phi_central = SV_phi[i]

        eta_custom  = mySV_eta[i]
        phi_custom  = mySV_phi[i]

        dr_matrix = deltaR_matrix(
                eta_central,
                phi_central,
                eta_custom,
                phi_custom
        )

        # Hungarian algorithm
        row_idx, col_idx = linear_sum_assignment(dr_matrix)

        valid_matches = []

        for r, c in zip(row_idx, col_idx):

                if dr_matrix[r, c] < dR_t:
                        valid_matches.append((r, c, dr_matrix[r, c]))
                        total_dr_match.append(dr_matrix[r, c])


        print(f"Matched {len(valid_matches)} / {n_central}")
        total_valid_matches.append(len(valid_matches))
        total_central.append(n_central)
        for r, c, drval in valid_matches:
                print(f"  central[{r}] ↔ custom[{c}]  ΔR = {drval:.4e}")

# %%
total_central = np.array(total_central)
total_valid_matches = np.array(total_valid_matches)
total_dr_match = np.array(total_dr_match)
# %%
ratio = total_valid_matches/(total_central+1e-8)
fig, ax = plt.subplots(1,1 )
counts, edges, patches = ax.hist(ratio, bins=np.linspace(0, 1.01, 21), density=False, edgecolor='black')
for count, edge in zip(counts, edges[:-1]):
    if count > 0:
        ax.text(edge + 0.5*(edges[1]-edges[0]), count, f'{int(count)}',
                ha='center', va='bottom', fontsize=18)
ax.text(x=0.05, y=0.95, s="dR < %.2f"%dR_t, transform=ax.transAxes, ha='left', va='top', fontsize=18)
ax.set_xlabel("Matched SVs / SVs in IVFcentral")
# %%
fig, ax = plt.subplots(1, 1)
ax.hist(total_dr_match, bins=np.linspace(0, dR_t, 100), density=False, edgecolor='black')
ax.set_xlabel("dR matching")
ax.set_yscale('log')
# %%
