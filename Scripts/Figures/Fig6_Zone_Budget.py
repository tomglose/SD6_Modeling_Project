# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 09:36:44 2020

@author: tomglose
"""

import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
import os
from pathlib import Path


# Change directory to working folder <- be sure to change
working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Figures/').mkdir(parents = True, exist_ok = True)
# Read in LHS variables

lhs_lat_inflow = pd.read_csv('./Inputs/Proj_LHS_Lat_Inflow.csv')
lhs_lat_inflow.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs_lat_inflow['Run'] = lhs_lat_inflow['Run'] + 1

lhs_rech = pd.read_csv('./Inputs/Proj_LHS_Recharge.csv')
lhs_rech.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs_rech['Run'] = lhs_rech['Run'] + 1

dates = pd.date_range(start = '10-01-1899', end = '05-25-2100')
dates = dates[~((dates.month == 2) & (dates.day == 29))]

#%% ZoneBudger for scenario 1
z2_z1_s1 = pd.DataFrame(data = [0])
z2_z3_s1 = pd.DataFrame(data = [0])


z2_rec_s1 = pd.DataFrame(data = [0])
z2_rec_no_red_s1 = pd.DataFrame(data = [0])


for i in range(0, len(lhs_lat_inflow), 1):
    
    zon1 = pd.read_csv('./Outputs/Zone_Budgets/LI/30_Percent/'
                       'Zon1_Run_%s.csv' % (lhs_lat_inflow.Run[i]))
    
    zon2 = pd.read_csv('./Outputs/Zone_Budgets/LI/30_Percent/'
                       'Zon2_Run_%s.csv' % (lhs_lat_inflow.Run[i]))
    
    zon3 = pd.read_csv('./Outputs/Zone_Budgets/LI/30_Percent/'
                       'Zon3_Run_%s.csv' % (lhs_lat_inflow.Run[i]))
    
    zon2_no_red = pd.read_csv('./Outputs/Zone_Budgets/LI_No_Red/30_Percent/' 
                              'Zon2_Run_%s.csv' 
                              % (lhs_lat_inflow.Run[i]))
    
    
    z2_z1_s1 = pd.concat([z2_z1_s1, zon1['FROM_ZONE_2']], axis = 1)
    z2_z3_s1 = pd.concat([z2_z3_s1, zon3['FROM_ZONE_2']], axis = 1)
    
    z2_rec_no_red_s1 = pd.concat([z2_rec_no_red_s1, zon1['FROM_UZF_RECHARGE']], axis = 1)
    z2_rec_s1 = pd.concat([z2_rec_s1, zon2['FROM_UZF_RECHARGE']], axis = 1)
    


z2_z1_s1.drop([0], axis = 1, inplace = True)
z2_z3_s1.drop([0], axis = 1, inplace = True)

z2_rec_no_red_s1.drop([0], axis = 1, inplace = True)
z2_rec_s1.drop([0], axis = 1, inplace = True)


dates = pd.date_range(start = '10-01-1899', end = '05-1-2100', freq = 'MS')
# dates = dates[~((dates.month == 2) & (dates.day == 29))]

z2_z1_s1.set_index(dates, inplace = True)
z2_z3_s1.set_index(dates, inplace = True)

z2_rec_no_red_s1.set_index(dates, inplace = True)
z2_rec_s1.set_index(dates, inplace = True)


z2_z1_s1 = z2_z1_s1.resample('D').mean()
z2_z3_s1 = z2_z3_s1.resample('D').mean()

z2_rec_no_red_s1 = z2_rec_no_red_s1.resample('D').mean()
z2_rec_s1 = z2_rec_s1.resample('D').mean()


z2_z1_s1 = z2_z1_s1.interpolate()
z2_z3_s1 = z2_z3_s1.interpolate()

z2_rec_no_red_s1 = z2_rec_no_red_s1.interpolate()
z2_rec_s1 = z2_rec_s1.interpolate()


z2_z1_s1 = z2_z1_s1.resample('A').sum()
z2_z3_s1 = z2_z3_s1.resample('A').sum()

z2_rec_no_red_s1 = z2_rec_no_red_s1.resample('A').sum()
z2_rec_s1 = z2_rec_s1.resample('A').sum()

z2_z1_s1['Years'] = range(1899, 2101, 1)
z2_z3_s1['Years'] = range(1899, 2101, 1)

z2_rec_no_red_s1['Years'] = range(1899, 2101, 1)
z2_rec_s1['Years'] = range(1899, 2101, 1)


z2_z1_s1.set_index('Years', inplace = True)
z2_z3_s1.set_index('Years', inplace = True)

z2_rec_no_red_s1.set_index('Years', inplace = True)
z2_rec_s1.set_index('Years', inplace = True)


z2_z1_s1 = z2_z1_s1.divide(800*800*7).multiply(1000)
z2_z3_s1 = z2_z3_s1.divide(800*800*7).multiply(1000)
z2_outs_s1 = z2_z1_s1 + z2_z3_s1

z2_rec_no_red_s1 = z2_rec_no_red_s1.divide(800*800*14).multiply(1000)
z2_rec_s1 = z2_rec_s1.divide(800*800*14).multiply(1000)
z2_z2_no_red_s1_rec = z2_rec_s1 - z2_rec_no_red_s1


z2_z1_s1.columns = lhs_lat_inflow.Run
z2_z3_s1.columns = lhs_lat_inflow.Run
z2_outs_s1.columns = lhs_lat_inflow.Run

z2_rec_no_red_s1.columns = lhs_lat_inflow.Run
z2_rec_s1.columns = lhs_lat_inflow.Run
z2_z2_no_red_s1_rec.columns = lhs_lat_inflow.Run


z2_z1_s1 =  z2_z1_s1.stack()
z2_z1_s1 = z2_z1_s1.reset_index()
z2_z1_s1.columns = ['Year', 'Run', 'Flow Rate']

z2_z3_s1 =  z2_z3_s1.stack()
z2_z3_s1 = z2_z3_s1.reset_index()
z2_z3_s1.columns = ['Year', 'Run', 'Flow Rate']

z2_outs_s1 =  z2_outs_s1.stack()
z2_outs_s1 = z2_outs_s1.reset_index()
z2_outs_s1.columns = ['Year', 'Run', 'Flow Rate']


z2_rec_no_red_s1 = z2_rec_no_red_s1.stack()
z2_rec_s1 = z2_rec_s1.stack()
z2_z2_no_red_s1_rec = z2_z2_no_red_s1_rec.stack()

z2_rec_no_red_s1 = z2_rec_no_red_s1.reset_index()
z2_rec_s1 = z2_rec_s1.reset_index()
z2_z2_no_red_s1_rec = z2_z2_no_red_s1_rec.reset_index()

z2_rec_no_red_s1.columns = ['Year', 'Run', 'Flow Rate']
z2_rec_s1.columns = ['Year', 'Run', 'Flow Rate']
z2_z2_no_red_s1_rec.columns = ['Year', 'Run', 'Flow Rate']


# Convert to dataframe statistics
z2_outs_s1_stats = z2_outs_s1.groupby(['Year']).describe()
z2_z2_no_red_s1_rec_stats = z2_z2_no_red_s1_rec.groupby(['Year']).describe()

med_s1_z2_outs = z2_outs_s1_stats[('Flow Rate', '50%')]
quart1_s1_z2_outs = z2_outs_s1_stats[('Flow Rate', '25%')]
quart3_s1_z2_outs = z2_outs_s1_stats[('Flow Rate', '75%')]

med_s1_z2_z2_no_red = z2_z2_no_red_s1_rec_stats[('Flow Rate', '50%')]
quart1_s1_z2_z2_no_red = z2_z2_no_red_s1_rec_stats[('Flow Rate', '25%')]
quart3_s1_z2_z2_no_red = z2_z2_no_red_s1_rec_stats[('Flow Rate', '75%')]

#%% ZoneBudget for scenario 2
z2_z1_s2 = pd.DataFrame(data = [0])
z2_z3_s2 = pd.DataFrame(data = [0])

z2_rec_s2 = pd.DataFrame(data = [0])
z2_rec_no_red_s2 = pd.DataFrame(data = [0])

for i in range(0, len(lhs_rech), 1):
    
    zon1 = pd.read_csv('./Outputs/Zone_Budgets/Recharge/30_Percent/'
                       'Zon1_Run_%s.csv' % (lhs_lat_inflow.Run[i]))
    
    zon2 = pd.read_csv('./Outputs/Zone_Budgets/Recharge/30_Percent/'
                       'Zon2_Run_%s.csv' % (lhs_lat_inflow.Run[i]))
    
    zon3 = pd.read_csv('./Outputs/Zone_Budgets/Recharge/30_Percent/'
                       'Zon3_Run_%s.csv' % (lhs_lat_inflow.Run[i]))
    
    zon2_no_red = pd.read_csv('./Outputs/Zone_Budgets/Recharge_No_Red/' 
                              'Zon2_Run_%s.csv' 
                              % (lhs_lat_inflow.Run[i]))
    
    
    z2_z1_s2 = pd.concat([z2_z1_s2, zon1['FROM_ZONE_2']], axis = 1)
    z2_z3_s2 = pd.concat([z2_z3_s2, zon3['FROM_ZONE_2']], axis = 1)
    
    z2_rec_no_red_s2 = pd.concat([z2_rec_no_red_s2, zon1['FROM_UZF_RECHARGE']], axis = 1)
    z2_rec_s2 = pd.concat([z2_rec_s2, zon2['FROM_UZF_RECHARGE']], axis = 1)
    


z2_z1_s2.drop([0], axis = 1, inplace = True)
z2_z3_s2.drop([0], axis = 1, inplace = True)

z2_rec_s2.drop([0], axis = 1, inplace = True)
z2_rec_no_red_s2.drop([0], axis = 1, inplace = True)

dates = pd.date_range(start = '10-01-1899', end = '05-1-2100', freq = 'MS')
# dates = dates[~((dates.month == 2) & (dates.day == 29))]

z2_z1_s2.set_index(dates, inplace = True)
z2_z3_s2.set_index(dates, inplace = True)

z2_rec_s2.set_index(dates, inplace = True)
z2_rec_no_red_s2.set_index(dates, inplace = True)

z2_z1_s2 = z2_z1_s2.resample('D').mean()
z2_z3_s2 = z2_z3_s2.resample('D').mean()

z2_rec_s2 = z2_rec_s2.resample('D').mean()
z2_rec_no_red_s2 = z2_rec_no_red_s2.resample('D').mean()

z2_z1_s2 = z2_z1_s2.interpolate()
z2_z3_s2 = z2_z3_s2.interpolate()

z2_rec_s2 = z2_rec_s2.interpolate()
z2_rec_no_red_s2 = z2_rec_no_red_s2.interpolate()

z2_z1_s2 = z2_z1_s2.resample('A').sum()
z2_z3_s2 = z2_z3_s2.resample('A').sum()

z2_rec_s2 = z2_rec_s2.resample('A').sum()
z2_rec_no_red_s2 = z2_rec_no_red_s2.resample('A').sum()

z2_z1_s2['Years'] = range(1899, 2101, 1)
z2_z3_s2['Years'] = range(1899, 2101, 1)

z2_rec_s2['Years'] = range(1899, 2101, 1)
z2_rec_no_red_s2['Years'] = range(1899, 2101, 1)

z2_z1_s2.set_index('Years', inplace = True)
z2_z3_s2.set_index('Years', inplace = True)

z2_rec_s2.set_index('Years', inplace = True)
z2_rec_no_red_s2.set_index('Years', inplace = True)

z2_z1_s2 = z2_z1_s2.divide(800*800*7).multiply(1000)
z2_z3_s2 = z2_z3_s2.divide(800*800*7).multiply(1000)
z2_outs_s2 = z2_z1_s2 + z2_z3_s2

z2_rec_no_red_s2 = z2_rec_no_red_s2.divide(800*800*14).multiply(1000)
z2_rec_s2 = z2_rec_s2.divide(800*800*14).multiply(1000)
z2_z2_no_red_s2_rec = z2_rec_s2 - z2_rec_no_red_s2


z2_z1_s2.columns = lhs_rech.Run
z2_z3_s2.columns = lhs_rech.Run
z2_outs_s2.columns = lhs_rech.Run

z2_rec_s2.columns = lhs_rech.Run
z2_rec_no_red_s2.columns = lhs_rech.Run
z2_z2_no_red_s2_rec.columns = lhs_rech.Run


z2_z1_s2 =  z2_z1_s2.stack()
z2_z1_s2 = z2_z1_s2.reset_index()
z2_z1_s2.columns = ['Year', 'Run', 'Flow Rate']

z2_z3_s2 =  z2_z3_s2.stack()
z2_z3_s2 = z2_z3_s2.reset_index()
z2_z3_s2.columns = ['Year', 'Run', 'Flow Rate']

z2_outs_s2 =  z2_outs_s2.stack()
z2_outs_s2 = z2_outs_s2.reset_index()
z2_outs_s2.columns = ['Year', 'Run', 'Flow Rate']


z2_rec_no_red_s2 = z2_rec_no_red_s2.stack()
z2_rec_s2 = z2_rec_s2.stack()
z2_z2_no_red_s2_rec = z2_z2_no_red_s2_rec.stack()

z2_rec_no_red_s2 = z2_rec_no_red_s2.reset_index()
z2_rec_s2 = z2_rec_s2.reset_index()
z2_z2_no_red_s2_rec = z2_z2_no_red_s2_rec.reset_index()

z2_rec_no_red_s2.columns = ['Year', 'Run', 'Flow Rate']
z2_rec_s2.columns = ['Year', 'Run', 'Flow Rate']
z2_z2_no_red_s2_rec.columns = ['Year', 'Run', 'Flow Rate']

# Convert to dataframe statistics
z2_outs_s2_stats = z2_outs_s2.groupby(['Year']).describe()
z2_z2_no_red_s2_rec_stats = z2_z2_no_red_s2_rec.groupby(['Year']).describe()

med_s2_z2_outs = z2_outs_s2_stats[('Flow Rate', '50%')]
quart1_s2_z2_outs = z2_outs_s2_stats[('Flow Rate', '25%')]
quart3_s2_z2_outs = z2_outs_s2_stats[('Flow Rate', '75%')]

med_s2_z2_z2_no_red = z2_z2_no_red_s2_rec_stats[('Flow Rate', '50%')]
quart1_s2_z2_z2_no_red = z2_z2_no_red_s2_rec_stats[('Flow Rate', '25%')]
quart3_s2_z2_z2_no_red = z2_z2_no_red_s2_rec_stats[('Flow Rate', '75%')]

#%% ZoneBudget Plots
mm = 1/25.4

sns.set_style('ticks')
colors = sns.color_palette('colorblind')

x = z2_outs_s1_stats.index


zonbud = plt.figure(figsize = (190*mm, 115*mm))
gs = zonbud.add_gridspec(2, 2)


# scenario 1 plots
ax1 = zonbud.add_subplot(gs[0,0])
ax1.set_ylabel('Lateral Flow Out of \n Conservation Area (mm yr$^{-1}$)', fontsize = 8)
ax1.set_xlabel('Year', fontsize = 8)
ax1.set_title('Lateral-Flow-Dominated', fontsize = 16)
ax1.set_xlim(2012, 2100)
ax1.set_ylim(0, 50)

ax1 = sns.lineplot(x, y = med_s1_z2_outs, color = colors[7])
ax1.fill_between(x, quart1_s1_z2_outs, quart3_s1_z2_outs, alpha=0.2, color = colors[7])

plt.tick_params(axis='both', which='major', labelsize = 8)

ax2 = zonbud.add_subplot(gs[1,0])
ax2.set_ylabel('Difference in Recharge Rate (mm yr$^{-1}$)', fontsize = 8)
ax2.set_xlabel('Year', fontsize = 8)
ax2.set_xlim(2012, 2100)
ax2.set_ylim(-60, 20)

ax2 = sns.lineplot(x, med_s1_z2_z2_no_red, color = colors[0])
ax2.fill_between(x, quart1_s1_z2_z2_no_red, quart3_s1_z2_z2_no_red, alpha=0.2, color = colors[0])
ax2.hlines(0, 2013, 2100, color = 'k', linestyles = '--', alpha = 0.5)

plt.tick_params(axis='both', which='major', labelsize = 8)


# scenario 2 plots
ax3 = zonbud.add_subplot(gs[0,1], sharey = ax1)
plt.setp(ax3.get_yticklabels(), visible=False)
# ax3.set_ylabel('Flow from Conservation Area (mm yr$^{-1}$)', fontsize = 8)
ax3.set_title('Recharge-Dominated', fontsize = 16)
ax3.set_xlabel('Year', fontsize = 8)
ax3.set_xlim(2012, 2100)
ax3.set_ylim(0, 50)

ax3 = sns.lineplot(x, y = med_s2_z2_outs, color = colors[7])
ax3.fill_between(x, quart1_s2_z2_outs, quart3_s2_z2_outs, alpha=0.2, color = colors[7])

plt.tick_params(axis='both', which='major', labelsize = 8)

ax4 = zonbud.add_subplot(gs[1,1], sharey = ax2)
plt.setp(ax4.get_yticklabels(), visible=False)
# ax4.set_ylabel('Difference in Recharge Rate (mm $^{-1}$)', fontsize = 8)
ax4.set_xlabel('Year', fontsize = 8)
ax4.set_xlim(2012, 2100)
ax4.set_ylim(-60, 20)

ax4 = sns.lineplot(x, med_s2_z2_z2_no_red, color = colors[0])
ax4.fill_between(x, quart1_s2_z2_z2_no_red, quart3_s2_z2_z2_no_red, alpha=0.2, color = colors[0])
ax4.hlines(0, 2013, 2100, color = 'k', linestyles = '--', alpha = 0.5)


zonbud.tight_layout()
plt.tick_params(axis='both', which='major', labelsize = 8)

zonbud.savefig('./Figures/Fig6_ZoneBudget_IQR.png', dpi = 300)

#%%

colors = sns.color_palette('tab10')

z2_rec_no_red_s1_stats = z2_rec_no_red_s1.groupby(['Year']).describe()
z2_rec_s1_stats = z2_rec_s1.groupby(['Year']).describe()

z2_rec_no_red_s2_stats = z2_rec_no_red_s2.groupby(['Year']).describe()
z2_rec_s2_stats = z2_rec_s2.groupby(['Year']).describe()

med_z2_rec_no_red_s1 = z2_rec_no_red_s1_stats[('Flow Rate', '50%')]
quart1_z2_rec_no_red_s1 = z2_rec_no_red_s1_stats[('Flow Rate', '25%')]
quart3_z2_rec_no_red_s1 = z2_rec_no_red_s1_stats[('Flow Rate', '75%')]

med_z2_rec_s1 = z2_rec_s1_stats[('Flow Rate', '50%')]
quart1_z2_rec_s1 = z2_rec_s1_stats[('Flow Rate', '25%')]
quart3_z2_rec_s1 = z2_rec_s1_stats[('Flow Rate', '75%')]


med_z2_rec_no_red_s2 = z2_rec_no_red_s2_stats[('Flow Rate', '50%')]
quart1_z2_rec_no_red_s2 = z2_rec_no_red_s2_stats[('Flow Rate', '25%')]
quart3_z2_rec_no_red_s2 = z2_rec_no_red_s2_stats[('Flow Rate', '75%')]

med_z2_rec_s2 = z2_rec_s2_stats[('Flow Rate', '50%')]
quart1_z2_rec_s2 = z2_rec_s2_stats[('Flow Rate', '25%')]
quart3_z2_rec_s2 = z2_rec_s2_stats[('Flow Rate', '75%')]


## Recharge rates for reduction and non-reduction scenarios in Z2
rec_rates = plt.figure(figsize = (95*mm, 115*mm))
gs = rec_rates.add_gridspec(1,1)

ax1 = rec_rates.add_subplot(gs[0,0])


ax1 = sns.lineplot(x, med_z2_rec_no_red_s2, color = colors[0])
ax1.fill_between(x, quart1_z2_rec_no_red_s2, quart3_z2_rec_no_red_s2, alpha=0.2, color = colors[0])

ax1 = sns.lineplot(x, med_z2_rec_s2, color = colors[3])
ax1.fill_between(x, quart1_z2_rec_s2, quart3_z2_rec_s2, alpha=0.2, color = colors[3])

ax1 = sns.lineplot(x, (med_z2_rec_no_red_s2 - med_z2_rec_s2))



ax1.set_xlim(2010, 2018)
ax1.set_ylim(-10, 5)


