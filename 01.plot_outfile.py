#!/usr/bin/python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



pval_each=pd.read_csv("pdb_pval")

pval_each['pvals']=pval_each['pvals']+0.0000000000000000001
pval_each['logar']=-np.log10(pval_each.pvals)

fig, ax1 = plt.subplots()
#plt.subplots_adjust(bottom=.5, left=.5)
x = pval_each['index']
y0=pval_each['foreground']
y1 = pval_each['bg_means']
y2 = pval_each['logar']


pval_each['regs']=pval_each['regs'].map(lambda x: np.nan if x < 1 else 0)
regs=pval_each['regs']

pval_each['active']=pval_each['active'].map(lambda x: np.nan if x < 1 else 0)
active=pval_each['active']

stdpl=pval_each['bg_means']+pval_each['bg_stdev']
stdm=pval_each['bg_means']-pval_each['bg_stdev']


ax1.plot(x, y0,'k-',label="Perfect")
ax1.plot(x, y1, '#404040','-')
ax1.plot(x, regs, 'r.')
ax1.plot(x, active, 'y.')
ax1.plot(x, stdpl, '#C0C0C0','-')
ax1.plot(x, stdpl, '#C0C0C0','-')
ax1.fill_between(x, stdm, stdpl, where=stdpl >= stdm, facecolor='#C0C0C0', interpolate=True)
ax1.set_ylabel("Phopshorylation per residue", fontsize=12)
ax2 = ax1.twinx()
ax2.plot(x, y2, '#0066CC','-')
ax2.set_ylabel("-log(pvalue)", fontsize=12)

hotspots=pval_each.index[pval_each['hotspot_plus'] >= 1].tolist() #####comment out these 3 lines if using full ali
for i in hotspots:					###############comment out these 3 lines if using full ali
	ax1.axvspan(i-0.5, i+0.5, alpha=0.5, color='yellow')	#######comment out these 3 lines if using full ali


plt.show()

