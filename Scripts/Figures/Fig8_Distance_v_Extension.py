# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:43:19 2021

@author: tomglose
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import os
from pathlib import Path

# Change directory to working folder <- be sure to change
working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Figures/').mkdir(parents = True, exist_ok = True)


# Read in lhs variables
lhs_lat_inflow = pd.read_csv('./Inputs/Proj_LHS_Lat_Inflow.csv')
lhs_lat_inflow.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs_lat_inflow['Run'] = lhs_lat_inflow['Run'] + 1

lhs_rech = pd.read_csv('./Inputs/Proj_LHS_Recharge.csv')
lhs_rech.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs_rech['Run'] = lhs_rech['Run'] + 1


dtw_file = ('./Validation/Year_to_Year_Heads.csv')
heads = pd.read_csv(dtw_file, usecols = ['Average'])


#%% Scenario_1 Heads
# 30% Pumping Reduction
S1_Heads_LEMA_30 = pd.read_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_30.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_LEMA_30.drop(S1_Heads_LEMA_30.columns[0], axis = 1, inplace = True)
S1_Heads_LEMA_30.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_LEMA_30 = S1_Heads_LEMA_30.mask(np.isclose(S1_Heads_LEMA_30, -1E30))
S1_Heads_LEMA_30.fillna(0, inplace = True)
S1_Heads_LEMA_30['Year'] = range(1999, 2101, 1)
S1_Heads_LEMA_30.set_index('Year', inplace = True)


S1_Heads_BAU_30_9 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_9.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_9.drop(S1_Heads_BAU_30_9.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_9.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_9 = S1_Heads_BAU_30_9.mask(np.isclose(S1_Heads_BAU_30_9, -1E30))
S1_Heads_BAU_30_9.fillna(0, inplace = True)
S1_Heads_BAU_30_9['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_9.set_index('Year', inplace = True)


S1_Heads_BAU_30_10 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_10.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_10.drop(S1_Heads_BAU_30_10.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_10.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_10 = S1_Heads_BAU_30_10.mask(np.isclose(S1_Heads_BAU_30_10, -1E30))
S1_Heads_BAU_30_10.fillna(0, inplace = True)
S1_Heads_BAU_30_10['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_10.set_index('Year', inplace = True)


S1_Heads_BAU_30_11 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_11.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_11.drop(S1_Heads_BAU_30_11.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_11.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_11 = S1_Heads_BAU_30_11.mask(np.isclose(S1_Heads_BAU_30_11, -1E30))
S1_Heads_BAU_30_11.fillna(0, inplace = True)
S1_Heads_BAU_30_11['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_11.set_index('Year', inplace = True)


S1_Heads_BAU_30_12 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_12.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_12.drop(S1_Heads_BAU_30_12.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_12.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_12 = S1_Heads_BAU_30_12.mask(np.isclose(S1_Heads_BAU_30_12, -1E30))
S1_Heads_BAU_30_12.fillna(0, inplace = True)
S1_Heads_BAU_30_12['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_12.set_index('Year', inplace = True)


S1_Heads_BAU_30_13 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_13.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_13.drop(S1_Heads_BAU_30_13.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_13.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_13 = S1_Heads_BAU_30_13.mask(np.isclose(S1_Heads_BAU_30_13, -1E30))
S1_Heads_BAU_30_13.fillna(0, inplace = True)
S1_Heads_BAU_30_13['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_13.set_index('Year', inplace = True)



S1_Heads_BAU_30_14 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_14.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_14.drop(S1_Heads_BAU_30_14.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_14.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_14 = S1_Heads_BAU_30_14.mask(np.isclose(S1_Heads_BAU_30_14, -1E30))
S1_Heads_BAU_30_14.fillna(0, inplace = True)
S1_Heads_BAU_30_14['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_14.set_index('Year', inplace = True)


S1_Heads_BAU_30_15 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_15.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_15.drop(S1_Heads_BAU_30_15.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_15.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_15 = S1_Heads_BAU_30_15.mask(np.isclose(S1_Heads_BAU_30_15, -1E30))
S1_Heads_BAU_30_15.fillna(0, inplace = True)
S1_Heads_BAU_30_15['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_15.set_index('Year', inplace = True)


S1_Heads_BAU_30_16 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_16.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_16.drop(S1_Heads_BAU_30_16.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_16.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_16 = S1_Heads_BAU_30_16.mask(np.isclose(S1_Heads_BAU_30_16, -1E30))
S1_Heads_BAU_30_16.fillna(0, inplace = True)
S1_Heads_BAU_30_16['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_16.set_index('Year', inplace = True)


S1_Heads_BAU_30_17 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_17.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_17.drop(S1_Heads_BAU_30_17.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_17.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_17 = S1_Heads_BAU_30_17.mask(np.isclose(S1_Heads_BAU_30_17, -1E30))
S1_Heads_BAU_30_17.fillna(0, inplace = True)
S1_Heads_BAU_30_17['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_17.set_index('Year', inplace = True)


S1_Heads_BAU_30_18 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_18.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_18.drop(S1_Heads_BAU_30_18.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_18.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_18 = S1_Heads_BAU_30_18.mask(np.isclose(S1_Heads_BAU_30_18, -1E30))
S1_Heads_BAU_30_18.fillna(0, inplace = True)
S1_Heads_BAU_30_18['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_18.set_index('Year', inplace = True)


S1_Heads_BAU_30_19 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_19.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_19.drop(S1_Heads_BAU_30_19.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_19.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_19 = S1_Heads_BAU_30_19.mask(np.isclose(S1_Heads_BAU_30_19, -1E30))
S1_Heads_BAU_30_19.fillna(0, inplace = True)
S1_Heads_BAU_30_19['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_19.set_index('Year', inplace = True)


S1_Heads_BAU_30_20 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_20.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_20.drop(S1_Heads_BAU_30_20.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_20.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_20 = S1_Heads_BAU_30_20.mask(np.isclose(S1_Heads_BAU_30_20, -1E30))
S1_Heads_BAU_30_20.fillna(0, inplace = True)
S1_Heads_BAU_30_20['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_20.set_index('Year', inplace = True)


S1_Heads_BAU_30_21 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_21.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_21.drop(S1_Heads_BAU_30_21.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_21.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_21 = S1_Heads_BAU_30_21.mask(np.isclose(S1_Heads_BAU_30_21, -1E30))
S1_Heads_BAU_30_21.fillna(0, inplace = True)
S1_Heads_BAU_30_21['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_21.set_index('Year', inplace = True)


S1_Heads_BAU_30_22 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_22.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_22.drop(S1_Heads_BAU_30_22.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_22.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_22 = S1_Heads_BAU_30_22.mask(np.isclose(S1_Heads_BAU_30_22, -1E30))
S1_Heads_BAU_30_22.fillna(0, inplace = True)
S1_Heads_BAU_30_22['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_22.set_index('Year', inplace = True)


S1_Heads_BAU_30_23 = pd.read_csv('./Outputs/BAU_Heads/LI/30_Percent/Full_Heads_BAU_23.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_30_23.drop(S1_Heads_BAU_30_23.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_30_23.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_30_23 = S1_Heads_BAU_30_23.mask(np.isclose(S1_Heads_BAU_30_23, -1E30))
S1_Heads_BAU_30_23.fillna(0, inplace = True)
S1_Heads_BAU_30_23['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_30_23.set_index('Year', inplace = True)


S1_Heads_No_LEMA = pd.read_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_30_No_Red.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_No_LEMA.drop(S1_Heads_No_LEMA.columns[0], axis = 1, inplace = True)
S1_Heads_No_LEMA.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_No_LEMA = S1_Heads_No_LEMA.mask(np.isclose(S1_Heads_No_LEMA, -1E30))
S1_Heads_No_LEMA.fillna(0, inplace = True)
S1_Heads_No_LEMA['Year'] = range(1999, 2101, 1)
S1_Heads_No_LEMA.set_index('Year', inplace = True)

# 20% Pumping Reduction
S1_Heads_LEMA_20 = pd.read_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_20.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_LEMA_20.drop(S1_Heads_LEMA_20.columns[0], axis = 1, inplace = True)
S1_Heads_LEMA_20.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_LEMA_20 = S1_Heads_LEMA_20.mask(np.isclose(S1_Heads_LEMA_20, -1E30))
S1_Heads_LEMA_20.fillna(0, inplace = True)
S1_Heads_LEMA_20['Year'] = range(1999, 2101, 1)
S1_Heads_LEMA_20.set_index('Year', inplace = True)


S1_Heads_BAU_20_9 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_9.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_9.drop(S1_Heads_BAU_20_9.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_9.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_9 = S1_Heads_BAU_20_9.mask(np.isclose(S1_Heads_BAU_20_9, -1E30))
S1_Heads_BAU_20_9.fillna(0, inplace = True)
S1_Heads_BAU_20_9['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_9.set_index('Year', inplace = True)


S1_Heads_BAU_20_10 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_10.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_10.drop(S1_Heads_BAU_20_10.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_10.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_10 = S1_Heads_BAU_20_10.mask(np.isclose(S1_Heads_BAU_20_10, -1E30))
S1_Heads_BAU_20_10.fillna(0, inplace = True)
S1_Heads_BAU_20_10['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_10.set_index('Year', inplace = True)


S1_Heads_BAU_20_11 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_11.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_11.drop(S1_Heads_BAU_20_11.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_11.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_11 = S1_Heads_BAU_20_11.mask(np.isclose(S1_Heads_BAU_20_11, -1E30))
S1_Heads_BAU_20_11.fillna(0, inplace = True)
S1_Heads_BAU_20_11['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_11.set_index('Year', inplace = True)


S1_Heads_BAU_20_12 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_12.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_12.drop(S1_Heads_BAU_20_12.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_12.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_12 = S1_Heads_BAU_20_12.mask(np.isclose(S1_Heads_BAU_20_12, -1E30))
S1_Heads_BAU_20_12.fillna(0, inplace = True)
S1_Heads_BAU_20_12['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_12.set_index('Year', inplace = True)


S1_Heads_BAU_20_13 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_13.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_13.drop(S1_Heads_BAU_20_13.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_13.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_13 = S1_Heads_BAU_20_13.mask(np.isclose(S1_Heads_BAU_20_13, -1E30))
S1_Heads_BAU_20_13.fillna(0, inplace = True)
S1_Heads_BAU_20_13['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_13.set_index('Year', inplace = True)


S1_Heads_BAU_20_14 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_14.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_14.drop(S1_Heads_BAU_20_14.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_14.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_14 = S1_Heads_BAU_20_14.mask(np.isclose(S1_Heads_BAU_20_14, -1E30))
S1_Heads_BAU_20_14.fillna(0, inplace = True)
S1_Heads_BAU_20_14['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_14.set_index('Year', inplace = True)


S1_Heads_BAU_20_15 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_15.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_15.drop(S1_Heads_BAU_20_15.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_15.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_15 = S1_Heads_BAU_20_15.mask(np.isclose(S1_Heads_BAU_20_15, -1E30))
S1_Heads_BAU_20_15.fillna(0, inplace = True)
S1_Heads_BAU_20_15['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_15.set_index('Year', inplace = True)


S1_Heads_BAU_20_16 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_16.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_16.drop(S1_Heads_BAU_20_16.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_16.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_16 = S1_Heads_BAU_20_16.mask(np.isclose(S1_Heads_BAU_20_16, -1E30))
S1_Heads_BAU_20_16.fillna(0, inplace = True)
S1_Heads_BAU_20_16['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_16.set_index('Year', inplace = True)


S1_Heads_BAU_20_17 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_17.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_17.drop(S1_Heads_BAU_20_17.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_17.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_17 = S1_Heads_BAU_20_17.mask(np.isclose(S1_Heads_BAU_20_17, -1E30))
S1_Heads_BAU_20_17.fillna(0, inplace = True)
S1_Heads_BAU_20_17['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_17.set_index('Year', inplace = True)


S1_Heads_BAU_20_18 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_18.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_18.drop(S1_Heads_BAU_20_18.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_18.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_18 = S1_Heads_BAU_20_18.mask(np.isclose(S1_Heads_BAU_20_18, -1E30))
S1_Heads_BAU_20_18.fillna(0, inplace = True)
S1_Heads_BAU_20_18['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_18.set_index('Year', inplace = True)


S1_Heads_BAU_20_19 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_19.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_19.drop(S1_Heads_BAU_20_19.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_19.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_19 = S1_Heads_BAU_20_19.mask(np.isclose(S1_Heads_BAU_20_19, -1E30))
S1_Heads_BAU_20_19.fillna(0, inplace = True)
S1_Heads_BAU_20_19['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_19.set_index('Year', inplace = True)


S1_Heads_BAU_20_20 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_20.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_20.drop(S1_Heads_BAU_20_20.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_20.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_20 = S1_Heads_BAU_20_20.mask(np.isclose(S1_Heads_BAU_20_20, -1E30))
S1_Heads_BAU_20_20.fillna(0, inplace = True)
S1_Heads_BAU_20_20['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_20.set_index('Year', inplace = True)


S1_Heads_BAU_20_21 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_21.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_21.drop(S1_Heads_BAU_20_21.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_21.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_21 = S1_Heads_BAU_20_21.mask(np.isclose(S1_Heads_BAU_20_21, -1E30))
S1_Heads_BAU_20_21.fillna(0, inplace = True)
S1_Heads_BAU_20_21['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_21.set_index('Year', inplace = True)


S1_Heads_BAU_20_22 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_22.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_22.drop(S1_Heads_BAU_20_22.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_22.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_22 = S1_Heads_BAU_20_22.mask(np.isclose(S1_Heads_BAU_20_22, -1E30))
S1_Heads_BAU_20_22.fillna(0, inplace = True)
S1_Heads_BAU_20_22['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_22.set_index('Year', inplace = True)


S1_Heads_BAU_20_23 = pd.read_csv('./Outputs/BAU_Heads/LI/20_Percent/Full_Heads_BAU_23.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S1_Heads_BAU_20_23.drop(S1_Heads_BAU_20_23.columns[0], axis = 1, inplace = True)
S1_Heads_BAU_20_23.columns = lhs_lat_inflow.Run.tolist()
S1_Heads_BAU_20_23 = S1_Heads_BAU_20_23.mask(np.isclose(S1_Heads_BAU_20_23, -1E30))
S1_Heads_BAU_20_23.fillna(0, inplace = True)
S1_Heads_BAU_20_23['Year'] = range(1999, 2101, 1)
S1_Heads_BAU_20_23.set_index('Year', inplace = True)

#%% Scenario_2 Heads
# 30% Pumping Reduction
S2_Heads_LEMA_30 = pd.read_csv('./Evaluation_Data/Projection/Rech/Accept_Full_Heads_30.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_LEMA_30.drop(S2_Heads_LEMA_30.columns[0], axis = 1, inplace = True)
S2_Heads_LEMA_30.columns = lhs_rech.Run.tolist()
S2_Heads_LEMA_30 = S2_Heads_LEMA_30.mask(np.isclose(S2_Heads_LEMA_30, -1E30))
S2_Heads_LEMA_30.fillna(0, inplace = True)
S2_Heads_LEMA_30['Year'] = range(1999, 2101, 1)
S2_Heads_LEMA_30.set_index('Year', inplace = True)


S2_Heads_BAU_30_9 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_9.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_9.drop(S2_Heads_BAU_30_9.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_9.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_9 = S2_Heads_BAU_30_9.mask(np.isclose(S2_Heads_BAU_30_9, -1E30))
S2_Heads_BAU_30_9.fillna(0, inplace = True)
S2_Heads_BAU_30_9['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_9.set_index('Year', inplace = True)


S2_Heads_BAU_30_10 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_10.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_10.drop(S2_Heads_BAU_30_10.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_10.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_10 = S2_Heads_BAU_30_10.mask(np.isclose(S2_Heads_BAU_30_10, -1E30))
S2_Heads_BAU_30_10.fillna(0, inplace = True)
S2_Heads_BAU_30_10['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_10.set_index('Year', inplace = True)


S2_Heads_BAU_30_11 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_11.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_11.drop(S2_Heads_BAU_30_11.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_11.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_11 = S2_Heads_BAU_30_11.mask(np.isclose(S2_Heads_BAU_30_11, -1E30))
S2_Heads_BAU_30_11.fillna(0, inplace = True)
S2_Heads_BAU_30_11['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_11.set_index('Year', inplace = True)


S2_Heads_BAU_30_12 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_12.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_12.drop(S2_Heads_BAU_30_12.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_12.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_12 = S2_Heads_BAU_30_12.mask(np.isclose(S2_Heads_BAU_30_12, -1E30))
S2_Heads_BAU_30_12.fillna(0, inplace = True)
S2_Heads_BAU_30_12['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_12.set_index('Year', inplace = True)


S2_Heads_BAU_30_13 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_13.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_13.drop(S2_Heads_BAU_30_13.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_13.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_13 = S2_Heads_BAU_30_13.mask(np.isclose(S2_Heads_BAU_30_13, -1E30))
S2_Heads_BAU_30_13.fillna(0, inplace = True)
S2_Heads_BAU_30_13['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_13.set_index('Year', inplace = True)



S2_Heads_BAU_30_14 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_14.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_14.drop(S2_Heads_BAU_30_14.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_14.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_14 = S2_Heads_BAU_30_14.mask(np.isclose(S2_Heads_BAU_30_14, -1E30))
S2_Heads_BAU_30_14.fillna(0, inplace = True)
S2_Heads_BAU_30_14['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_14.set_index('Year', inplace = True)


S2_Heads_BAU_30_15 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_15.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_15.drop(S2_Heads_BAU_30_15.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_15.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_15 = S2_Heads_BAU_30_15.mask(np.isclose(S2_Heads_BAU_30_15, -1E30))
S2_Heads_BAU_30_15.fillna(0, inplace = True)
S2_Heads_BAU_30_15['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_15.set_index('Year', inplace = True)


S2_Heads_BAU_30_16 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_16.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_16.drop(S2_Heads_BAU_30_16.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_16.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_16 = S2_Heads_BAU_30_16.mask(np.isclose(S2_Heads_BAU_30_16, -1E30))
S2_Heads_BAU_30_16.fillna(0, inplace = True)
S2_Heads_BAU_30_16['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_16.set_index('Year', inplace = True)


S2_Heads_BAU_30_17 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_17.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_17.drop(S2_Heads_BAU_30_17.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_17.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_17 = S2_Heads_BAU_30_17.mask(np.isclose(S2_Heads_BAU_30_17, -1E30))
S2_Heads_BAU_30_17.fillna(0, inplace = True)
S2_Heads_BAU_30_17['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_17.set_index('Year', inplace = True)


S2_Heads_BAU_30_18 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_18.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_18.drop(S2_Heads_BAU_30_18.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_18.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_18 = S2_Heads_BAU_30_18.mask(np.isclose(S2_Heads_BAU_30_18, -1E30))
S2_Heads_BAU_30_18.fillna(0, inplace = True)
S2_Heads_BAU_30_18['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_18.set_index('Year', inplace = True)


S2_Heads_BAU_30_19 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_19.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_19.drop(S2_Heads_BAU_30_19.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_19.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_19 = S2_Heads_BAU_30_19.mask(np.isclose(S2_Heads_BAU_30_19, -1E30))
S2_Heads_BAU_30_19.fillna(0, inplace = True)
S2_Heads_BAU_30_19['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_19.set_index('Year', inplace = True)


S2_Heads_BAU_30_20 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_20.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_20.drop(S2_Heads_BAU_30_20.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_20.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_20 = S2_Heads_BAU_30_20.mask(np.isclose(S2_Heads_BAU_30_20, -1E30))
S2_Heads_BAU_30_20.fillna(0, inplace = True)
S2_Heads_BAU_30_20['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_20.set_index('Year', inplace = True)


S2_Heads_BAU_30_21 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_21.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_21.drop(S2_Heads_BAU_30_21.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_21.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_21 = S2_Heads_BAU_30_21.mask(np.isclose(S2_Heads_BAU_30_21, -1E30))
S2_Heads_BAU_30_21.fillna(0, inplace = True)
S2_Heads_BAU_30_21['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_21.set_index('Year', inplace = True)


S2_Heads_BAU_30_22 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_22.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_22.drop(S2_Heads_BAU_30_22.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_22.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_22 = S2_Heads_BAU_30_22.mask(np.isclose(S2_Heads_BAU_30_22, -1E30))
S2_Heads_BAU_30_22.fillna(0, inplace = True)
S2_Heads_BAU_30_22['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_22.set_index('Year', inplace = True)


S2_Heads_BAU_30_23 = pd.read_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_23.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_30_23.drop(S2_Heads_BAU_30_23.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_30_23.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_30_23 = S2_Heads_BAU_30_23.mask(np.isclose(S2_Heads_BAU_30_23, -1E30))
S2_Heads_BAU_30_23.fillna(0, inplace = True)
S2_Heads_BAU_30_23['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_30_23.set_index('Year', inplace = True)


S2_Heads_No_LEMA = pd.read_csv('./Evaluation_Data/Projection/Rech/Accept_Full_Heads_30_No_Red.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_No_LEMA.drop(S2_Heads_No_LEMA.columns[0], axis = 1, inplace = True)
S2_Heads_No_LEMA.columns = lhs_rech.Run.tolist()
S2_Heads_No_LEMA = S2_Heads_No_LEMA.mask(np.isclose(S2_Heads_No_LEMA, -1E30))
S2_Heads_No_LEMA.fillna(0, inplace = True)
S2_Heads_No_LEMA['Year'] = range(1999, 2101, 1)
S2_Heads_No_LEMA.set_index('Year', inplace = True)

# 20% Pumping Reduction
S2_Heads_LEMA_20 = pd.read_csv('./Evaluation_Data/Projection/Rech/Accept_Full_Heads_20.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_LEMA_20.drop(S2_Heads_LEMA_20.columns[0], axis = 1, inplace = True)
S2_Heads_LEMA_20.columns = lhs_rech.Run.tolist()
S2_Heads_LEMA_20 = S2_Heads_LEMA_20.mask(np.isclose(S2_Heads_LEMA_20, -1E30))
S2_Heads_LEMA_20.fillna(0, inplace = True)
S2_Heads_LEMA_20['Year'] = range(1999, 2101, 1)
S2_Heads_LEMA_20.set_index('Year', inplace = True)


S2_Heads_BAU_20_9 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_9.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_9.drop(S2_Heads_BAU_20_9.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_9.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_9 = S2_Heads_BAU_20_9.mask(np.isclose(S2_Heads_BAU_20_9, -1E30))
S2_Heads_BAU_20_9.fillna(0, inplace = True)
S2_Heads_BAU_20_9['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_9.set_index('Year', inplace = True)


S2_Heads_BAU_20_10 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_10.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_10.drop(S2_Heads_BAU_20_10.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_10.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_10 = S2_Heads_BAU_20_10.mask(np.isclose(S2_Heads_BAU_20_10, -1E30))
S2_Heads_BAU_20_10.fillna(0, inplace = True)
S2_Heads_BAU_20_10['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_10.set_index('Year', inplace = True)


S2_Heads_BAU_20_11 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_11.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_11.drop(S2_Heads_BAU_20_11.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_11.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_11 = S2_Heads_BAU_20_11.mask(np.isclose(S2_Heads_BAU_20_11, -1E30))
S2_Heads_BAU_20_11.fillna(0, inplace = True)
S2_Heads_BAU_20_11['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_11.set_index('Year', inplace = True)


S2_Heads_BAU_20_12 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_12.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_12.drop(S2_Heads_BAU_20_12.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_12.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_12 = S2_Heads_BAU_20_12.mask(np.isclose(S2_Heads_BAU_20_12, -1E30))
S2_Heads_BAU_20_12.fillna(0, inplace = True)
S2_Heads_BAU_20_12['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_12.set_index('Year', inplace = True)


S2_Heads_BAU_20_13 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_13.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_13.drop(S2_Heads_BAU_20_13.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_13.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_13 = S2_Heads_BAU_20_13.mask(np.isclose(S2_Heads_BAU_20_13, -1E30))
S2_Heads_BAU_20_13.fillna(0, inplace = True)
S2_Heads_BAU_20_13['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_13.set_index('Year', inplace = True)


S2_Heads_BAU_20_14 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_14.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_14.drop(S2_Heads_BAU_20_14.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_14.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_14 = S2_Heads_BAU_20_14.mask(np.isclose(S2_Heads_BAU_20_14, -1E30))
S2_Heads_BAU_20_14.fillna(0, inplace = True)
S2_Heads_BAU_20_14['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_14.set_index('Year', inplace = True)


S2_Heads_BAU_20_15 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_15.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_15.drop(S2_Heads_BAU_20_15.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_15.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_15 = S2_Heads_BAU_20_15.mask(np.isclose(S2_Heads_BAU_20_15, -1E30))
S2_Heads_BAU_20_15.fillna(0, inplace = True)
S2_Heads_BAU_20_15['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_15.set_index('Year', inplace = True)


S2_Heads_BAU_20_16 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_16.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_16.drop(S2_Heads_BAU_20_16.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_16.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_16 = S2_Heads_BAU_20_16.mask(np.isclose(S2_Heads_BAU_20_16, -1E30))
S2_Heads_BAU_20_16.fillna(0, inplace = True)
S2_Heads_BAU_20_16['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_16.set_index('Year', inplace = True)


S2_Heads_BAU_20_17 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_17.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_17.drop(S2_Heads_BAU_20_17.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_17.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_17 = S2_Heads_BAU_20_17.mask(np.isclose(S2_Heads_BAU_20_17, -1E30))
S2_Heads_BAU_20_17.fillna(0, inplace = True)
S2_Heads_BAU_20_17['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_17.set_index('Year', inplace = True)


S2_Heads_BAU_20_18 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_18.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_18.drop(S2_Heads_BAU_20_18.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_18.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_18 = S2_Heads_BAU_20_18.mask(np.isclose(S2_Heads_BAU_20_18, -1E30))
S2_Heads_BAU_20_18.fillna(0, inplace = True)
S2_Heads_BAU_20_18['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_18.set_index('Year', inplace = True)


S2_Heads_BAU_20_19 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_19.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_19.drop(S2_Heads_BAU_20_19.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_19.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_19 = S2_Heads_BAU_20_19.mask(np.isclose(S2_Heads_BAU_20_19, -1E30))
S2_Heads_BAU_20_19.fillna(0, inplace = True)
S2_Heads_BAU_20_19['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_19.set_index('Year', inplace = True)


S2_Heads_BAU_20_20 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_20.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_20.drop(S2_Heads_BAU_20_20.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_20.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_20 = S2_Heads_BAU_20_20.mask(np.isclose(S2_Heads_BAU_20_20, -1E30))
S2_Heads_BAU_20_20.fillna(0, inplace = True)
S2_Heads_BAU_20_20['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_20.set_index('Year', inplace = True)


S2_Heads_BAU_20_21 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_21.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_21.drop(S2_Heads_BAU_20_21.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_21.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_21 = S2_Heads_BAU_20_21.mask(np.isclose(S2_Heads_BAU_20_21, -1E30))
S2_Heads_BAU_20_21.fillna(0, inplace = True)
S2_Heads_BAU_20_21['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_21.set_index('Year', inplace = True)


S2_Heads_BAU_20_22 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_22.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_22.drop(S2_Heads_BAU_20_22.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_22.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_22 = S2_Heads_BAU_20_22.mask(np.isclose(S2_Heads_BAU_20_22, -1E30))
S2_Heads_BAU_20_22.fillna(0, inplace = True)
S2_Heads_BAU_20_22['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_22.set_index('Year', inplace = True)


S2_Heads_BAU_20_23 = pd.read_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_23.csv', index_col = [0], 
                             skiprows = list(range(0, 44, 1))) 
S2_Heads_BAU_20_23.drop(S2_Heads_BAU_20_23.columns[0], axis = 1, inplace = True)
S2_Heads_BAU_20_23.columns = lhs_rech.Run.tolist()
S2_Heads_BAU_20_23 = S2_Heads_BAU_20_23.mask(np.isclose(S2_Heads_BAU_20_23, -1E30))
S2_Heads_BAU_20_23.fillna(0, inplace = True)
S2_Heads_BAU_20_23['Year'] = range(1999, 2101, 1)
S2_Heads_BAU_20_23.set_index('Year', inplace = True)

#%% Scenario 1 Results

res_ind_S1_LEMA_30 = []
res_ind_S1_BAU_30_9 = []
res_ind_S1_BAU_30_10 = []
res_ind_S1_BAU_30_11 = []
res_ind_S1_BAU_30_12 = []
res_ind_S1_BAU_30_13 = []
res_ind_S1_BAU_30_14 = []
res_ind_S1_BAU_30_15 = []
res_ind_S1_BAU_30_15 = []
res_ind_S1_BAU_30_16 = []
res_ind_S1_BAU_30_17 = []
res_ind_S1_BAU_30_18 = []
res_ind_S1_BAU_30_19 = []
res_ind_S1_BAU_30_20 = []
res_ind_S1_BAU_30_21 = []
res_ind_S1_BAU_30_22 = []
res_ind_S1_BAU_30_23 = []
res_ind_S1_No_LEMA = []


for i in lhs_lat_inflow.Run.tolist():
    res_ind_S1_LEMA_30.append(S1_Heads_LEMA_30[i].sub(8).abs().idxmin())  
    res_ind_S1_BAU_30_9.append(S1_Heads_BAU_30_9[i].sub(8).abs().idxmin()) 
    res_ind_S1_BAU_30_10.append(S1_Heads_BAU_30_10[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_11.append(S1_Heads_BAU_30_11[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_12.append(S1_Heads_BAU_30_12[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_13.append(S1_Heads_BAU_30_13[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_14.append(S1_Heads_BAU_30_14[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_15.append(S1_Heads_BAU_30_15[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_16.append(S1_Heads_BAU_30_16[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_17.append(S1_Heads_BAU_30_17[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_18.append(S1_Heads_BAU_30_18[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_19.append(S1_Heads_BAU_30_19[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_20.append(S1_Heads_BAU_30_20[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_21.append(S1_Heads_BAU_30_21[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_22.append(S1_Heads_BAU_30_22[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_30_23.append(S1_Heads_BAU_30_23[i].sub(8).abs().idxmin())
    res_ind_S1_No_LEMA.append(S1_Heads_No_LEMA[i].sub(8).abs().idxmin())


ext_S1_LEMA_30 = np.mean([x - y for x, y in zip(res_ind_S1_LEMA_30, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_23 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_23, res_ind_S1_No_LEMA)])

ext_S1_BAU_30_22 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_22, res_ind_S1_No_LEMA)]) 

ext_S1_BAU_30_21 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_21, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_20 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_20, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_19 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_19, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_18 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_18, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_17 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_17, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_16 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_16, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_15 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_15, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_14 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_14, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_13 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_13, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_12 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_12, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_11 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_11, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_10 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_10, res_ind_S1_No_LEMA)])
ext_S1_BAU_30_9 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_30_9, res_ind_S1_No_LEMA)])


res_ind_S1_LEMA_20 = []
res_ind_S1_BAU_20_9 = []
res_ind_S1_BAU_20_10 = []
res_ind_S1_BAU_20_11 = []
res_ind_S1_BAU_20_12 = []
res_ind_S1_BAU_20_13 = []
res_ind_S1_BAU_20_14 = []
res_ind_S1_BAU_20_15 = []
res_ind_S1_BAU_20_15 = []
res_ind_S1_BAU_20_16 = []
res_ind_S1_BAU_20_17 = []
res_ind_S1_BAU_20_18 = []
res_ind_S1_BAU_20_19 = []
res_ind_S1_BAU_20_20 = []
res_ind_S1_BAU_20_21 = []
res_ind_S1_BAU_20_22 = []
res_ind_S1_BAU_20_23 = []
res_ind_S1_No_LEMA = []


for i in lhs_lat_inflow.Run.tolist():
    res_ind_S1_LEMA_20.append(S1_Heads_LEMA_20[i].sub(8).abs().idxmin())  
    res_ind_S1_BAU_20_9.append(S1_Heads_BAU_20_9[i].sub(8).abs().idxmin()) 
    res_ind_S1_BAU_20_10.append(S1_Heads_BAU_20_10[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_11.append(S1_Heads_BAU_20_11[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_12.append(S1_Heads_BAU_20_12[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_13.append(S1_Heads_BAU_20_13[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_14.append(S1_Heads_BAU_20_14[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_15.append(S1_Heads_BAU_20_15[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_16.append(S1_Heads_BAU_20_16[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_17.append(S1_Heads_BAU_20_17[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_18.append(S1_Heads_BAU_20_18[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_19.append(S1_Heads_BAU_20_19[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_20.append(S1_Heads_BAU_20_20[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_21.append(S1_Heads_BAU_20_21[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_22.append(S1_Heads_BAU_20_22[i].sub(8).abs().idxmin())
    res_ind_S1_BAU_20_23.append(S1_Heads_BAU_20_23[i].sub(8).abs().idxmin())
    res_ind_S1_No_LEMA.append(S1_Heads_No_LEMA[i].sub(8).abs().idxmin())


ext_S1_LEMA_20 = np.mean([x - y for x, y in zip(res_ind_S1_LEMA_20, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_23 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_23, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_22 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_22, res_ind_S1_No_LEMA)]) 
ext_S1_BAU_20_21 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_21, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_20 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_20, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_19 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_19, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_18 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_18, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_17 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_17, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_16 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_16, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_15 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_15, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_14 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_14, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_13 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_13, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_12 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_12, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_11 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_11, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_10 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_10, res_ind_S1_No_LEMA)])
ext_S1_BAU_20_9 = np.mean([x - y for x, y in zip(res_ind_S1_BAU_20_9, res_ind_S1_No_LEMA)])

#%% Scenario 2 Results
res_ind_S2_LEMA_30 = []
res_ind_S2_BAU_30_9 = []
res_ind_S2_BAU_30_10 = []
res_ind_S2_BAU_30_11 = []
res_ind_S2_BAU_30_12 = []
res_ind_S2_BAU_30_13 = []
res_ind_S2_BAU_30_14 = []
res_ind_S2_BAU_30_15 = []
res_ind_S2_BAU_30_15 = []
res_ind_S2_BAU_30_16 = []
res_ind_S2_BAU_30_17 = []
res_ind_S2_BAU_30_18 = []
res_ind_S2_BAU_30_19 = []
res_ind_S2_BAU_30_20 = []
res_ind_S2_BAU_30_21 = []
res_ind_S2_BAU_30_22 = []
res_ind_S2_BAU_30_23 = []
res_ind_S2_No_LEMA = []


for i in lhs_rech.Run.tolist():
    res_ind_S2_LEMA_30.append(S2_Heads_LEMA_30[i].sub(8).abs().idxmin())  
    res_ind_S2_BAU_30_9.append(S2_Heads_BAU_30_9[i].sub(8).abs().idxmin()) 
    res_ind_S2_BAU_30_10.append(S2_Heads_BAU_30_10[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_11.append(S2_Heads_BAU_30_11[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_12.append(S2_Heads_BAU_30_12[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_13.append(S2_Heads_BAU_30_13[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_14.append(S2_Heads_BAU_30_14[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_15.append(S2_Heads_BAU_30_15[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_16.append(S2_Heads_BAU_30_16[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_17.append(S2_Heads_BAU_30_17[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_18.append(S2_Heads_BAU_30_18[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_19.append(S2_Heads_BAU_30_19[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_20.append(S2_Heads_BAU_30_20[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_21.append(S2_Heads_BAU_30_21[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_22.append(S2_Heads_BAU_30_22[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_30_23.append(S2_Heads_BAU_30_23[i].sub(8).abs().idxmin())
    res_ind_S2_No_LEMA.append(S2_Heads_No_LEMA[i].sub(8).abs().idxmin())


ext_S2_LEMA_30 = np.mean([x - y for x, y in zip(res_ind_S2_LEMA_30, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_23 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_23, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_22 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_22, res_ind_S2_No_LEMA)]) 
ext_S2_BAU_30_21 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_21, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_20 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_20, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_19 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_19, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_18 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_18, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_17 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_17, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_16 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_16, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_15 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_15, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_14 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_14, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_13 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_13, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_12 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_12, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_11 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_11, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_10 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_10, res_ind_S2_No_LEMA)])
ext_S2_BAU_30_9 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_30_9, res_ind_S2_No_LEMA)])


res_ind_S2_LEMA_20 = []
res_ind_S2_BAU_20_9 = []
res_ind_S2_BAU_20_10 = []
res_ind_S2_BAU_20_11 = []
res_ind_S2_BAU_20_12 = []
res_ind_S2_BAU_20_13 = []
res_ind_S2_BAU_20_14 = []
res_ind_S2_BAU_20_15 = []
res_ind_S2_BAU_20_15 = []
res_ind_S2_BAU_20_16 = []
res_ind_S2_BAU_20_17 = []
res_ind_S2_BAU_20_18 = []
res_ind_S2_BAU_20_19 = []
res_ind_S2_BAU_20_20 = []
res_ind_S2_BAU_20_21 = []
res_ind_S2_BAU_20_22 = []
res_ind_S2_BAU_20_23 = []
res_ind_S2_No_LEMA = []


for i in lhs_rech.Run.tolist():
    res_ind_S2_LEMA_20.append(S2_Heads_LEMA_20[i].sub(8).abs().idxmin())  
    res_ind_S2_BAU_20_9.append(S2_Heads_BAU_20_9[i].sub(8).abs().idxmin()) 
    res_ind_S2_BAU_20_10.append(S2_Heads_BAU_20_10[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_11.append(S2_Heads_BAU_20_11[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_12.append(S2_Heads_BAU_20_12[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_13.append(S2_Heads_BAU_20_13[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_14.append(S2_Heads_BAU_20_14[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_15.append(S2_Heads_BAU_20_15[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_16.append(S2_Heads_BAU_20_16[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_17.append(S2_Heads_BAU_20_17[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_18.append(S2_Heads_BAU_20_18[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_19.append(S2_Heads_BAU_20_19[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_20.append(S2_Heads_BAU_20_20[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_21.append(S2_Heads_BAU_20_21[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_22.append(S2_Heads_BAU_20_22[i].sub(8).abs().idxmin())
    res_ind_S2_BAU_20_23.append(S2_Heads_BAU_20_23[i].sub(8).abs().idxmin())
    res_ind_S2_No_LEMA.append(S2_Heads_No_LEMA[i].sub(8).abs().idxmin())


ext_S2_LEMA_20 = np.mean([x - y for x, y in zip(res_ind_S2_LEMA_20, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_23 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_23, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_22 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_22, res_ind_S2_No_LEMA)]) 
ext_S2_BAU_20_21 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_21, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_20 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_20, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_19 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_19, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_18 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_18, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_17 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_17, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_16 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_16, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_15 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_15, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_14 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_14, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_13 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_13, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_12 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_12, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_11 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_11, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_10 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_10, res_ind_S2_No_LEMA)])
ext_S2_BAU_20_9 = np.mean([x - y for x, y in zip(res_ind_S2_BAU_20_9, res_ind_S2_No_LEMA)])

#%% Plotting Variables

ext_S1_30 = [ext_S1_LEMA_30, ext_S1_BAU_30_23, ext_S1_BAU_30_22, 
             ext_S1_BAU_30_21, ext_S1_BAU_30_20, ext_S1_BAU_30_19, 
             ext_S1_BAU_30_18, ext_S1_BAU_30_17, ext_S1_BAU_30_16, 
             ext_S1_BAU_30_15, ext_S1_BAU_30_14, ext_S1_BAU_30_13, 
             ext_S1_BAU_30_12, ext_S1_BAU_30_11, ext_S1_BAU_30_10, 
             ext_S1_BAU_30_9]

ext_S1_20 = [ext_S1_LEMA_20, ext_S1_BAU_20_23, ext_S1_BAU_20_22, 
             ext_S1_BAU_20_21, ext_S1_BAU_20_20, ext_S1_BAU_20_19, 
             ext_S1_BAU_20_18, ext_S1_BAU_20_17, ext_S1_BAU_20_16, 
             ext_S1_BAU_20_15, ext_S1_BAU_20_14, ext_S1_BAU_20_13, 
             ext_S1_BAU_20_12, ext_S1_BAU_20_11, ext_S1_BAU_20_10, 
             ext_S1_BAU_20_9]

ext_S2_30 = [ext_S2_LEMA_30, ext_S2_BAU_30_23, ext_S2_BAU_30_22, 
             ext_S2_BAU_30_21, ext_S2_BAU_30_20, ext_S2_BAU_30_19, 
             ext_S2_BAU_30_18, ext_S2_BAU_30_17, ext_S2_BAU_30_16, 
             ext_S2_BAU_30_15, ext_S2_BAU_30_14, ext_S2_BAU_30_13, 
             ext_S2_BAU_30_12, ext_S2_BAU_30_11, ext_S2_BAU_30_10, 
             ext_S2_BAU_30_9]

ext_S2_20 = [ext_S2_LEMA_20, ext_S2_BAU_20_23, ext_S2_BAU_20_22, 
             ext_S2_BAU_20_21, ext_S2_BAU_20_20, ext_S2_BAU_20_19, 
             ext_S2_BAU_20_18, ext_S2_BAU_20_17, ext_S2_BAU_20_16, 
             ext_S2_BAU_20_15, ext_S2_BAU_20_14, ext_S2_BAU_20_13, 
             ext_S2_BAU_20_12, ext_S2_BAU_20_11, ext_S2_BAU_20_10, 
             ext_S2_BAU_20_9]


distance = [0, 0.8, 1.6, 2.4, 3.2, 4.0, 4.8, 5.6, 6.4, 7.2, 8, 8.8, 9.6, 
            10.4, 11.2, 12]
#%% Plots Yo
mm = 1/25.4

sns.set_style('ticks')
colors_30 = sns.color_palette('tab10')
colors_20 = sns.color_palette('tab10')

ext_lifetime_ext, ax1 = plt.subplots(1,1, figsize = (95*mm, 115*mm))

ax1.set_xlabel('Distance from Center (km)', fontsize = 8)
ax1.set_ylabel('Extension of Usable Lifetime (yr)', fontsize = 8)
ax1.set_ylim(0, 28)

plt.tick_params(axis='both', which='major', labelsize = 8)


ax1.scatter(distance, ext_S1_30, color = colors_30[1])
ax1.scatter(distance, ext_S2_30, color = colors_30[1], marker = 'x')
ax1.scatter(distance, ext_S1_20, color = colors_20[0])
ax1.scatter(distance, ext_S2_20, color = 'w', marker = 'o', zorder = 0)
ax1.scatter(distance, ext_S2_20, color = colors_20[0], marker = 'x')
ax1.vlines(5, -5, 30, linestyle = '--', color = 'k', zorder = 0)

labels = ['Lateral-Flow-Dominated', 'Recharge-Dominated', 
          '20% Pumping Reduction', '30% Pumping Reduction', 
          '_nolegend_', 'Edge of Conservation Area ']


leg = ax1.legend(labels = labels, scatterpoints = 1, 
           loc = 'best', prop={'size': 6}, markerscale = 0.75)

leg.legendHandles[0].set_color('k')
leg.legendHandles[1].set_color('k')
leg.legendHandles[2].set_color(colors_20[0])
leg.legendHandles[3].set_color(colors_30[1])


ext_lifetime_ext.tight_layout()


ext_lifetime_ext.savefig('./Figures/Exterior_Extension.png', dpi = 300)






