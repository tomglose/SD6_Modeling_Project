# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:13:23 2020

@author: tomglose
"""

import os
import flopy.utils.mflistfile as lst
import pandas as pd


working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

# Paths
val_path = './Validation/'
# heads_path = './Outputs/Eval_Heads'

# Read in LHS variables

lhs = pd.read_csv('./Inputs/Eval_LHS_Parameters.csv')

# Read in data from .csv files that contain real data from SD_6, format, and organize

hc_file = ('./Validation/Year_to_Year_Head_Change.csv')
dtw_file = ('./Validation/Year_to_Year_Heads.csv')

# Change in head
hc = pd.read_csv(hc_file, usecols = ['Average'])
hc_std = pd.read_csv(hc_file, usecols = ['Standard Deviation'])

# Depth to water
heads = pd.read_csv(dtw_file, usecols = ['Average'])
heads_std = pd.read_csv(dtw_file, usecols = ['Standard Deviation'])



Accept_HC = pd.DataFrame(data = [0], index = [99])
Accept_Heads = pd.DataFrame(data = [0], index = [99])

Reject_HC = pd.DataFrame(data = [0], index = [99])
Reject_Heads = pd.DataFrame(data = [0], index = [99])

accept_runs = []
reject_runs = []


# Read in data from MODFLOW runs and populate a pandas dataframe 
for i in range(1, len(lhs) + 1, 1):

    
    mf_list = lst.MfListBudget('./Data/Evaluation/Run_%s/'
                                'Run_%s.list' % (i, i))

    kstpkper = mf_list.get_kstpkper()
    data = mf_list.get_data(kstpkper = kstpkper[-1], incremental = True)

    if data.value[12] != 0:
        reject_runs.append(i)
        
        Bad_AnnHeads = pd.read_csv('./Outputs/Eval_Heads/'
                                   'JanAnnHeads_Run_%s.csv' % (i))
        Bad_AnnHeads_HC = Bad_AnnHeads.diff(axis = 0)
        Bad_AnnHeads_HC = Bad_AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)

        
        Reject_HC = pd.concat([Reject_HC, pd.DataFrame(Bad_AnnHeads_HC.iloc[99:119, 24])], axis = 1)
        Reject_Heads = pd.concat([Reject_Heads, pd.DataFrame(Bad_AnnHeads.iloc[99:120, 24])], axis = 1)
             
    else:
        accept_runs.append(i)
        
        AnnHeads = pd.read_csv('./Outputs/Eval_Heads/'
                               '/JanAnnHeads_Run_%s.csv' % (i))
        AnnHeads_HC = AnnHeads.diff(axis = 0)
        AnnHeads_HC = AnnHeads_HC.drop([0], axis = 0).reset_index().drop(['index'], axis = 1)

        
        Accept_HC = pd.concat([Accept_HC, pd.DataFrame(AnnHeads_HC.iloc[99:119, 24])], axis = 1)
        Accept_Heads = pd.concat([Accept_Heads, pd.DataFrame(AnnHeads.iloc[99:120, 24])], axis = 1)


#%%
## Drop first column as it is a holder and then rename all columns to the 
## correct run.
##
# Good Runs
Accept_HC = Accept_HC.drop([0], axis = 1)
Accept_HC.columns = accept_runs

Accept_Heads= Accept_Heads.drop([0], axis = 1)
Accept_Heads.columns = accept_runs


#Bad Runs
Reject_HC = Reject_HC.drop([0], axis = 1)
Reject_HC.columns = reject_runs

Reject_Heads = Reject_Heads.drop([0], axis = 1)
Reject_Heads.columns = reject_runs

##
## Be sure to change the folder!
##
from pathlib import Path

Path('./Evaluation_Data/').mkdir(parents = True, exist_ok = True)


Accept_HC.to_csv('./Evaluation_Data/Evaluation/Accept_HC.csv')
Accept_Heads.to_csv('./Evaluation_Data/Evaluation/Accept_Heads.csv')

Reject_HC.to_csv('./Evaluation_Data/Evaluation/Reject_HC.csv') 
Reject_Heads.to_csv('./Evaluation_Data/Evaluation/Reject_Heads.csv') 
 














