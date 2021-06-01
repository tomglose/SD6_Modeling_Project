# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 10:11:07 2020

@author: tomglose
"""

import pandas as pd
import os



working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

lhs = pd.read_csv('./Inputs/Eval_LHS_Parameters.csv')
eval_ind = pd.read_csv('./Inputs/High_KGE_Index_Eval.csv', 
                   index_col = 0).stack().tolist()

eval_ind = [(i - 1) for i in eval_ind]

lhs_li = lhs.loc[eval_ind].query('LI > 0.0001')
lhs_rec = lhs.loc[eval_ind].query('LI < 0.0001')

lhs_li.to_csv('./Inputs/Proj_LHS_Lat_Inflow.csv')
lhs_rec.to_csv('./Inputs/Proj_LHS_Recharge.csv')

