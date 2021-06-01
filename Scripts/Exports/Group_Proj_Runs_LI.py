# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:13:23 2020

@author: tomglose
"""

import os
import pandas as pd

working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

# Read in data from .csv files that contain real data from SD_6, format, and organize
hc_file = ('./Validation/Year_to_Year_Head_Change.csv')
dtw_file = ('./Validation/Year_to_Year_Heads.csv')

# Change in head
hc = pd.read_csv(hc_file, usecols = ['Average'])
hc_std = pd.read_csv(hc_file, usecols = ['Standard Deviation'])

# Depth to water
heads = pd.read_csv(dtw_file, usecols = ['Average'])
heads_std = pd.read_csv(dtw_file, usecols = ['Standard Deviation'])

#%% Lateral Inflow
# 20% No Reduction
# Read in LHS variables
lhs = pd.read_csv('./Inputs/Proj_LHS_Lat_Inflow.csv')

lhs.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']

lhs.Run = lhs.Run + 1

Accept_HC_No_Red = pd.DataFrame(data = [0], index = [99])
Accept_Heads_No_Red = pd.DataFrame(data = [0], index = [99])

Accept_Full_HC_No_Red = pd.DataFrame(data = [0], index = [54])
Accept_Full_Heads_No_Red = pd.DataFrame(data = [0], index = [55])


accept_runs = []

# Read in data from MODFLOW runs and populate a pandas dataframe 
for i in range(0, len(lhs), 1):
    
    AnnHeads = pd.read_csv('./Outputs/Proj_Heads/LI_No_Red/20_Percent/'
                           '/JanAnnHeads_Run_%s.csv' % (lhs.Run[i]))
    AnnHeads_HC = AnnHeads.diff(axis = 0)
    AnnHeads_HC = AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)

    
    Accept_HC_No_Red = pd.concat([Accept_HC_No_Red, pd.DataFrame(AnnHeads_HC.iloc[99:119, 24])], axis = 1)
    Accept_Heads_No_Red = pd.concat([Accept_Heads_No_Red, pd.DataFrame(AnnHeads.iloc[99:120, 24])], axis = 1)

    Accept_Full_HC_No_Red = pd.concat([Accept_Full_HC_No_Red, pd.DataFrame(AnnHeads_HC.iloc[54:, 24])], axis = 1)
    Accept_Full_Heads_No_Red = pd.concat([Accept_Full_Heads_No_Red, pd.DataFrame(AnnHeads.iloc[55:, 24])], axis = 1)


## Drop first column as it is a holder and then rename all columns to the 
## correct run.
##
# Good Runs
Accept_HC_No_Red = Accept_HC_No_Red.drop([0], axis = 1)
Accept_HC_No_Red.columns = lhs.Run

Accept_Heads_No_Red= Accept_Heads_No_Red.drop([0], axis = 1)
Accept_Heads_No_Red.columns = lhs.Run

## Be sure to change the folder!
from pathlib import Path

Path('./Evaluation_Data/Projection/LI/').mkdir(parents = True, exist_ok = True)


Accept_HC_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_HC_20_No_Red.csv')
Accept_Heads_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Heads_20_No_Red.csv')

Accept_Full_HC_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Full_HC_20_No_Red.csv')
Accept_Full_Heads_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_20_No_Red.csv') 

#%% 20% Reduction

Accept_HC_No_Red = pd.DataFrame(data = [0], index = [99])
Accept_Heads_No_Red = pd.DataFrame(data = [0], index = [99])

Accept_Full_HC_No_Red = pd.DataFrame(data = [0], index = [54])
Accept_Full_Heads_No_Red = pd.DataFrame(data = [0], index = [55])


accept_runs = []

# Read in data from MODFLOW runs and populate a pandas dataframe 
for i in range(0, len(lhs), 1):
    
    AnnHeads = pd.read_csv('./Outputs/Proj_Heads/LI/20_Percent/'
                           '/JanAnnHeads_Run_%s.csv' % (lhs.Run[i]))
    AnnHeads_HC = AnnHeads.diff(axis = 0)
    AnnHeads_HC = AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)

    
    Accept_HC_No_Red = pd.concat([Accept_HC_No_Red, pd.DataFrame(AnnHeads_HC.iloc[99:119, 24])], axis = 1)
    Accept_Heads_No_Red = pd.concat([Accept_Heads_No_Red, pd.DataFrame(AnnHeads.iloc[99:120, 24])], axis = 1)

    Accept_Full_HC_No_Red = pd.concat([Accept_Full_HC_No_Red, pd.DataFrame(AnnHeads_HC.iloc[54:, 24])], axis = 1)
    Accept_Full_Heads_No_Red = pd.concat([Accept_Full_Heads_No_Red, pd.DataFrame(AnnHeads.iloc[55:, 24])], axis = 1)


## Drop first column as it is a holder and then rename all columns to the 
## correct run.
##
# Good Runs
Accept_HC_No_Red = Accept_HC_No_Red.drop([0], axis = 1)
Accept_HC_No_Red.columns = lhs.Run

Accept_Heads_No_Red= Accept_Heads_No_Red.drop([0], axis = 1)
Accept_Heads_No_Red.columns = lhs.Run

## Be sure to change the folder!
from pathlib import Path

Path('./Evaluation_Data/Projection/LI/').mkdir(parents = True, exist_ok = True)


Accept_HC_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_HC_20.csv')
Accept_Heads_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Heads_20.csv')

Accept_Full_HC_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Full_HC_20.csv')
Accept_Full_Heads_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_20.csv') 

#%%
Accept_HC_No_Red = pd.DataFrame(data = [0], index = [99])
Accept_Heads_No_Red = pd.DataFrame(data = [0], index = [99])

Accept_Full_HC_No_Red = pd.DataFrame(data = [0], index = [54])
Accept_Full_Heads_No_Red = pd.DataFrame(data = [0], index = [55])


accept_runs = []

# Read in data from MODFLOW runs and populate a pandas dataframe 
for i in range(0, len(lhs), 1):
    
    AnnHeads = pd.read_csv('./Outputs/Proj_Heads/LI_No_Red/30_Percent/'
                           '/JanAnnHeads_Run_%s.csv' % (lhs.Run[i]))
    AnnHeads_HC = AnnHeads.diff(axis = 0)
    AnnHeads_HC = AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)

    
    Accept_HC_No_Red = pd.concat([Accept_HC_No_Red, pd.DataFrame(AnnHeads_HC.iloc[99:119, 24])], axis = 1)
    Accept_Heads_No_Red = pd.concat([Accept_Heads_No_Red, pd.DataFrame(AnnHeads.iloc[99:120, 24])], axis = 1)

    Accept_Full_HC_No_Red = pd.concat([Accept_Full_HC_No_Red, pd.DataFrame(AnnHeads_HC.iloc[54:, 24])], axis = 1)
    Accept_Full_Heads_No_Red = pd.concat([Accept_Full_Heads_No_Red, pd.DataFrame(AnnHeads.iloc[55:, 24])], axis = 1)


## Drop first column as it is a holder and then rename all columns to the 
## correct run.
##
# Good Runs
Accept_HC_No_Red = Accept_HC_No_Red.drop([0], axis = 1)
Accept_HC_No_Red.columns = lhs.Run

Accept_Heads_No_Red= Accept_Heads_No_Red.drop([0], axis = 1)
Accept_Heads_No_Red.columns = lhs.Run

## Be sure to change the folder!
from pathlib import Path

Path('./Evaluation_Data/Projection/LI/').mkdir(parents = True, exist_ok = True)


Accept_HC_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_HC_30_No_Red.csv')
Accept_Heads_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Heads_30_No_Red.csv')

Accept_Full_HC_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Full_HC_30_No_Red.csv')
Accept_Full_Heads_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_30_No_Red.csv') 

#%% 20% Reduction

Accept_HC_No_Red = pd.DataFrame(data = [0], index = [99])
Accept_Heads_No_Red = pd.DataFrame(data = [0], index = [99])

Accept_Full_HC_No_Red = pd.DataFrame(data = [0], index = [54])
Accept_Full_Heads_No_Red = pd.DataFrame(data = [0], index = [55])


accept_runs = []

# Read in data from MODFLOW runs and populate a pandas dataframe 
for i in range(0, len(lhs), 1):
    
    AnnHeads = pd.read_csv('./Outputs/Proj_Heads/LI/30_Percent/'
                           '/JanAnnHeads_Run_%s.csv' % (lhs.Run[i]))
    AnnHeads_HC = AnnHeads.diff(axis = 0)
    AnnHeads_HC = AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)

    
    Accept_HC_No_Red = pd.concat([Accept_HC_No_Red, pd.DataFrame(AnnHeads_HC.iloc[99:119, 24])], axis = 1)
    Accept_Heads_No_Red = pd.concat([Accept_Heads_No_Red, pd.DataFrame(AnnHeads.iloc[99:120, 24])], axis = 1)

    Accept_Full_HC_No_Red = pd.concat([Accept_Full_HC_No_Red, pd.DataFrame(AnnHeads_HC.iloc[54:, 24])], axis = 1)
    Accept_Full_Heads_No_Red = pd.concat([Accept_Full_Heads_No_Red, pd.DataFrame(AnnHeads.iloc[55:, 24])], axis = 1)


## Drop first column as it is a holder and then rename all columns to the 
## correct run.
##
# Good Runs
Accept_HC_No_Red = Accept_HC_No_Red.drop([0], axis = 1)
Accept_HC_No_Red.columns = lhs.Run

Accept_Heads_No_Red= Accept_Heads_No_Red.drop([0], axis = 1)
Accept_Heads_No_Red.columns = lhs.Run

## Be sure to change the folder!
from pathlib import Path

Path('./Evaluation_Data/Projection/LI/').mkdir(parents = True, exist_ok = True)


Accept_HC_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_HC_30.csv')
Accept_Heads_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Heads_30.csv')

Accept_Full_HC_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Full_HC_30.csv')
Accept_Full_Heads_No_Red.to_csv('./Evaluation_Data/Projection/LI/Accept_Full_Heads_30.csv')









