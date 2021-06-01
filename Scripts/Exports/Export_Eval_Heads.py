# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:02:28 2020

@author: tomglose
"""

from pathlib import Path
import pandas as pd
import os
import flopy.utils.binaryfile as bf 
import numpy as np
import math


working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

Path('./Outputs/Eval_Heads/').mkdir(parents = True, exist_ok = True)

lhs = pd.read_csv('./Inputs/Eval_LHS_Parameters.csv')

for a in range(1, len(lhs) + 1, 1):
    os.chdir('./Data/Evaluation/Run_%s' % (a))
    
    modelname = 'Run_%s' % (a)
    
    hds = bf.HeadFile(modelname + '.hds')
    hds_time = hds.get_times()
    hds_kstpkper = hds.get_kstpkper()
    hds_alldata = hds.get_alldata()
    
    # Gathering all heads into one variable
    hds_data = np.ones([len(hds_time),hds_alldata.shape[3]])
    
    for i in range(len(hds_time)):
        hds_data[i,:] = hds.get_data(totim = int(hds_time[i]))
    
    
    # Generates annual head data (Jan. 1)
    JanHeads = np.ones([int(math.ceil(len(hds_time)/12)),50])
    
    k = 0;
    for i in range(3,len(hds_time),12):
        JanHeads[k,:] = hds_data[i,:]
        k = k+1;
    
    JanHeads = pd.DataFrame(data = JanHeads)
    
    os.chdir(working_folder)
    JanHeads.to_csv('./Outputs/Eval_Heads/JanAnnHeads_Run_%s.csv' % (a), 
                    index = None)
    
            
    
            