# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 11:14:53 2021

@author: tomglose
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
from pathlib import Path
import matplotlib.ticker as ticker
import os

# Change directory to working folder <- be sure to change
working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Figures/').mkdir(parents = True, exist_ok = True)
#%% Data wrangling

# Read in LHS variables
lhs_lat_inflow = pd.read_csv('./Inputs/Proj_LHS_Lat_Inflow.csv')
lhs_lat_inflow.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs_lat_inflow['Run'] = lhs_lat_inflow['Run'] + 1

lhs_rech = pd.read_csv('./Inputs/Proj_LHS_Recharge.csv')
lhs_rech.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs_rech['Run'] = lhs_rech['Run'] + 1


dtw_file = ('./Validation/Year_to_Year_Heads.csv')
heads = pd.read_csv(dtw_file, usecols = ['Average'])


# Full heads 20% reduction both scenarios
fh_s1_lema_20 = pd.read_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_20.csv', 
                            index_col = [0], skiprows = list(range(0, 44, 1))) 
fh_s1_lema_20.drop(fh_s1_lema_20.columns[0], axis = 1, inplace = True)
fh_s1_lema_20.columns = lhs_lat_inflow.Run.tolist()
fh_s1_lema_20 = fh_s1_lema_20.mask(np.isclose(fh_s1_lema_20, -1E30))
fh_s1_lema_20.fillna(0, inplace = True)
fh_s1_lema_20['Year'] = range(1999, 2101, 1)
fh_s1_lema_20.set_index('Year', inplace = True)

fh_s1_lema_20_unmelt = fh_s1_lema_20

fh_s2_lema_20 = pd.read_csv('./Evaluation_Data/Projection/Rech/Accept_Full_Heads_20.csv', 
                            index_col = [0], skiprows = list(range(0, 44, 1))) 
fh_s2_lema_20.drop(fh_s2_lema_20.columns[0], axis = 1, inplace = True)
fh_s2_lema_20.columns = lhs_rech.Run.tolist()
fh_s2_lema_20 = fh_s2_lema_20.mask(np.isclose(fh_s2_lema_20, -1E30))
fh_s2_lema_20.fillna(0, inplace = True)
fh_s2_lema_20['Year'] = range(1999, 2101, 1)
fh_s2_lema_20.set_index('Year', inplace = True)

fh_s2_lema_20_unmelt = fh_s2_lema_20

# Full heads 30% reduction both scenarios
fh_s1_lema_30 = pd.read_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_30.csv', 
                            index_col = [0], skiprows = list(range(0, 44, 1))) 
fh_s1_lema_30.drop(fh_s1_lema_30.columns[0], axis = 1, inplace = True)
fh_s1_lema_30.columns = lhs_lat_inflow.Run.tolist()
fh_s1_lema_30 = fh_s1_lema_30.mask(np.isclose(fh_s1_lema_30, -1E30))
fh_s1_lema_30.fillna(0, inplace = True)
fh_s1_lema_30['Year'] = range(1999, 2101, 1)
fh_s1_lema_30.set_index('Year', inplace = True)

fh_s1_lema_30_unmelt = fh_s1_lema_30

fh_s2_lema_30 = pd.read_csv('./Evaluation_Data/Projection/Rech/Accept_Full_Heads_30.csv', 
                            index_col = [0], skiprows = list(range(0, 44, 1))) 
fh_s2_lema_30.drop(fh_s2_lema_30.columns[0], axis = 1, inplace = True)
fh_s2_lema_30.columns = lhs_rech.Run.tolist()
fh_s2_lema_30 = fh_s2_lema_30.mask(np.isclose(fh_s2_lema_30, -1E30))
fh_s2_lema_30.fillna(0, inplace = True)
fh_s2_lema_30['Year'] = range(1999, 2101, 1)
fh_s2_lema_30.set_index('Year', inplace = True)

fh_s2_lema_30_unmelt = fh_s2_lema_30

# Full heads no reduction both scenarios
fh_s1_no_lema = pd.read_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_30_No_Red.csv', 
                            index_col = [0], skiprows = list(range(0, 44, 1))) 
fh_s1_no_lema.drop(fh_s1_no_lema.columns[0], axis = 1, inplace = True)
fh_s1_no_lema.columns = lhs_lat_inflow.Run.tolist()
fh_s1_no_lema = fh_s1_no_lema.mask(np.isclose(fh_s1_no_lema, -1E30))
fh_s1_no_lema.fillna(0, inplace = True)
fh_s1_no_lema['Year'] = range(1999, 2101, 1)
fh_s1_no_lema.set_index('Year', inplace = True)

fh_s1_no_lema_unmelt = fh_s1_no_lema

fh_s2_no_lema = pd.read_csv('./Evaluation_Data/Projection/Rech/Accept_Full_Heads_30_No_Red.csv', 
                            index_col = [0], skiprows = list(range(0, 44, 1))) 
fh_s2_no_lema.drop(fh_s2_no_lema.columns[0], axis = 1, inplace = True)
fh_s2_no_lema.columns = lhs_rech.Run.tolist()
fh_s2_no_lema = fh_s2_no_lema.mask(np.isclose(fh_s2_no_lema, -1E30))
fh_s2_no_lema.fillna(0, inplace = True)
fh_s2_no_lema['Year'] = range(1999, 2101, 1)
fh_s2_no_lema.set_index('Year', inplace = True)

fh_s2_no_lema_unmelt = fh_s2_no_lema


# put data into long form
fh_s1_lema_20 =  fh_s1_lema_20.stack()
fh_s1_lema_20 = fh_s1_lema_20.reset_index()
fh_s1_lema_20.columns = ['Year', 'Run', 'Head']

fh_s1_lema_30 =  fh_s1_lema_30.stack()
fh_s1_lema_30 = fh_s1_lema_30.reset_index()
fh_s1_lema_30.columns = ['Year', 'Run', 'Head']

fh_s1_no_lema = fh_s1_no_lema.stack()
fh_s1_no_lema = fh_s1_no_lema.reset_index()
fh_s1_no_lema.columns = ['Year', 'Run', 'Head']

fh_s2_lema_20 =  fh_s2_lema_20.stack()
fh_s2_lema_20 = fh_s2_lema_20.reset_index()
fh_s2_lema_20.columns = ['Year', 'Run', 'Head']

fh_s2_lema_30 =  fh_s2_lema_30.stack()
fh_s2_lema_30 = fh_s2_lema_30.reset_index()
fh_s2_lema_30.columns = ['Year', 'Run', 'Head']

fh_s2_no_lema = fh_s2_no_lema.stack()
fh_s2_no_lema = fh_s2_no_lema.reset_index()
fh_s2_no_lema.columns = ['Year', 'Run', 'Head']

# grouping data and finding descrriptive stats
fh_s1_lema_20_stats = fh_s1_lema_20.groupby(['Year']).describe()
fh_s1_lema_30_stats = fh_s1_lema_30.groupby(['Year']).describe()
fh_s1_no_lema_stats = fh_s1_no_lema.groupby(['Year']).describe()

fh_s2_lema_20_stats = fh_s2_lema_20.groupby(['Year']).describe()
fh_s2_lema_30_stats = fh_s2_lema_30.groupby(['Year']).describe()
fh_s2_no_lema_stats = fh_s2_no_lema.groupby(['Year']).describe()


# putting data into plottable portions
med_s1_lema_20 = fh_s1_lema_20_stats[('Head', '50%')]
quart1_s1_lema_20 = fh_s1_lema_20_stats[('Head', '25%')]
quart3_s1_lema_20 = fh_s1_lema_20_stats[('Head', '75%')]

med_s1_lema_30 = fh_s1_lema_30_stats[('Head', '50%')]
quart1_s1_lema_30 = fh_s1_lema_30_stats[('Head', '25%')]
quart3_s1_lema_30 = fh_s1_lema_30_stats[('Head', '75%')]

med_s1_no_lema = fh_s1_no_lema_stats[('Head', '50%')]
quart1_s1_no_lema = fh_s1_no_lema_stats[('Head', '25%')]
quart3_s1_no_lema = fh_s1_no_lema_stats[('Head', '75%')]

med_s2_lema_20 = fh_s2_lema_20_stats[('Head', '50%')]
quart1_s2_lema_20 = fh_s2_lema_20_stats[('Head', '25%')]
quart3_s2_lema_20 = fh_s2_lema_20_stats[('Head', '75%')]

med_s2_lema_30 = fh_s2_lema_30_stats[('Head', '50%')]
quart1_s2_lema_30 = fh_s2_lema_30_stats[('Head', '25%')]
quart3_s2_lema_30 = fh_s2_lema_30_stats[('Head', '75%')]

med_s2_no_lema = fh_s2_no_lema_stats[('Head', '50%')]
quart1_s2_no_lema = fh_s2_no_lema_stats[('Head', '25%')]
quart3_s2_no_lema = fh_s2_no_lema_stats[('Head', '75%')]

# Organize data for barplot
res_ind_s1_lema_20 = []
res_ind_s1_lema_30 = []
res_ind_s1_no_lema = []

res_ind_s2_lema_20 = []
res_ind_s2_lema_30 = []
res_ind_s2_no_lema = []

for i in lhs_lat_inflow.Run.tolist():
    res_ind_s1_lema_20.append(fh_s1_lema_20_unmelt[i].sub(8).abs().idxmin())
    res_ind_s1_lema_30.append(fh_s1_lema_30_unmelt[i].sub(8).abs().idxmin())
    res_ind_s1_no_lema.append(fh_s1_no_lema_unmelt[i].sub(8).abs().idxmin())

for i in lhs_rech.Run.tolist():
    res_ind_s2_lema_20.append(fh_s2_lema_20_unmelt[i].sub(8).abs().idxmin())
    res_ind_s2_lema_30.append(fh_s2_lema_30_unmelt[i].sub(8).abs().idxmin())
    res_ind_s2_no_lema.append(fh_s2_no_lema_unmelt[i].sub(8).abs().idxmin())


ext_s1_20 = [x - y for x, y in zip(res_ind_s1_lema_20, res_ind_s1_no_lema)]
ext_s1_30 = [x - y for x, y in zip(res_ind_s1_lema_30, res_ind_s1_no_lema)]

ext_s2_20 = [x - y for x, y in zip(res_ind_s2_lema_20, res_ind_s2_no_lema)]
ext_s2_30 = [x - y for x, y in zip(res_ind_s2_lema_30, res_ind_s2_no_lema)]


labels_s1_20, counts_s1_20 = np.unique(ext_s1_20, return_counts = True)
labels_s1_30, counts_s1_30 = np.unique(ext_s1_30, return_counts = True)

labels_s2_20, counts_s2_20 = np.unique(ext_s2_20, return_counts = True)
labels_s2_30, counts_s2_30 = np.unique(ext_s2_30, return_counts = True)

med_ext_s1_20 = np.mean(ext_s1_20)
med_ext_s1_30 = np.mean(ext_s1_30)
med_ext_s2_20 = np.mean(ext_s2_20)
med_ext_s2_30 = np.mean(ext_s2_30)


#%% Generating linear trends to quantify extenision of usable lifetime assuming
#   lagged respones

s1_20_data = fh_s1_lema_20_stats.loc[2013:2020, ('Head', '50%')]
s1_30_data = fh_s1_lema_30_stats.loc[2013:2020, ('Head', '50%')]

s2_20_data = fh_s2_lema_20_stats.loc[2013:2022, ('Head', '50%')]
s2_30_data = fh_s2_lema_30_stats.loc[2013:2023, ('Head', '50%')]

s1_20_data = s1_20_data.to_numpy()
s1_30_data = s1_30_data.to_numpy()

s2_20_data = s2_20_data.to_numpy()
s2_30_data = s2_30_data.to_numpy()

s1_time = np.array(list(range(2013,2021,1)), dtype = 'float64')
s2_time_20 = np.array(list(range(2013,2023,1)), dtype = 'float64')
s2_time_30 = np.array(list(range(2013,2024,1)), dtype = 'float64')

s1_20_fit = np.polyfit(s1_time, s1_20_data, 1)
s1_30_fit = np.polyfit(s1_time, s1_30_data, 1)

s2_20_fit = np.polyfit(s2_time_20, s2_20_data, 1)
s2_30_fit = np.polyfit(s2_time_30, s2_30_data, 1)

dates = np.array(list(range(2013, 2101, 1)), dtype = 'float64') 

# Linear Trend for observed data
obs_heads = heads.loc[14:21]
obs_heads = obs_heads.to_numpy(dtype = 'float64')
obs_heads_time = np.array(list(range(2013, 2020, 1)), dtype = 'float64')
obs_heads_fit = np.polyfit(obs_heads_time, obs_heads, 1)

#%% Figure w/ IQR
mm = 1/25.4

sns.set_style('ticks')
colors = sns.color_palette('colorblind')

x = fh_s1_lema_20_stats.index
extend_plot = plt.figure(figsize = (190*mm, 230*mm))
gs = extend_plot.add_gridspec(4,2)
ax1 = extend_plot.add_subplot(gs[0:2, 0])

ax1.plot(range(1999, 2020, 1), heads.iloc[:, 0], 'o', color = 'k', 
         markerfacecolor = 'none', markersize = 4, zorder = 10)


ax1 = sns.lineplot(x, med_s1_no_lema, color = colors[7]) 
ax1.fill_between(x, quart1_s1_no_lema, quart3_s1_no_lema, alpha=0.2, color = colors[7])

ax1 = sns.lineplot(x, med_s1_lema_20, color = colors[0]) 
ax1.fill_between(x, quart1_s1_lema_20, quart3_s1_lema_20, alpha=0.2, color = colors[0])

ax1 = sns.lineplot(x, med_s1_lema_30, color = colors[3]) 
ax1.fill_between(x, quart1_s1_lema_30, quart3_s1_lema_30, alpha=0.2, color = colors[3])


ax1.plot(dates, s1_20_fit[0]*dates+s1_20_fit[1], '--', color = colors[0], 
         alpha = 0.5)
ax1.plot(dates, s1_30_fit[0]*dates+s1_30_fit[1], '--', color = colors[3], 
         alpha = 0.5)

ax1.plot(dates, obs_heads_fit[0]*dates+obs_heads_fit[1], '--', color = 'k', 
         alpha = 0.5)


ax1.hlines(8, 1999, 2110, linestyle = 'dotted', color = 'k') 
ax1.set_xlim(1999, 2080)
ax1.set_ylim(7.5, 35)

ax1.set_xlabel('Year', fontsize = 8)
ax1.set_ylabel('Remaining Saturated Thickness (m)', fontsize = 8)
plt.tick_params(axis='both', which='major', labelsize = 8)


ax1.legend(labels = ['Observed Heads', 'No Pumping Reduction','20% Pumping Reduction', 
                     '30% Pumping Reduction', '_nolegend_', '_nolegend', 
                     'Extrapolation if Lagged \n Processes Ignored'], 
           loc = 'best', prop={'size': 6}, markerscale = 0.75)

ax2 = extend_plot.add_subplot(gs[0:2, 1])
ax2.plot(range(1999, 2020, 1), heads.iloc[:, 0], 'o', color = 'k', 
         markerfacecolor = 'none', markersize = 4, zorder = 10)


ax2 = sns.lineplot(x, med_s2_no_lema, color = colors[7]) 
ax2.fill_between(x, quart1_s2_no_lema, quart3_s2_no_lema, alpha=0.2, color = colors[7])

ax2 = sns.lineplot(x, med_s2_lema_20, color = colors[0]) 
ax2.fill_between(x, quart1_s2_lema_20, quart3_s2_lema_20, alpha=0.2, color = colors[0])

ax2 = sns.lineplot(x, med_s2_lema_30, color = colors[3]) 
ax2.fill_between(x, quart1_s2_lema_30, quart3_s2_lema_30, alpha=0.2, color = colors[3])

ax2.plot(dates, s2_20_fit[0]*dates+s2_20_fit[1], '--', color = colors[0], 
         alpha = 0.5)
ax2.plot(dates, s2_30_fit[0]*dates+s2_30_fit[1], '--', color = colors[3], 
         alpha = 0.5)

ax2.plot(dates, obs_heads_fit[0]*dates+obs_heads_fit[1], '--', color = 'k', 
         alpha = 0.5)


ax2.hlines(8, 1999, 2110, linestyle = 'dotted', color = 'k') 
ax2.set_xlim(1999, 2080)
ax2.set_ylim(7.5, 35)

ax2.set_xlabel('Year', fontsize = 8)
ax2.set_ylabel('Remaining Saturated Thickness (m)', fontsize = 8)
plt.tick_params(axis='both', which='major', labelsize = 8)


ax2.legend(labels = ['Observed Heads', 'No Pumping Reduction','20% Pumping Reduction', 
                     '30% Pumping Reduction', '_nolegend_', '_nolegend', 
                     'Extrapolation if Lagged \n Processes Ignored'], 
           loc = 'best', prop={'size': 6}, markerscale = 0.75)


ax3 = extend_plot.add_subplot(gs[2,0])

for axis in [ax3.xaxis, ax3.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))

ax3.bar(labels_s1_20, counts_s1_20, align = 'center', width = 0.8,
        label = '20% Pumping Reduction', color = colors[0])

ax3.vlines(np.median(ext_s1_20), 0, 100, linestyle = 'dotted', color = 'k')

ax3.set_xlim(0, 45)
ax3.set_ylim(0, np.max(counts_s1_20) + 0.25)

ax3.set_ylabel('Count', fontsize = 8)
plt.tick_params(axis='both', which='major', labelsize = 8)

ax3.legend(loc = 'best', prop={'size': 6}, markerscale = 0.5)


ax4 = extend_plot.add_subplot(gs[3,0])

for axis in [ax4.xaxis, ax4.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))

ax4.bar(labels_s1_30, counts_s1_30, align = 'center', width = 0.8,
        label = '30% Pumping Reduction', color = colors[3])

ax4.vlines(np.median(ext_s1_30), 0, 100, linestyle = 'dotted', color = 'k') 

ax4.set_xlim(0, 45)
ax4.set_ylim(0, np.max(counts_s1_30) + 0.25)


ax4.set_xlabel('Extension of Useable Aquifer Lifetime (yrs)', fontsize = 8)
ax4.set_ylabel('Count', fontsize = 8)
plt.tick_params(axis='both', which='major', labelsize = 8)

ax4.legend(loc = 'best', prop={'size': 6}, markerscale = 0.5)


ax5 = extend_plot.add_subplot(gs[2,1])

for axis in [ax5.xaxis, ax5.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))

ax5.bar(labels_s2_20, counts_s2_20, align = 'center', width = 0.8,
        label = '20% Pumping Reduction', color = colors[0])

ax5.vlines(np.median(ext_s2_20), 0, 100, linestyle = 'dotted', color = 'k')

ax5.set_xlim(0, 45)
ax5.set_ylim(0, np.max(counts_s2_20) + 0.25)

ax5.set_ylabel('Count', fontsize = 8)
plt.tick_params(axis='both', which='major', labelsize = 8)

ax5.legend(loc = 'best', prop={'size': 6}, markerscale = 0.5)


ax6 = extend_plot.add_subplot(gs[3,1])

for axis in [ax6.xaxis, ax6.yaxis]:
    axis.set_major_locator(ticker.MaxNLocator(integer=True))

ax6.bar(labels_s2_30, counts_s2_30, align = 'center', width = 0.8,
        label = '30% Pumping Reduction', color = colors[3])

ax6.vlines(np.median(ext_s2_30), 0, 100, linestyle = 'dotted', color = 'k') 

ax6.set_xlim(0, 45)
ax6.set_ylim(0, np.max(counts_s2_30) + 0.25)


ax6.set_xlabel('Extension of Useable Aquifer Lifetime (yrs)', fontsize = 8)
ax6.set_ylabel('Count', fontsize = 8)
plt.tick_params(axis='both', which='major', labelsize = 8)

ax6.legend(loc = 'best', prop={'size': 6}, markerscale = 0.5)


extend_plot.tight_layout()

extend_plot.savefig('./Figures/All_Q_Scenarios_Heads_IQR_Plot.png', dpi = 300)


