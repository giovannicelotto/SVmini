import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
hep.style.use("CMS")
eps = 1e-8
def efficiencyVsVariable(num, den, bins, xlabel, outName, title=None, underOverFlow = False, tick_positions=None, tick_labels=None):

    fig,ax = plt.subplots(1, 1)
    matched = np.histogram(num, bins=bins)[0]
    total =   np.histogram(den, bins=bins)[0]

    if underOverFlow:
        matched = np.histogram(np.clip(num, bins[0], bins[-1]), bins=bins)[0]
        total =   np.histogram(np.clip(den, bins[0], bins[-1]), bins=bins)[0]


    bins_center = (bins[:-1]+bins[1:])/2
    ax.errorbar(bins_center, matched/(total+eps), xerr=np.diff(bins)/2,yerr=np.sqrt(matched)/(total+eps), marker='o', linestyle='none', color='black')
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Efficiency [%]")
    ax.set_ylim(0, 1.2)
    ax.text(x=0.95, y=0.94, s="Matched Entries %d"%(len(num)), transform=ax.transAxes, horizontalalignment='right')
    ax.text(x=0.95, y=0.89, s=title, transform=ax.transAxes, horizontalalignment='right')
    #print(tick_positions)
    if tick_positions is not None:
        ax.set_xticks(tick_positions, tick_labels,  rotation=30)
        for x,y in zip(bins_center, matched/(total+eps)):
            if y!=0:
                ax.text(x=x, y=y+0.05, s="%.1f%%"%(y*100), ha='center')

    #if title is not None:
    hep.cms.label()
    fig.savefig(outName, bbox_inches='tight')
    print("Saved %s"%outName)
    plt.close()
    return

def efficiencyVsVariable_collections(nums, dens, labels, colors, bins, xlabel, outName, title=None, underOverFlow = False, tick_positions=None, tick_labels=None):
    '''
    plot for different collections
    
    '''

    fig,ax = plt.subplots(1, 1)
    y_pos=0.95
    for (num, den, label, color) in zip(nums, dens, labels, colors):
        matched = np.histogram(num, bins=bins)[0]
        total =   np.histogram(den, bins=bins)[0]

        if underOverFlow:
            matched = np.histogram(np.clip(num, bins[0], bins[-1]), bins=bins)[0]
            total =   np.histogram(np.clip(den, bins[0], bins[-1]), bins=bins)[0]


        bins_center = (bins[:-1]+bins[1:])/2
        ax.errorbar(bins_center, matched/(total+eps), xerr=np.diff(bins)/2,yerr=np.sqrt(matched)/(total+eps), marker='o', linestyle='none',  label=label, color=color)
        if tick_positions is not None:
            ax.set_xticks(tick_positions, tick_labels,  rotation=30)
            for x,y in zip(bins_center, matched/(total+eps)):
                if y!=0:
                    ax.text(x=x, y=y_pos-0.1, s="%.1f%%"%(y*100), ha='center', color=color)
        y_pos = y_pos - 0.06
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Efficiency [%]")
    ax.set_ylim(0, 1.2)
    ax.text(x=0.95, y=0.94, s="Matched Entries %d"%(len(num)), transform=ax.transAxes, horizontalalignment='right')
    ax.text(x=0.95, y=0.89, s=title, transform=ax.transAxes, horizontalalignment='right')
    #print(tick_positions)

    #if title is not None:
    hep.cms.label()
    ax.legend()
    fig.savefig(outName, bbox_inches='tight')
    print("Saved %s"%outName)
    plt.close()
    return