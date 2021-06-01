# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:48:08 2021

@author: tomglose
"""
import pandas as pd
import hydrostats as hs
import seaborn as sns
import numpy as np
import os
from pathlib import Path

working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Figures/').mkdir(parents = True, exist_ok = True)


reject_runs = pd.read_csv('./Evaluation_Data/Evaluation/Reject_Heads.csv', 
                          index_col = [0]).columns.tolist()
accept_runs = pd.read_csv('./Evaluation_Data/Evaluation/Accept_Heads.csv', 
                          index_col = [0]).columns.tolist()


# Read in data from .csv files that contain real data from SD_6, format, and organize

hc_file = ('./Validation/Year_to_Year_Head_Change.csv')
dtw_file = ('./Validation/Year_to_Year_Heads.csv')

# Change in head
hc = pd.read_csv(hc_file, usecols = ['Average'])
hc_std = pd.read_csv(hc_file, usecols = ['Standard Deviation'])

# Depth to water
heads = pd.read_csv(dtw_file, usecols = ['Average'])
heads_std = pd.read_csv(dtw_file, usecols = ['Standard Deviation'])


Cal_HC = pd.read_csv('./Evaluation_Data/Evaluation/Accept_HC.csv', index_col = [0])
Cal_Heads = pd.read_csv('./Evaluation_Data/Evaluation/Accept_Heads.csv', index_col = [0])

Bad_Cal_HC = pd.read_csv('./Evaluation_Data/Evaluation/Reject_HC.csv', index_col = [0])
Bad_Cal_Heads = pd.read_csv('./Evaluation_Data/Evaluation/Reject_Heads.csv', index_col = [0])

#%%
# Quantifying KGE for head change and heads
lhs = pd.read_csv('./Inputs/Eval_LHS_Parameters.csv')

lhs.LI = np.log10(lhs.LI)
lhs.K_v = np.log10(lhs.K_v)

data_heads = []
data_hc = []
accept_runs_index = [int(i) - 1 for i in accept_runs]
reject_runs_index = [int(i) - 1 for i in reject_runs]
lhs_index = sorted(accept_runs_index + reject_runs_index)
lhs_index_str = [str(i + 1) for i in lhs_index]


for i in lhs_index_str:
    if i in accept_runs:
        data_heads.append(hs.kge_2012(Cal_Heads[i].squeeze(), heads.iloc[:, 0], 
                                        return_all = True))
        
        data_hc.append(hs.kge_2012(Cal_HC[i].squeeze(), hc.iloc[:, 0], 
                                        return_all = True))
        
    else:   
        data_heads.append((float('inf'),float('inf'), float('inf'), float('inf')))

        data_hc.append((float('inf'),float('inf'), float('inf'), float('inf')))


kge_heads = pd.DataFrame(data_heads, columns = ['r', 'alpha', 'beta', 'kge_heads'], 
                         index = lhs_index)     
kge_hc = pd.DataFrame(data_hc, columns = ['r', 'alpha', 'beta', 'kge_hc'], 
                      index = lhs_index) 


kge_combine = pd.concat([kge_heads['kge_heads'], kge_hc['kge_hc']], axis=1, keys=['kge_heads', 'kge_hc'])

kge_combine['kge_min'] = kge_combine[['kge_heads', 'kge_hc']].min(axis = 1)

kge_combine.drop(['kge_heads', 'kge_hc'], axis = 1, inplace = True)


kge_hc.fillna(-999, inplace = True)
kge_heads.fillna(-999, inplace = True)


kge_hc['kge_group_hc'] = pd.cut(kge_hc.iloc[:, 3], 
                              bins = ([-float('inf'), -0.41,  0.0, 0.5, 1, float('inf')]), 
                              right = True, include_lowest = True, 
                              labels = ['Poor', 'Low', 'Medium', 'High', 'Discarded Run'])

kge_heads['kge_group_heads'] = pd.cut(kge_heads.iloc[:, 3], 
                              bins = ([-float('inf'), -0.41,  0.0, 0.5, 1, float('inf')]), 
                              right = True, include_lowest = True, 
                              labels = ['Poor', 'Low', 'Medium', 'High', 'Discarded Run'])

kge_combine['kge_group'] = pd.cut(kge_combine.iloc[:, 0], 
                              bins = ([-float('inf'), -0.41,  0.0, 0.5, 1, float('inf')]), 
                              right = True, include_lowest = True, 
                              labels = ['Poor', 'Low', 'Medium', 'High', 'Discarded Run'])


kge_hc.kge_group_hc = pd.Categorical(kge_hc.kge_group_hc, 
                                      categories = ['Discarded Run', 'Poor', 'Low',
                                                    'Medium', 'High'],
                                      ordered = True)

kge_heads.kge_group_heads = pd.Categorical(kge_heads.kge_group_heads, 
                                      categories = ['Discarded Run', 'Poor', 'Low',
                                                    'Medium', 'High'],
                                      ordered = True)

kge_combine.kge_group = pd.Categorical(kge_combine.kge_group, 
                                      categories = ['Discarded Run', 'Poor', 'Low',
                                                    'Medium', 'High'], 
                                      ordered = True)


kge_var_hc = pd.merge(lhs, kge_hc, left_index = True, right_index = True)
kge_var_heads = pd.merge(lhs, kge_heads, left_index = True, right_index = True)
kge_var = pd.merge(lhs, kge_combine, left_index = True, right_index = True)


hc_high_index = kge_hc.index[kge_hc['kge_group_hc'] == 'High'].tolist()
heads_high_index = kge_heads.index[kge_heads['kge_group_heads'] == 'High'].tolist()
combo_high_index = kge_combine.index[kge_combine['kge_group'] == 'High'].tolist()

combo_high_index = [x + 1 for x in combo_high_index]

kge_var_hc.sort_values('kge_group_hc', inplace = True)
kge_var_heads.sort_values('kge_group_heads', inplace = True)
kge_var.sort_values('kge_group', inplace = True)

kge_var_hc.to_csv('./Evaluation_Data/Evaluation/KGE_Eval_HC.csv')
kge_var_heads.to_csv('./Evaluation_Data/Evaluation/KGE_Eval_Heads.csv')
kge_var.to_csv('./Evaluation_Data/Evaluation/KGE_Eval_Combo.csv')

pd.DataFrame(combo_high_index).to_csv('./Inputs/High_KGE_Index_Eval.csv')


#%%
# Setup legend elements to be used throughout 
from matplotlib.lines import Line2D
color_list = (sns.color_palette("coolwarm", 4))
color_list = np.array(color_list)
legend_elements = [Line2D([0], [0], marker = 'o', color = 'w', markersize = 6, 
                          markerfacecolor = color_list[0], label = 'Poor (< -0.41)'), 
                   Line2D([0], [0], marker = 'o', color = 'w', markersize = 6, 
                          markerfacecolor = color_list[1], label = 'Low (-0.41 to 0)'),
                   Line2D([0], [0], marker = 'o', color = 'w', markersize = 6, 
                          markerfacecolor = color_list[2], label = 'Medium (0 to 0.5)'),
                   Line2D([0], [0], marker = 'o', color = 'w', markersize = 6, 
                          markerfacecolor = color_list[3], label = 'High (0.5 - 1)'),
                   Line2D([0], [0], marker = 'X', color = 'w', markersize = 6,
                          markerfacecolor = 'lightgrey', label = 'Discarded Run')]

#%% Plotting Parameters

mm = 1/25.4
palette_dict = {'Poor': color_list[0],
                'Low': color_list[1],
                'Medium': color_list[2],
                'High': color_list[3],
                'Discarded Run': (211/255, 211/255, 211/255, .5)}

sns.set(font_scale = 0.6)
sns.set_style("ticks")

#%%
#KGE_Combined_Correlation
kge_combo = sns.pairplot(kge_var, x_vars = ['K_v', 'EPS', 'LI', 'Sy'],
                            y_vars = ['K_v', 'EPS', 'LI', 'Sy'], 
                            hue_order = ['High', 'Medium', 'Low', 'Poor', 'Discarded Run'],
                            kind = "scatter", hue = 'kge_group',
                            palette = palette_dict, markers = ['X', 'o', 'o', 'o', 'o'], 
                            corner = True, diag_kind = 'kde',
                            plot_kws = {'edgecolor' : None,
                                        's': 5},
                            diag_kws = {"linewidth": 0, "shade": False},
                            grid_kws = {'layout_pad': 0.6})


kge_combo.fig.set_size_inches(115*mm, 115*mm)

kge_combo.axes[0, 0].set_xlim((-6, 1))
kge_combo.axes[1, 1].set_xlim((2, 5))
kge_combo.axes[2, 2].set_xlim((-6, -3))
kge_combo.axes[3, 3].set_xlim((0.08, 0.16))

kge_combo.axes[0, 0].set_visible(False)
kge_combo.axes[1, 1].set_visible(False)
kge_combo.axes[2, 2].set_visible(False)
kge_combo.axes[3, 3].set_visible(False)

kge_combo.axes[1, 0].set_ylabel(r'Brooks and Corey $\epsilon$ (-)', fontsize = 6)
kge_combo.axes[3, 1].set_xlabel(r'Brooks and Corey $\epsilon$ (-)', fontsize = 6)

kge_combo.axes[2, 0].set_ylabel(r'$\log_{10}$ LI (m $d^{-1}$)', fontsize = 6)
kge_combo.axes[3, 2].set_xlabel(r'$\log_{10}$ LI (m $d^{-1}$)', fontsize = 6)

kge_combo.axes[3, 0].set_ylabel(r'$S_Y$ (-)', fontsize = 6)
kge_combo.axes[3, 3].set_xlabel(r'')
# kge_combo.axes[3, 3].set_xlabel(r'$S_Y$')

kge_combo.axes[0, 0].set_ylabel(r'$\log_{10}$ $K_Z$ (m $d^{-1}$)', fontsize = 6)
kge_combo.axes[3, 0].set_xlabel(r'$\log_{10}$ $K_Z$ (m $d^{-1}$)', fontsize = 6)


kge_combo._legend.remove()
kge_combo.add_legend(handles =  legend_elements, title ='KGE_Combination', 
                           bbox_to_anchor = [0.65, 0.44], markerscale = 0.75)


kge_combo.tight_layout()
kge_combo.savefig('./Figures/Fig4_PairPlot.png', dpi = 300)
