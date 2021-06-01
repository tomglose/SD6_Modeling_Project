# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 13:40:39 2021

@author: tomglose
"""
import pandas as pd
import hydrostats as hs
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path
import os

# Change directory to working folder <- be sure to change
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

#%% Plot Parameters
mm = 1/25.4
sns.set(font_scale = 0.75)
sns.set_style("ticks")
plt.rcParams.update({'errorbar.capsize': 2})


#%% S1 Cal/val plot
# Attempt at average model run value figure
lhs_lat_inflow = pd.read_csv('./Inputs/Proj_LHS_Lat_Inflow.csv')
lhs_lat_inflow.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs_lat_inflow['Run'] = lhs_lat_inflow['Run'] + 1

lhs_rech = pd.read_csv('./Inputs/Proj_LHS_Recharge.csv')
lhs_rech.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs_rech['Run'] = lhs_rech['Run'] + 1

S1_high_index_str = [str(i) for i in lhs_lat_inflow['Run']]
S2_high_index_str = [str(i) for i in lhs_rech['Run']]


eval_fig = plt.figure(figsize = (190*mm, 115*mm))
gs = eval_fig.add_gridspec(2,2)

ax1 = eval_fig.add_subplot(gs[0, 0])
ax1.plot(range(2000, 2020, 1), hc.iloc[:, 0], '--', color = 'black',
              zorder = len(lhs_lat_inflow) + 1, linewidth = 1)

ax1.errorbar(range(2000, 2020, 1), hc.iloc[:, 0], yerr = hc_std.iloc[:, 0], 
              fmt = 'none', ecolor = 'black', zorder = len(lhs_lat_inflow) + 1, 
              linewidth = 0.8)

ax1.set_ylabel('Annual \u0394H (m)')
ax1.set_title('Lateral-Flow-Dominated', fontsize = 16)
ax1.locator_params(axis = 'x', nbins = 5)



ax1.plot(range(2000, 2020, 1), Cal_HC.loc[:, S1_high_index_str], 
            color = 'gainsboro', linewidth = 1)

ax1.plot(range(2000, 2020, 1), Cal_HC.loc[:, S1_high_index_str].mean(axis = 1),
         color = 'red', linewidth = 1)

ax2 = eval_fig.add_subplot(gs[1, 0])

ax2.plot(range(1999, 2020, 1), heads.iloc[:, 0], '--', color = 'black', 
          zorder = len(lhs_lat_inflow) + 1, linewidth = 1)

ax2.errorbar(range(1999, 2020, 1), heads.iloc[:, 0], yerr = heads_std.iloc[:, 0], 
              fmt = 'none', ecolor = 'black', zorder = len(lhs_lat_inflow) + 1, 
              linewidth = 0.8)

ax2.set_xlabel('Years')
ax2.set_ylabel('Head (m)')

ax2.locator_params(axis = 'x', nbins = 5)


ax2.plot(range(1999, 2020, 1), Cal_Heads.loc[:, S1_high_index_str], 
         color = 'gainsboro', linewidth = 1)
ax2.set_ylim(10, 35)

    
ax2.plot(range(1999, 2020, 1), Cal_Heads.loc[:, S1_high_index_str].mean(axis = 1),
         color = 'red', linewidth = 1)    


# 
ax3 = eval_fig.add_subplot(gs[0, 1], sharey = ax1)

plt.setp(ax3.get_yticklabels(), visible=False)

ax3.plot(range(2000, 2020, 1), hc.iloc[:, 0], '--', color = 'black',
              zorder = len(lhs_rech) + 1, linewidth = 1)

ax3.errorbar(range(2000, 2020, 1), hc.iloc[:, 0], yerr = hc_std.iloc[:, 0], 
              fmt = 'none', ecolor = 'black', zorder = len(lhs_rech) + 1, 
              linewidth = 0.8)

# ax3.set_ylabel('Annual \u0394H (m)')
ax3.set_title('Recharge-Dominated', fontsize = 16)
ax3.locator_params(axis = 'x', nbins = 5)


  

   
ax3.plot(range(2000, 2020, 1), Cal_HC.loc[:, S2_high_index_str], 
         color = 'gainsboro', linewidth = 1)

ax3.plot(range(2000, 2020, 1), Cal_HC.loc[:, S2_high_index_str].mean(axis = 1),
         color = 'red', linewidth = 1)

ax4 = eval_fig.add_subplot(gs[1, 1], sharey = ax2)
plt.setp(ax4.get_yticklabels(), visible=False)
ax4.plot(range(1999, 2020, 1), heads.iloc[:, 0], '--', color = 'black', 
          zorder = len(lhs_lat_inflow) + 1, linewidth = 1)

ax4.errorbar(range(1999, 2020, 1), heads.iloc[:, 0], yerr = heads_std.iloc[:, 0], 
              fmt = 'none', ecolor = 'black', zorder = len(lhs_rech) + 1, 
              linewidth = 0.8)

ax4.set_xlabel('Years')
# ax4.set_ylabel('Head (m)')
ax4.locator_params(axis = 'x', nbins = 5)




ax4.plot(range(1999, 2020, 1), Cal_Heads.loc[:, S2_high_index_str], 
         color = 'gainsboro', linewidth = 1)
ax4.set_ylim(10, 35)

    
ax4.plot(range(1999, 2020, 1), Cal_Heads.loc[:, S2_high_index_str].mean(axis = 1),
         color = 'red', linewidth = 1)   


eval_fig.tight_layout()

eval_fig.savefig('./Figures/Fig5_Model_Evaluation.png', dpi = 300)

