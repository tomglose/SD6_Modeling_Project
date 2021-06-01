# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:13:23 2020

@author: tomglose
"""

import os
import pandas as pd
from pathlib import Path


working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Figures/').mkdir(parents = True, exist_ok = True)

# Read in LHS variables

lhs = pd.read_csv('./Inputs/Proj_LHS_Recharge.csv')
lhs.columns = ['Run', 'K_v', 'Sy', 'Rech', 'EPS']
lhs['Run'] = lhs['Run'] + 1


# Read in data from .csv files that contain real data from SD_6, format, and organize

hc_file = ('./Validation/Year_to_Year_Head_Change.csv')
dtw_file = ('./Validation/Year_to_Year_Heads.csv')

# Change in head
hc = pd.read_csv(hc_file, usecols = ['Average'])
hc_std = pd.read_csv(hc_file, usecols = ['Standard Deviation'])

# Depth to water
heads = pd.read_csv(dtw_file, usecols = ['Average'])
heads_std = pd.read_csv(dtw_file, usecols = ['Standard Deviation'])


Cal_HC = pd.DataFrame(data = [0], index = [99])
Cal_Heads = pd.DataFrame(data = [0], index = [99])

Full_Heads_BAU_9 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_10 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_11 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_12 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_13 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_14 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_15 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_16 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_17 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_18 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_19 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_20 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_21 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_22 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_23 = pd.DataFrame(data = [0], index = [55])


good_runs = []

# Read in data from MODFLOW runs and populate a pandas dataframe 
for i in range(0, len(lhs), 1):
    AnnHeads = pd.read_csv('./Outputs/Proj_Heads/Rech/20_Percent/'
                           '/JanAnnHeads_Run_%s.csv' % (lhs.Run[i]))
    
    AnnHeads_HC = AnnHeads.diff(axis = 0)
    AnnHeads_HC = AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)
    
    Cal_HC = pd.concat([Cal_HC, pd.DataFrame(AnnHeads_HC.iloc[99:119, 24])], axis = 1)
    Cal_Heads = pd.concat([Cal_Heads, pd.DataFrame(AnnHeads.iloc[99:120, 24])], axis = 1)


    Full_Heads_BAU_9 = pd.concat([Full_Heads_BAU_9, pd.DataFrame(AnnHeads.iloc[55:, 9])], axis = 1)
    Full_Heads_BAU_10 = pd.concat([Full_Heads_BAU_10, pd.DataFrame(AnnHeads.iloc[55:, 10])], axis = 1)
    Full_Heads_BAU_11 = pd.concat([Full_Heads_BAU_11, pd.DataFrame(AnnHeads.iloc[55:, 11])], axis = 1)
    Full_Heads_BAU_12 = pd.concat([Full_Heads_BAU_12, pd.DataFrame(AnnHeads.iloc[55:, 12])], axis = 1)
    Full_Heads_BAU_13 = pd.concat([Full_Heads_BAU_13, pd.DataFrame(AnnHeads.iloc[55:, 13])], axis = 1)
    Full_Heads_BAU_14 = pd.concat([Full_Heads_BAU_14, pd.DataFrame(AnnHeads.iloc[55:, 14])], axis = 1)
    Full_Heads_BAU_15 = pd.concat([Full_Heads_BAU_15, pd.DataFrame(AnnHeads.iloc[55:, 15])], axis = 1)
    Full_Heads_BAU_16 = pd.concat([Full_Heads_BAU_16, pd.DataFrame(AnnHeads.iloc[55:, 16])], axis = 1)
    Full_Heads_BAU_17 = pd.concat([Full_Heads_BAU_17, pd.DataFrame(AnnHeads.iloc[55:, 17])], axis = 1)
    Full_Heads_BAU_18 = pd.concat([Full_Heads_BAU_18, pd.DataFrame(AnnHeads.iloc[55:, 18])], axis = 1)
    Full_Heads_BAU_19 = pd.concat([Full_Heads_BAU_19, pd.DataFrame(AnnHeads.iloc[55:, 19])], axis = 1)
    Full_Heads_BAU_20 = pd.concat([Full_Heads_BAU_20, pd.DataFrame(AnnHeads.iloc[55:, 20])], axis = 1)
    Full_Heads_BAU_21 = pd.concat([Full_Heads_BAU_21, pd.DataFrame(AnnHeads.iloc[55:, 21])], axis = 1)
    Full_Heads_BAU_22 = pd.concat([Full_Heads_BAU_22, pd.DataFrame(AnnHeads.iloc[55:, 22])], axis = 1)
    Full_Heads_BAU_23 = pd.concat([Full_Heads_BAU_23, pd.DataFrame(AnnHeads.iloc[55:, 23])], axis = 1)



## Drop first column as it is a holder and then rename all columns to the 
## correct run.
##
# Good Runs
Cal_HC = Cal_HC.drop([0], axis = 1)
Cal_HC.columns = lhs.Run

Cal_Heads= Cal_Heads.drop([0], axis = 1)
Cal_Heads.columns = lhs.Run


##
## Be sure to change the folder!
##

working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Outputs/BAU_Heads/Rech/20_Percent').mkdir(parents = True, exist_ok = True)

Full_Heads_BAU_9.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_9.csv')
Full_Heads_BAU_10.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_10.csv') 
Full_Heads_BAU_11.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_11.csv') 
Full_Heads_BAU_12.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_12.csv') 
Full_Heads_BAU_13.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_13.csv') 
Full_Heads_BAU_14.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_14.csv') 
Full_Heads_BAU_15.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_15.csv') 
Full_Heads_BAU_16.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_16.csv') 
Full_Heads_BAU_17.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_17.csv')
Full_Heads_BAU_17.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_17.csv')
Full_Heads_BAU_18.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_18.csv')
Full_Heads_BAU_19.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_19.csv')
Full_Heads_BAU_20.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_20.csv')
Full_Heads_BAU_21.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_21.csv')
Full_Heads_BAU_22.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_22.csv')
Full_Heads_BAU_23.to_csv('./Outputs/BAU_Heads/Rech/20_Percent/Full_Heads_BAU_23.csv')  

#%%
# Repeat for 30% Reduction
Cal_HC = pd.DataFrame(data = [0], index = [99])
Cal_Heads = pd.DataFrame(data = [0], index = [99])

Full_Heads_BAU_9 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_10 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_11 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_12 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_13 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_14 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_15 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_16 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_17 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_18 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_19 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_20 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_21 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_22 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_23 = pd.DataFrame(data = [0], index = [55])


good_runs = []

# Read in data from MODFLOW runs and populate a pandas dataframe 
for i in range(0, len(lhs), 1):
    AnnHeads = pd.read_csv('./Outputs/Proj_Heads/Rech/30_Percent/'
                           '/JanAnnHeads_Run_%s.csv' % (lhs.Run[i]))
    
    AnnHeads_HC = AnnHeads.diff(axis = 0)
    AnnHeads_HC = AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)
    
    Cal_HC = pd.concat([Cal_HC, pd.DataFrame(AnnHeads_HC.iloc[99:119, 24])], axis = 1)
    Cal_Heads = pd.concat([Cal_Heads, pd.DataFrame(AnnHeads.iloc[99:120, 24])], axis = 1)


    Full_Heads_BAU_9 = pd.concat([Full_Heads_BAU_9, pd.DataFrame(AnnHeads.iloc[55:, 9])], axis = 1)
    Full_Heads_BAU_10 = pd.concat([Full_Heads_BAU_10, pd.DataFrame(AnnHeads.iloc[55:, 10])], axis = 1)
    Full_Heads_BAU_11 = pd.concat([Full_Heads_BAU_11, pd.DataFrame(AnnHeads.iloc[55:, 11])], axis = 1)
    Full_Heads_BAU_12 = pd.concat([Full_Heads_BAU_12, pd.DataFrame(AnnHeads.iloc[55:, 12])], axis = 1)
    Full_Heads_BAU_13 = pd.concat([Full_Heads_BAU_13, pd.DataFrame(AnnHeads.iloc[55:, 13])], axis = 1)
    Full_Heads_BAU_14 = pd.concat([Full_Heads_BAU_14, pd.DataFrame(AnnHeads.iloc[55:, 14])], axis = 1)
    Full_Heads_BAU_15 = pd.concat([Full_Heads_BAU_15, pd.DataFrame(AnnHeads.iloc[55:, 15])], axis = 1)
    Full_Heads_BAU_16 = pd.concat([Full_Heads_BAU_16, pd.DataFrame(AnnHeads.iloc[55:, 16])], axis = 1)
    Full_Heads_BAU_17 = pd.concat([Full_Heads_BAU_17, pd.DataFrame(AnnHeads.iloc[55:, 17])], axis = 1)
    Full_Heads_BAU_18 = pd.concat([Full_Heads_BAU_18, pd.DataFrame(AnnHeads.iloc[55:, 18])], axis = 1)
    Full_Heads_BAU_19 = pd.concat([Full_Heads_BAU_19, pd.DataFrame(AnnHeads.iloc[55:, 19])], axis = 1)
    Full_Heads_BAU_20 = pd.concat([Full_Heads_BAU_20, pd.DataFrame(AnnHeads.iloc[55:, 20])], axis = 1)
    Full_Heads_BAU_21 = pd.concat([Full_Heads_BAU_21, pd.DataFrame(AnnHeads.iloc[55:, 21])], axis = 1)
    Full_Heads_BAU_22 = pd.concat([Full_Heads_BAU_22, pd.DataFrame(AnnHeads.iloc[55:, 22])], axis = 1)
    Full_Heads_BAU_23 = pd.concat([Full_Heads_BAU_23, pd.DataFrame(AnnHeads.iloc[55:, 23])], axis = 1)



## Drop first column as it is a holder and then rename all columns to the 
## correct run.
##
# Good Runs
Cal_HC = Cal_HC.drop([0], axis = 1)
Cal_HC.columns = lhs.Run

Cal_Heads= Cal_Heads.drop([0], axis = 1)
Cal_Heads.columns = lhs.Run


##
## Be sure to change the folder!
##

working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Outputs/BAU_Heads/Rech/30_Percent').mkdir(parents = True, exist_ok = True)


Full_Heads_BAU_9.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_9.csv')
Full_Heads_BAU_10.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_10.csv') 
Full_Heads_BAU_11.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_11.csv') 
Full_Heads_BAU_12.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_12.csv') 
Full_Heads_BAU_13.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_13.csv') 
Full_Heads_BAU_14.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_14.csv') 
Full_Heads_BAU_15.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_15.csv') 
Full_Heads_BAU_16.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_16.csv') 
Full_Heads_BAU_17.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_17.csv')
Full_Heads_BAU_17.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_17.csv')
Full_Heads_BAU_18.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_18.csv')
Full_Heads_BAU_19.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_19.csv')
Full_Heads_BAU_20.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_20.csv')
Full_Heads_BAU_21.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_21.csv')
Full_Heads_BAU_22.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_22.csv')
Full_Heads_BAU_23.to_csv('./Outputs/BAU_Heads/Rech/30_Percent/Full_Heads_BAU_23.csv')  


#%%
# Repeat for no reduction
Cal_HC = pd.DataFrame(data = [0], index = [99])
Cal_Heads = pd.DataFrame(data = [0], index = [99])

Full_Heads_BAU_9 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_10 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_11 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_12 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_13 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_14 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_15 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_16 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_17 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_18 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_19 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_20 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_21 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_22 = pd.DataFrame(data = [0], index = [55])
Full_Heads_BAU_23 = pd.DataFrame(data = [0], index = [55])


good_runs = []

# Read in data from MODFLOW runs and populate a pandas dataframe 
for i in range(0, len(lhs), 1):
    AnnHeads = pd.read_csv('./Outputs/Proj_Heads/Rech_No_Red/30_Percent/'
                           '/JanAnnHeads_Run_%s.csv' % (lhs.Run[i]))
    
    AnnHeads_HC = AnnHeads.diff(axis = 0)
    AnnHeads_HC = AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)
    
    Cal_HC = pd.concat([Cal_HC, pd.DataFrame(AnnHeads_HC.iloc[99:119, 24])], axis = 1)
    Cal_Heads = pd.concat([Cal_Heads, pd.DataFrame(AnnHeads.iloc[99:120, 24])], axis = 1)


    Full_Heads_BAU_9 = pd.concat([Full_Heads_BAU_9, pd.DataFrame(AnnHeads.iloc[55:, 9])], axis = 1)
    Full_Heads_BAU_10 = pd.concat([Full_Heads_BAU_10, pd.DataFrame(AnnHeads.iloc[55:, 10])], axis = 1)
    Full_Heads_BAU_11 = pd.concat([Full_Heads_BAU_11, pd.DataFrame(AnnHeads.iloc[55:, 11])], axis = 1)
    Full_Heads_BAU_12 = pd.concat([Full_Heads_BAU_12, pd.DataFrame(AnnHeads.iloc[55:, 12])], axis = 1)
    Full_Heads_BAU_13 = pd.concat([Full_Heads_BAU_13, pd.DataFrame(AnnHeads.iloc[55:, 13])], axis = 1)
    Full_Heads_BAU_14 = pd.concat([Full_Heads_BAU_14, pd.DataFrame(AnnHeads.iloc[55:, 14])], axis = 1)
    Full_Heads_BAU_15 = pd.concat([Full_Heads_BAU_15, pd.DataFrame(AnnHeads.iloc[55:, 15])], axis = 1)
    Full_Heads_BAU_16 = pd.concat([Full_Heads_BAU_16, pd.DataFrame(AnnHeads.iloc[55:, 16])], axis = 1)
    Full_Heads_BAU_17 = pd.concat([Full_Heads_BAU_17, pd.DataFrame(AnnHeads.iloc[55:, 17])], axis = 1)
    Full_Heads_BAU_18 = pd.concat([Full_Heads_BAU_18, pd.DataFrame(AnnHeads.iloc[55:, 18])], axis = 1)
    Full_Heads_BAU_19 = pd.concat([Full_Heads_BAU_19, pd.DataFrame(AnnHeads.iloc[55:, 19])], axis = 1)
    Full_Heads_BAU_20 = pd.concat([Full_Heads_BAU_20, pd.DataFrame(AnnHeads.iloc[55:, 20])], axis = 1)
    Full_Heads_BAU_21 = pd.concat([Full_Heads_BAU_21, pd.DataFrame(AnnHeads.iloc[55:, 21])], axis = 1)
    Full_Heads_BAU_22 = pd.concat([Full_Heads_BAU_22, pd.DataFrame(AnnHeads.iloc[55:, 22])], axis = 1)
    Full_Heads_BAU_23 = pd.concat([Full_Heads_BAU_23, pd.DataFrame(AnnHeads.iloc[55:, 23])], axis = 1)



## Drop first column as it is a holder and then rename all columns to the 
## correct run.
##
# Good Runs
Cal_HC = Cal_HC.drop([0], axis = 1)
Cal_HC.columns = lhs.Run

Cal_Heads= Cal_Heads.drop([0], axis = 1)
Cal_Heads.columns = lhs.Run


##
## Be sure to change the folder!
##

working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Outputs/BAU_Heads/Rech_No_Red/30_Percent').mkdir(parents = True, exist_ok = True)


Full_Heads_BAU_9.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_9.csv')
Full_Heads_BAU_10.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_10.csv') 
Full_Heads_BAU_11.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_11.csv') 
Full_Heads_BAU_12.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_12.csv') 
Full_Heads_BAU_13.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_13.csv') 
Full_Heads_BAU_14.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_14.csv') 
Full_Heads_BAU_15.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_15.csv') 
Full_Heads_BAU_16.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_16.csv') 
Full_Heads_BAU_17.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_17.csv')
Full_Heads_BAU_17.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_17.csv')
Full_Heads_BAU_18.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_18.csv')
Full_Heads_BAU_19.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_19.csv')
Full_Heads_BAU_20.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_20.csv')
Full_Heads_BAU_21.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_21.csv')
Full_Heads_BAU_22.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_22.csv')
Full_Heads_BAU_23.to_csv('./Outputs/BAU_Heads/Rech_No_Red/30_Percent/Full_Heads_BAU_23.csv')  
