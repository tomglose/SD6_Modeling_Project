# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:51:44 2020

@author: tomglose
"""

# Script for rates through time #

import numpy as np
from scipy import stats
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import os


# Change directory to working folder <- be sure to change
working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

# Read in SD-6 data for PPT relationship data
year = pd.read_csv('./Inputs/PPT_Relationship_Data.csv', 
                   usecols = ['Year'])

precip = pd.read_csv('./Inputs/PPT_Relationship_Data.csv', 
                   usecols = ['PPT Ann (mm)'])

pumping = pd.read_csv('./Inputs/PPT_Relationship_Data.csv', 
                   usecols = ['Q Ann (mm)'])

bau_irr_ppt = pd.read_csv('./Inputs/PPT_Relationship_Data.csv', 
                   usecols = ['Ann BAU Irr + PPT (mm)'])
  
lema_irr_ppt = pd.read_csv('./Inputs/PPT_Relationship_Data.csv', 
                   usecols = ['Ann LEMA Irr + PPT (mm)']) 

bau_dp = pd.read_csv('./Inputs/PPT_Relationship_Data.csv', 
                   usecols = ['Ann BAU DP (mm)'])
  
lema_dp = pd.read_csv('./Inputs/PPT_Relationship_Data.csv', 
                   usecols = ['Ann LEMA DP (mm)'])       

# Split years into pre-conservation and post_conservation  
year = year.values.tolist()

pre_con_dp = year[8:13]
post_con_dp = year[13:] 

# pre_LEMA Data
q_no_con = np.asarray(pumping)
q_no_con[13:] = q_no_con[13:]/0.73 

q_no_con= np.reshape(q_no_con, 19, order = 'F' )

q_20 = q_no_con*0.8
q_20 = np.reshape(q_20, 19, order = 'F' )

q_30 = q_no_con*0.7
q_30 = np.reshape(q_30, 19, order = 'F' )

precip = np.asarray(precip)
precip = np.reshape(precip, 19, order = 'F' )

precip, q_no_con, q_20, q_30 = [np.asarray(a) for a in zip(*sorted(zip(precip, q_no_con, q_20, q_30)))]

# Linear Regression for no conservation
m_nc_qppt, b_nc_qppt, r_nc_qppt, p_nc_qppt, std_err_nc_qppt = stats.linregress(precip, q_no_con)
r_2_nc_qppt = r_nc_qppt**2

# Linear Regression for 20% pumping reduction
m_20_qppt, b_20_qppt, r_20_qppt, p_20_qppt, std_err_20_qppt = stats.linregress(precip, q_20)
r_2_20_qppt = r_20_qppt**2

# Linear Regression for 30% pumping reduction
m_30_qppt, b_30_qppt, r_30_qppt, p_30_qppt, std_err_30_qppt = stats.linregress(precip, q_30)
r_2_30_qppt = r_30_qppt**2

lin_reg_no_con = m_nc_qppt*precip + b_nc_qppt
lin_reg_20 = m_20_qppt*precip + b_20_qppt
lin_reg_30 = m_30_qppt*precip + b_30_qppt


# Deep Percolation Data
dp_bau = np.asarray(bau_dp[8:18])
dp_bau = np.asarray(dp_bau)

dp_lema = np.asarray(lema_dp[13:18])
dp_lema = np.asarray(dp_lema)

dp_bau = np.reshape(dp_bau, 10, order = 'F')
dp_lema = np.reshape(dp_lema, 5, order = 'F')

dp_total = np.append(dp_bau, dp_lema)

bau_sum_irr_ppt = np.asarray(bau_irr_ppt[8:18])
lema_sum_irr_ppt = np.asarray(lema_irr_ppt[13:18])

bau_sum_irr_ppt = np.reshape(bau_sum_irr_ppt, 10, order = 'F')
lema_sum_irr_ppt = np.reshape(lema_sum_irr_ppt, 5, order = 'F')

irr_ppt_total = np.append(bau_sum_irr_ppt, lema_sum_irr_ppt)

irr_ppt_total, dp_total = [np.asarray(a) for a in zip(*sorted(zip(irr_ppt_total, dp_total)))]

# Linear regression for deep percolation relationship
m_dpppt, b_dpppt, r_dpppt, p_dpppt, std_err_dpppt = stats.linregress(irr_ppt_total, dp_total)
r_2_dpppt = r_dpppt**2

lin_reg_dp = m_dpppt*irr_ppt_total + b_dpppt


# Read in each .csv file for plotting
q_no_full = pd.read_csv('./Inputs/Proj_PumpingRates_20.csv', usecols = ['BAU Pumping Rate'])
q_20_full = pd.read_csv('./Inputs/Proj_PumpingRates_20.csv', usecols = ['LEMA Pumping Rate'])
q_30_full = pd.read_csv('./Inputs/Proj_PumpingRates_30.csv', usecols = ['LEMA Pumping Rate'])

dp_no_full = pd.read_csv('./Inputs/Proj_DeepPerc_20.csv', usecols = ['DP BAU'])
dp_20_full = pd.read_csv('./Inputs/Proj_DeepPerc_20.csv', usecols = ['DP LEMA'])
dp_30_full = pd.read_csv('./Inputs/Proj_DeepPerc_30.csv', usecols = ['DP LEMA'])


q_no_full = q_no_full.divide(-800*800).multiply(1000*103)
q_20_full = q_20_full.divide(-800*800).multiply(1000*103)
q_30_full = q_30_full.divide(-800*800).multiply(1000*103)

dp_no_full = dp_no_full.multiply(1000*103)
dp_20_full = dp_20_full.multiply(1000*103)
dp_30_full = dp_30_full.multiply(1000*103)

dp_no_full.replace(to_replace = [0, 1.03], value = np.nan, inplace = True)
dp_20_full.replace(to_replace = [0, 1.03], value = np.nan, inplace = True)
dp_30_full.replace(to_replace = [0, 1.03], value = np.nan, inplace = True)

dp_no_full.dropna(how = 'any', inplace = True)
dp_no_full.reset_index(drop = True, inplace = True)

dp_20_full.dropna(how = 'any', inplace = True)
dp_20_full.reset_index(drop = True, inplace = True)

dp_30_full.dropna(how = 'any', inplace = True)
dp_30_full.reset_index(drop = True, inplace = True)

dp_no_full.replace(to_replace = [1E-9], value = 0, inplace = True)
dp_20_full.replace(to_replace = [1E-9], value = 0, inplace = True)
dp_30_full.replace(to_replace = [1E-9], value = 0, inplace = True)


#%%
# Figure creation
mm = 1/25.4
sns.set_style('ticks')
colors = sns.color_palette('colorblind')

# Annual pumping depth vs annual precipitation
q_vs_ppt = plt.figure(figsize = (95*mm, 85*mm))

gs = q_vs_ppt.add_gridspec(1,1)

ax1 = q_vs_ppt.add_subplot(gs[0, 0])

ax1.plot(precip, q_no_con, 'o', markersize = 5,
         color = colors[7], label = 'No Conservation', zorder = 0)

ax1.plot(precip, q_20, 's', markersize = 5,
         color = colors[0], label = '20% Pumping Reduction', zorder = 1)

ax1.plot(precip, q_30, 'd', markersize = 5,
         color = colors[3], label = '30% Pumping Reduction', zorder = 2)


ax1.plot(precip, lin_reg_no_con, '--', color = colors[7], 
         label='y = {:.3}x + {:.2f}'.format(m_nc_qppt,b_nc_qppt), zorder = 0)

ax1.plot(precip, lin_reg_20, '--', color = colors[0],
         label='y = {:.3}x + {:.2f}'.format(m_20_qppt,b_20_qppt), zorder = 0)

ax1.plot(precip, lin_reg_30, '--', color = colors[3],
         label='y = {:.3}x + {:.2f}'.format(m_30_qppt,b_30_qppt), zorder = 0)


ax1.set_xlabel('Annual Precipitation (mm)', fontsize = 8)
ax1.set_ylabel('Annual Pumping (mm)', fontsize = 8)
plt.tick_params(axis='both', which='major', labelsize = 8)
ax1.legend(loc = 'best', prop = {'size': 6, }, markerscale = 0.75)
q_vs_ppt.tight_layout()

q_vs_ppt.savefig('./Figures/Fig3_Q_vs_PPT.png', dpi = 300)

# Annual deep percolation depth vs (Annual precip + annunal irrigation depth)
dp_vs_ppt = plt.figure(figsize = (95*mm, 85*mm))
gs = dp_vs_ppt.add_gridspec(1,1)

ax1 = dp_vs_ppt.add_subplot(gs[0, 0])

ax1.plot(bau_sum_irr_ppt, dp_bau, 'o', color = colors[7], markersize = 5, 
         label = 'No Conservation')
ax1.plot(lema_sum_irr_ppt, dp_lema, 'x', color = colors[7], markersize = 5,
         label = 'Conservation')

ax1.plot(irr_ppt_total, lin_reg_dp, ls = 'dashed', color = colors[7], 
         label='EQ: y = {:.4}x - {:.2f}'.format(m_dpppt,abs(b_dpppt)), zorder = 0,
         linewidth = 0.75)


ax1.set_xlabel(r'$\sum$ Annual Precipitation + Annual Irrigation Depth (mm)', fontsize = 8)
ax1.set_ylabel('Annual Deep Percolation (mm)', fontsize = 8)
plt.tick_params(axis='both', which='major', labelsize = 8)

ax1.legend(loc = 'best', prop = {'size': 6, }, markerscale = 0.75)
q_vs_ppt.tight_layout()
q_vs_ppt.savefig('./Figures/Fig3_DP_vs_PPT.png', dpi = 300)


# Applied rates of annual pumping and deep percolation
app_rates= plt.figure(figsize = (190*mm, 145*mm))

gs = app_rates.add_gridspec(12,10)
ax1 = app_rates.add_subplot(gs[0:6, :])


ax1.plot(range(1955, 1994, 1), q_no_full.iloc[0:39], ':', color = colors[7], zorder = 2, linewidth = 1)
ax1.plot(range(1955, 1994, 1), q_20_full.iloc[0:39], ':', color = colors[0], zorder = 1, linewidth = 1)
ax1.plot(range(1955, 1994, 1), q_30_full.iloc[0:39], ':', color = colors[3], zorder = 0, linewidth = 1)

ax1.plot(range(1993, 2020, 1), q_no_full.iloc[38:65], color = colors[7], zorder = 2, linewidth = 1)
ax1.plot(range(1993, 2020, 1), q_30_full.iloc[38:65], color = colors[0], zorder = 0, linewidth = 1)
ax1.plot(range(1993, 2020, 1), q_30_full.iloc[38:65], color = colors[3], zorder = 1, linewidth = 1)

ax1.plot(range(2019, 2100, 1), q_no_full.iloc[64:], '--', color = colors[7], zorder = 2, linewidth = 1)
ax1.plot(range(2019, 2100, 1), q_20_full.iloc[64:], '--', color = colors[0], zorder = 1, linewidth = 1)
ax1.plot(range(2019, 2100, 1), q_30_full.iloc[64:], '--', color = colors[3], zorder = 0, linewidth = 1)


ax1.vlines(2019, 0, 200, linestyle = '-', color = 'k', linewidth = 1) 

ax1.set_xlim(1955, 2100)
ax1.set_ylim(0, 200)
ax1.set_xticklabels([])

ax1.set_ylabel('Pumping Rate (mm $yr^{-1}$)', fontsize = 8)

plt.tick_params(axis='both', which='major', labelsize = 8)

ax1.legend(labels = ['_nolegend_', '_nolegend_', '_nolegend_', 'No Conservation', 
                     '20% Pumping Reduction', '30% Pumping Reduction'], 
           loc = 'upper left', prop={'size': 6}, markerscale = 0.5)


ax2 = app_rates.add_subplot(gs[6:, :])

ax2.plot(range(1955, 1994, 1), dp_no_full.iloc[55:94], ':', color = colors[7], zorder = 2, linewidth = 1)
ax2.plot(range(1955, 1994, 1), dp_20_full.iloc[55:94], ':', color = colors[0], zorder = 1, linewidth = 1)
ax2.plot(range(1955, 1994, 1), dp_30_full.iloc[55:94], ':', color = colors[3], zorder = 0, linewidth = 1)

ax2.plot(range(1993, 2020, 1), dp_no_full.iloc[93:120], color = colors[7], zorder = 2, linewidth = 1)
ax2.plot(range(1993, 2020, 1), dp_20_full.iloc[93:120], color = colors[0], zorder = 0, linewidth = 1)
ax2.plot(range(1993, 2020, 1), dp_30_full.iloc[93:120], color = colors[3], zorder = 1, linewidth = 1)

ax2.plot(range(2019, 2100, 1), dp_no_full.iloc[119:], '--', color = colors[7], zorder = 2, linewidth = 1)
ax2.plot(range(2019, 2100, 1), dp_20_full.iloc[119:], '--', color = colors[0], zorder = 1,linewidth = 1)
ax2.plot(range(2019, 2100, 1), dp_30_full.iloc[119:], '--', color = colors[3], zorder = 0, linewidth = 1)

ax2.vlines(2019, 0, 200, linestyle = '-', color = 'k', linewidth = 1) 

ax2.set_xlim(1955, 2100)
ax2.set_ylim(0, 200)

ax2.set_xlabel('Years', fontsize = 8)
ax2.set_ylabel('Deep Percolation Rate (mm $yr^{-1}$)', fontsize = 8)

plt.tick_params(axis='both', which='major', labelsize = 8)

ax2.legend(labels = ['_nolegend_', '_nolegend_', '_nolegend_', 'No Conservation', 
                     '20% Pumping Reduction', '30% Pumping Reduction'], 
           loc = 'upper left', prop={'size': 6}, markerscale = 0.5)

app_rates.tight_layout()

app_rates.savefig('./Figures/Fig3_App_Rates_TimeSeries.png', dpi = 300)


inset = plt.figure(figsize = (55*mm, 45*mm))

gs = inset.add_gridspec(1,1)
ax1 = inset.add_subplot(gs[0, 0])

ax1.plot(range(2065, 2086, 1), dp_no_full.iloc[165:186], '--', color = colors[7], zorder = 2)
ax1.plot(range(2065, 2086, 1), dp_20_full.iloc[165:186], '--', color = colors[0], zorder = 1)
ax1.plot(range(2065, 2086, 1), dp_30_full.iloc[165:186], '--', color = colors[3], zorder = 0)

ax1.xaxis.set_major_locator(plt.MaxNLocator(2))
ax1.set_xticklabels([2070, 2075, 2080])

ax1.set_xlim(2070, 2080)


inset.tight_layout()

inset.savefig('./Figures/Fig_3_Inset_Plot.png', dpi = 300, transparent = True)