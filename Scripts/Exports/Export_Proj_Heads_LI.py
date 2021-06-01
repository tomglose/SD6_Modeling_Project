# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:28:52 2021

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

Path('./Outputs/Proj_Heads/LI/20_Percent').mkdir(parents = True, exist_ok = True)


lhs = pd.read_csv('./Inputs/Proj_LHS_Lat_Inflow.csv')

lhs.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']

lhs.Run = lhs.Run + 1

for a in range(0, len(lhs), 1):
    os.chdir('./Data/Projection/LI/20_Percent/Run_%s' % (lhs.Run[a]))
    
    modelname = 'Run_%s' % (lhs.Run[a])
    
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
    JanHeads.to_csv('./Outputs/Proj_Heads/LI/20_Percent/JanAnnHeads_Run_%s.csv' % (lhs.Run[a]), 
                    index = None)


Path('./Outputs/Proj_Heads/LI/30_Percent').mkdir(parents = True, exist_ok = True)


for a in range(0, len(lhs), 1):
    os.chdir('./Data/Projection/LI/30_Percent/Run_%s' % (lhs.Run[a]))
    
    modelname = 'Run_%s' % (lhs.Run[a])
    
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
    JanHeads.to_csv('./Outputs/Proj_Heads/LI/30_Percent/JanAnnHeads_Run_%s.csv' % (lhs.Run[a]), 
                    index = None)
    



#%% No Reduction
Path('./Outputs/Proj_Heads/LI_No_Red/20_Percent').mkdir(parents = True, exist_ok = True)

for a in range(0, len(lhs), 1):
    os.chdir('./Data/Projection/LI_No_Red/20_Percent/Run_%s' % (lhs.Run[a]))
    
    modelname = 'Run_%s' % (lhs.Run[a])
    
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
    JanHeads.to_csv('./Outputs/Proj_Heads/LI_No_Red/20_Percent/JanAnnHeads_Run_%s.csv' % (lhs.Run[a]), 
                    index = None)


Path('./Outputs/Proj_Heads/LI_No_Red/30_Percent').mkdir(parents = True, exist_ok = True)


for a in range(0, len(lhs), 1):
    os.chdir('./Data/Projection/LI_No_Red/30_Percent/Run_%s' % (lhs.Run[a]))
    
    modelname = 'Run_%s' % (lhs.Run[a])
    
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
    JanHeads.to_csv('./Outputs/Proj_Heads/LI_No_Red/30_Percent/JanAnnHeads_Run_%s.csv' % (lhs.Run[a]), 
                    index = None)