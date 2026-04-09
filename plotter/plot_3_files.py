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
fileName_cand = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/candidate_tt_2.root"
f_cand = uproot.open(fileName_cand)
tree_cand = f_cand["Events"]
branches_cand = tree_cand.arrays()

fileName_central = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/central_tt_2.root"
f_central = uproot.open(fileName_central)
tree_central = f_central["Events"]
branches_central = tree_central.arrays()

fileName_track = "/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/track_cov.root"
f_track = uproot.open(fileName_track)
tree_track = f_track["Events"]
branches_track = tree_track.arrays()



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
# Efficiency calculations
nGV = branches_central["nGV"]
GV_Hadron_pdgId = branches_central["GV_Hadron_pdgId"]



#central
GV_isB_central = branches_central["GV_isB"]
GV_isD_central = branches_central["GV_isD"]
GV_Hadron_SVIdx_central = branches_central["GV_Hadron_SVIdx"]
GV_Hadron_pdgId_central = branches_central["GV_Hadron_pdgId"]
GV_pt_central = branches_central["GV_pt"]

# track
GV_isB_track = branches_track["GV_isB"]
GV_pt_track = branches_track["GV_pt"]
GV_isD_track = branches_track["GV_isD"]
GV_Hadron_SVIdx_track = branches_track["GV_Hadron_SVIdx"]
GV_Hadron_pdgId_track = branches_track["GV_Hadron_pdgId"]

# cand
GV_isB_cand = branches_cand["GV_isB"]
GV_isD_cand = branches_cand["GV_isD"]
GV_Hadron_SVIdx_cand = branches_cand["GV_Hadron_SVIdx"]
GV_Hadron_pdgId_cand = branches_cand["GV_Hadron_pdgId"]
GV_pt_cand = branches_cand["GV_pt"]

map_to_groups_vec = np.vectorize(map_to_groups)
mesons_central = map_to_groups_vec(ak.flatten(GV_Hadron_pdgId_central))
mesons_track = map_to_groups_vec(ak.flatten(GV_Hadron_pdgId_track))
mesons_cand = map_to_groups_vec(ak.flatten(GV_Hadron_pdgId_cand))

# %%

efficiencyVsVariable_collections(nums=[mesons_central[(ak.flatten(GV_Hadron_SVIdx_central)>-1)], 
                                       mesons_track[(ak.flatten(GV_Hadron_SVIdx_track)>-1)], 
                                       mesons_cand[(ak.flatten(GV_Hadron_SVIdx_cand)>-1)], 
                                       ],
                                dens=[mesons_central,
                                    mesons_track,
                                    mesons_cand
                                    ],
                                    labels=["Central", "Track", "Candidate"],
                                    colors=['C0', 'C1', 'C2'],
                                    bins=np.linspace(-0.5, 5.5, 7), xlabel="Hadron Flavor",
                                    outName="/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/plots/efficiency/eff_pdgDiff_3coll.png", title = "All particles",
                                    tick_positions = [0, 1, 2, 3, 4, 5],
                                    tick_labels = ['D mesons', 'B mesons', 'Strange Baryons', 'Charmed Baryons', 'Bottom Baryons', 'Tau'],)




efficiencyVsVariable_collections(nums=[ak.flatten(GV_pt_central[(GV_Hadron_SVIdx_central)>-1]), 
                                       ak.flatten(GV_pt_track[(GV_Hadron_SVIdx_track)>-1]), 
                                       ak.flatten(GV_pt_cand[(GV_Hadron_SVIdx_cand)>-1]), 
                                       ],
                                dens=[ak.flatten(GV_pt_central),
                                    ak.flatten(GV_pt_track),
                                    ak.flatten(GV_pt_cand)],
                                    labels=["Central", "Track", "Candidate"],
                                    colors=['C0', 'C1', "C2"],
                                    bins=np.linspace(10, 20, 31), xlabel="p$_T$ [GeV]",
                                    outName="/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/plots/efficiency/eff_pT_3coll.png", title = "All particles",
                                    )


efficiencyVsVariable_collections(nums=[ ak.flatten(ak.run_lengths(branches_central["GVDaughters_hadronIndex"])[(GV_Hadron_SVIdx_central>-1)]), 
                                        ak.flatten(ak.run_lengths(branches_track["GVDaughters_hadronIndex"])[(GV_Hadron_SVIdx_track>-1)]),
                                        ak.flatten(ak.run_lengths(branches_cand["GVDaughters_hadronIndex"])[(GV_Hadron_SVIdx_cand>-1)])
                                        ],
                                dens=[  ak.flatten(ak.run_lengths(branches_central["GVDaughters_hadronIndex"])),
                                        ak.flatten(ak.run_lengths(branches_track["GVDaughters_hadronIndex"])),
                                        ak.flatten(ak.run_lengths(branches_cand["GVDaughters_hadronIndex"]))
                                        ],
                                    labels=["Central", "Track", "Candidate"],
                                    colors=['C0', 'C1', 'C2'],
                                    bins=np.arange(0, 10), xlabel="Number of hadron daughters",
                                    outName="/work/gcelotto/btv_mini_rerun/CMSSW_10_6_32_patch1/src/plots/efficiency/eff_nGenTracksDiff_3coll.png", title = "All particles",
                                    )
# %%
