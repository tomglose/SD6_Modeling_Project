# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:20:03 2020

@author: tomglose
"""
from pathlib import Path
import os
import pandas as pd
import numpy as np
import flopy.utils.binaryfile as bf 
from flopy.utils.zonbud import ZoneBudget, read_zbarray, write_zbarray


# Change directory to working folder <- be sure to change
working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)

# Import Latin Hypercube Sampling parameters to be used in model runs
lhs = pd.read_csv('./Inputs/Proj_LHS_Recharge.csv')

lhs.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs.Run = lhs.Run + 1

Path('./Outputs/Zone_Budgets/Rech/20_Percent/').mkdir(parents = True, exist_ok = True)

for a in range(0, len(lhs), 1):
    os.chdir('./Data/Projection/Rech/20_Percent/Run_%s' % (lhs.Run[a]))
    
    modelname = 'Run_%s' % (lhs.Run[a])
    
    hds = bf.HeadFile(modelname + '.hds')
    hds_time = hds.get_times()
    hds_kstpkper = hds.get_kstpkper()

    
    # Creates the zone array to be used
    zone_array = np.zeros((1,50), dtype = 'float64')
    zone_array[0, 4:18] = 1
    zone_array[0, 18:32] = 2
    zone_array[0, 32:46] = 3
    
    # Writes the zone array to a file to be read by FloPy
    write_zbarray('zon_array.zbr', zone_array)
    
    # Reads the file just created
    zon = read_zbarray('zon_array.zbr')
    
    # Calculates the zone budget
    zb = ZoneBudget(modelname + '.cbc', zon, kstpkper= hds_kstpkper)
    
    # Moves the zone budget to a dataframe for further analysis
    df = zb.get_dataframes()
    
    zb_1 = df.pop('ZONE_1')
    zb_2 = df.pop('ZONE_2')
    zb_3 = df.pop('ZONE_3')
    
    zb_1 = zb_1.to_frame()
    zb_2 = zb_2.to_frame()
    zb_3 = zb_3.to_frame()
    
    zb_1 = zb_1.unstack(level = 'name')
    zb_2 = zb_2.unstack(level = 'name')
    zb_3 = zb_3.unstack(level = 'name')
        
    zb_1.index.names = ['Time']
    zb_2.index.names = ['Time']
    zb_3.index.names = ['Time']
    
    zb_1.columns = zb_1.columns.droplevel()
    zb_2.columns = zb_2.columns.droplevel()
    zb_3.columns = zb_3.columns.droplevel()

    # # Save Zone Budgets for sperate zones to .csv files
    working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
    os.chdir(working_folder)
    
    zb_1.to_csv('./Outputs/Zone_Budgets/Rech/20_Percent/'
     'Zon1_Run_%s.csv' % (lhs.Run[a]))
    zb_2.to_csv('./Outputs/Zone_Budgets/Rech/20_Percent/'
     'Zon2_Run_%s.csv' % (lhs.Run[a]))
    zb_3.to_csv('./Outputs/Zone_Budgets/Rech/20_Percent/'
     'Zon3_Run_%s.csv' % (lhs.Run[a]))    
    
    
Path('./Outputs/Zone_Budgets/Rech/30_Percent/').mkdir(parents = True, exist_ok = True)

for a in range(0, len(lhs), 1):
    os.chdir('./Data/Projection/Rech/30_Percent/Run_%s' % (lhs.Run[a]))
    
    modelname = 'Run_%s' % (lhs.Run[a])
    
    hds = bf.HeadFile(modelname + '.hds')
    hds_time = hds.get_times()
    hds_kstpkper = hds.get_kstpkper()

    
    # Creates the zone array to be used
    zone_array = np.zeros((1,50), dtype = 'float64')
    zone_array[0, 4:18] = 1
    zone_array[0, 18:32] = 2
    zone_array[0, 32:46] = 3
    
    # Writes the zone array to a file to be read by FloPy
    write_zbarray('zon_array.zbr', zone_array)
    
    # Reads the file just created
    zon = read_zbarray('zon_array.zbr')
    
    # Calculates the zone budget
    zb = ZoneBudget(modelname + '.cbc', zon, kstpkper= hds_kstpkper)
    
    # Moves the zone budget to a dataframe for further analysis
    df = zb.get_dataframes()
    
    zb_1 = df.pop('ZONE_1')
    zb_2 = df.pop('ZONE_2')
    zb_3 = df.pop('ZONE_3')
    
    zb_1 = zb_1.to_frame()
    zb_2 = zb_2.to_frame()
    zb_3 = zb_3.to_frame()
    
    zb_1 = zb_1.unstack(level = 'name')
    zb_2 = zb_2.unstack(level = 'name')
    zb_3 = zb_3.unstack(level = 'name')
        
    zb_1.index.names = ['Time']
    zb_2.index.names = ['Time']
    zb_3.index.names = ['Time']
    
    zb_1.columns = zb_1.columns.droplevel()
    zb_2.columns = zb_2.columns.droplevel()
    zb_3.columns = zb_3.columns.droplevel()

    # # Save Zone Budgets for sperate zones to .csv files
    working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
    os.chdir(working_folder)
    
    
    zb_1.to_csv('./Outputs/Zone_Budgets/Rech/30_Percent/'
     'Zon1_Run_%s.csv' % (lhs.Run[a]))
    zb_2.to_csv('./Outputs/Zone_Budgets/Rech/30_Percent/'
     'Zon2_Run_%s.csv' % (lhs.Run[a]))
    zb_3.to_csv('./Outputs/Zone_Budgets/Rech/30_Percent/'
     'Zon3_Run_%s.csv' % (lhs.Run[a]))    



Path('./Outputs/Zone_Budgets/Rech_No_Red/20_Percent/').mkdir(parents = True, exist_ok = True)

for a in range(0, len(lhs), 1):
    os.chdir('./Data/Projection/Rech_No_Red/20_Percent/Run_%s' % (lhs.Run[a]))
    
    modelname = 'Run_%s' % (lhs.Run[a])
    
    hds = bf.HeadFile(modelname + '.hds')
    hds_time = hds.get_times()
    hds_kstpkper = hds.get_kstpkper()

    
    # Creates the zone array to be used
    zone_array = np.zeros((1,50), dtype = 'float64')
    zone_array[0, 4:18] = 1
    zone_array[0, 18:32] = 2
    zone_array[0, 32:46] = 3
    
    # Writes the zone array to a file to be read by FloPy
    write_zbarray('zon_array.zbr', zone_array)
    
    # Reads the file just created
    zon = read_zbarray('zon_array.zbr')
    
    # Calculates the zone budget
    zb = ZoneBudget(modelname + '.cbc', zon, kstpkper= hds_kstpkper)
    
    # Moves the zone budget to a dataframe for further analysis
    df = zb.get_dataframes()
    
    zb_1 = df.pop('ZONE_1')
    zb_2 = df.pop('ZONE_2')
    zb_3 = df.pop('ZONE_3')
    
    zb_1 = zb_1.to_frame()
    zb_2 = zb_2.to_frame()
    zb_3 = zb_3.to_frame()
    
    zb_1 = zb_1.unstack(level = 'name')
    zb_2 = zb_2.unstack(level = 'name')
    zb_3 = zb_3.unstack(level = 'name')
        
    zb_1.index.names = ['Time']
    zb_2.index.names = ['Time']
    zb_3.index.names = ['Time']
    
    zb_1.columns = zb_1.columns.droplevel()
    zb_2.columns = zb_2.columns.droplevel()
    zb_3.columns = zb_3.columns.droplevel()

    # # Save Zone Budgets for sperate zones to .csv files
    working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
    os.chdir(working_folder)

    
    zb_1.to_csv('./Outputs/Zone_Budgets/Rech_No_Red/20_Percent/'
     'Zon1_Run_%s.csv' % (lhs.Run[a]))
    zb_2.to_csv('./Outputs/Zone_Budgets/Rech_No_Red/20_Percent/'
     'Zon2_Run_%s.csv' % (lhs.Run[a]))
    zb_3.to_csv('./Outputs/Zone_Budgets/Rech_No_Red/20_Percent/'
     'Zon3_Run_%s.csv' % (lhs.Run[a])) 
    
    
Path('./Outputs/Zone_Budgets/Rech_No_Red/30_Percent/').mkdir(parents = True, exist_ok = True)

for a in range(0, len(lhs), 1):
    os.chdir('./Data/Projection/Rech_No_Red/30_Percent/Run_%s' % (lhs.Run[a]))
    
    modelname = 'Run_%s' % (lhs.Run[a])
    
    hds = bf.HeadFile(modelname + '.hds')
    hds_time = hds.get_times()
    hds_kstpkper = hds.get_kstpkper()

    
    # Creates the zone array to be used
    zone_array = np.zeros((1,50), dtype = 'float64')
    zone_array[0, 4:18] = 1
    zone_array[0, 18:32] = 2
    zone_array[0, 32:46] = 3
    
    # Writes the zone array to a file to be read by FloPy
    write_zbarray('zon_array.zbr', zone_array)
    
    # Reads the file just created
    zon = read_zbarray('zon_array.zbr')
    
    # Calculates the zone budget
    zb = ZoneBudget(modelname + '.cbc', zon, kstpkper= hds_kstpkper)
    
    # Moves the zone budget to a dataframe for further analysis
    df = zb.get_dataframes()
    
    zb_1 = df.pop('ZONE_1')
    zb_2 = df.pop('ZONE_2')
    zb_3 = df.pop('ZONE_3')
    
    zb_1 = zb_1.to_frame()
    zb_2 = zb_2.to_frame()
    zb_3 = zb_3.to_frame()
    
    zb_1 = zb_1.unstack(level = 'name')
    zb_2 = zb_2.unstack(level = 'name')
    zb_3 = zb_3.unstack(level = 'name')
        
    zb_1.index.names = ['Time']
    zb_2.index.names = ['Time']
    zb_3.index.names = ['Time']
    
    zb_1.columns = zb_1.columns.droplevel()
    zb_2.columns = zb_2.columns.droplevel()
    zb_3.columns = zb_3.columns.droplevel()

    # # Save Zone Budgets for sperate zones to .csv files
    working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
    os.chdir(working_folder)
    
    zb_1.to_csv('./Outputs/Zone_Budgets/Rech_No_Red/30_Percent/'
     'Zon1_Run_%s.csv' % (lhs.Run[a]))
    zb_2.to_csv('./Outputs/Zone_Budgets/Rech_No_Red/30_Percent/'
     'Zon2_Run_%s.csv' % (lhs.Run[a]))
    zb_3.to_csv('./Outputs/Zone_Budgets/Rech_No_Red/30_Percent/'
     'Zon3_Run_%s.csv' % (lhs.Run[a])) 