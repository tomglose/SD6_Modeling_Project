# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:59:00 2020

@author: tomglose
"""

from pathlib import Path
import os
import csv
import numpy as np
import flopy
import pandas as pd

# Change directory to working folder <- be sure to change
working_folder = 'C:/Users/tomglose/Desktop/SD_6_Surrogate_Modeling/'
os.chdir(working_folder)


# Import Latin Hypercube Sampling parameters to be used in model runs
lhs = pd.read_csv('./Inputs/Proj_LHS_Lat_Inflow.csv')

# Set absolute path to modflow executeable

modflow = (working_folder + 'MODFLOW_Executables/')

path2mf = modflow + 'mfnwt'
 

lhs.columns = ['Run', 'K_v', 'Sy', 'LI', 'EPS']
lhs.Run = lhs.Run + 1


# 20% pumping reduction scenario for lateral inflow dominated parameters
for k in range(0, len(lhs), 1):
    Lx = 40000.
    Ly = 800.
    ztop = 72.
    zbot = 0.
    nlay = 1
    nrow = 1
    ncol = 50
    delr = Lx/ncol
    delc = Ly/nrow
    botm = 0
    ss = 1E-5
    
    hk = 20
    vk = lhs.K_v[k]
    sy = lhs.Sy[k]
    LI = lhs.LI[k]
    eps = lhs.EPS[k]
    thts = 0.25
    thtr = thts - lhs.Sy[k]
    thti = (thts - lhs.Sy[k]) + 0.005
    modelname = 'Run_%s' % (lhs.Run[k])
    
    # Model name
    mf = flopy.modflow.Modflow(modelname, version = 'mfnwt',
                               exe_name = path2mf)
    
    # Stress period and time step setup
    nper = 401
    perlen = np.empty((401,), dtype = np.int32)
    perlen[::2] = perlen[::2] = 262
    perlen[1::2] = perlen[1::2] = 103
    nstp = np.empty((401,), dtype = np.int32)
    nstp[::2] = nstp[::2] = 262
    nstp[1::2] = nstp[1::2] = 103
    steady = [False for x in range (1,402)]
    tsmult = np.empty((401,), dtype = np.int32)
    tsmult = 1
    
    # Discretization (.dis) package defintion
    dis = flopy.modflow.ModflowDis(mf, nlay, nrow, ncol, delr = delr, 
                                   delc = delc, top = ztop, botm = botm, 
                                   nper = nper, perlen = perlen, nstp = nstp, 
                                   tsmult = tsmult, steady = steady)
    
    # Variables for the basic (.bas) package #
    ibound = np.ones((nlay, nrow, ncol), dtype = np.int32)
    strt = 40 * np.ones((nlay, nrow, ncol), dtype = np.float32)
    
    # Create the basic (.bas) package #
    bas = flopy.modflow.ModflowBas(mf, ibound = ibound, strt = strt)
    
    # Define the properties for the layer property flow (.lpf) package #
    laytyp = 1
    
    
    #  
    upw = flopy.modflow.ModflowUpw(mf, hk = hk, vka = vk, sy = sy, ss = ss,
                                    laytyp = laytyp, ipakcb = 53)
    
    # Define the preconditioned conjugate gradient (.nwt) package #
    nwt = flopy.modflow.ModflowNwt(mf, linmeth = 2, options = 'COMPLEX')
    
    # Creating the well inputs for the well (.wel) package #
    # It is important to adjust the distributed pumping volume to reflect
    # the length of the pumping season that is prescribed
    
    
    with open('./Inputs/Proj_PumpingRates_20.csv','r') as f:
        reader = csv.reader(f)
        pr = list(reader)
    
    pr.pop(0)
    pr_BAU, pr_LEMA = [list(i) for i in zip(*pr)]
    
    lay_num = np.zeros([145,50])
    row_num = np.zeros([145,50])
    col_num = np.ones([145,50])*list(range(0,50))
    no_pump = np.zeros([145,50])
    
    wel_nopump = np.dstack((lay_num, row_num, col_num, no_pump))
    
    
    lay_num = np.zeros([145,50])
    row_num = np.zeros([145,50])
    col_num = np.ones([145,50])*list(range(0,50))
    
    
    PR = np.ones([145,50])
    
    for i in range(145):     
            PR[i,0:18] = pr_BAU[i]
            PR[i,18:32] = pr_BAU[i]
            PR[i,32:50] = pr_BAU[i]
    
    wel_PR = np.dstack((lay_num, row_num, col_num, PR))
    
    
    wel_nopump = wel_nopump.tolist()
    wel_PR = wel_PR.tolist()
    
    keys_nopump = list(range(112,401,2));
    keys_PR = list(range(111,401,2));
    
    
    wel_spd = {}
    
    for i in keys_nopump:
        for j in range(40):
            wel_spd[i] = wel_nopump[j]
            
    j = 0    
    for i in keys_PR:
            wel_spd[i] = wel_PR[j]
            j = j + 1
    
    
    wel = flopy.modflow.ModflowWel(mf, ipakcb = 53, 
                                   stress_period_data = wel_spd)
    
    # Create the drain package
    lay = [0]*50
    row = [0]*50
    col = list(range(0,50,1))
    stag = [40]*50
    cond = [1000000]*50
    
    drn_loc = list(zip(lay, row, col, stag, cond))
    
    
    drn_dict = {}

    for d in range(111):
        drn_dict[d] = drn_loc
    
    drn = flopy.modflow.ModflowDrn(mf, ipakcb = 53,
                                   stress_period_data = drn_dict)
    
        
    # Create the flow and head boundary (.fhb) package
   
    nflw = 50
    lay = [0]*50
    row = [0]*50
    col = list(range(0,50,1))
    iaux = list(range(0,50,1))
    flwrat = [LI*800*800]*50


    ds5 = list(zip(lay, row, col, iaux, flwrat))
    
    fhb = flopy.modflow.ModflowFhb(mf, ipakcb = 53, nflw = nflw, ds5 = ds5)
                
    
    # Create the unsaturated zone flow package
    uzgag = {65: [0, 9, 65, 2],
              66: [0, 24, 66, 2],
              67: [0, 39, 67, 2]}
    
    with open('./Inputs/Proj_DeepPerc_20.csv','r') as f:
        reader = csv.reader(f)
        inf = list(reader)
    
    inf.pop(0)
    inf_BAU, inf_LEMA = [list(i) for i in zip(*inf)]
    
    
    inf_array = np.zeros([401, 50])
    for i in range(401):
            inf_array[i,0:18] = inf_BAU[i]
            inf_array[i,18:32] = inf_BAU[i]
            inf_array[i,32:50] = inf_BAU[i]
    
    inf_list = np.split(inf_array, indices_or_sections = 401)
     
    inf_dict = {}
    
    for i in range(401):
        inf_dict[i] = inf_list[i]
    
    
    finf = inf_dict
    

    uzf = flopy.modflow.ModflowUzf1(mf, nuztop = 1, iuzfopt = 2, irunflg = 0, 
                                    ietflg = 0, ipakcb = 53, iuzfcb2 = 0, 
                                    ntrail2 = 20, nsets = 20, surfdep = 0,
                                    iuzfbnd = 1, irunbnd = 0, eps = eps, 
                                    thts = thts, thtr = thtr, thti = thti,
                                    specifythtr = True, specifythti = True,
                                    nosurfleak = True, finf = finf, pet = 0, 
                                    extdp = 0, netflux = None, uzgag = uzgag)
    
    # Creating the ouput control (.oc) package for all stress periods and # 
    # time steps  Model uses water year start date (October 1 as day 1) #
    # This will print the head and cell-by-cell budget for the first day #
    # of each month #
    spinup = [i for i in range(0,401,2) for _ in range(8)]
    spinup2 = [i for i in range(1,401,2) for _ in range(4)]
    
    
    spinup.extend(spinup2)
    
    oc_sp = sorted(spinup)
    
    timesteps_print = [25, 56, 86, 117, 148, 176, 207, 237, 6, 36, 67, 98]
    ts_sp = timesteps_print*201
    ts_sp2 = [25, 56, 86, 117, 148, 176, 207, 237]
    
    ts_sp.extend(ts_sp2)
    
    sp_keys = list(zip(oc_sp, ts_sp))
    
    oc_spd = dict.fromkeys(sp_keys, ['print head', 'print budget', 'print drawdown',
                                     'save head', 'save budget', 'save drawdown'])
    
    oc = flopy.modflow.ModflowOc(mf, stress_period_data=oc_spd, compact=True)
    
    with open('./Inputs/Head_Observations.csv','r') as f:
        reader = csv.reader(f)
        tsd = list(reader)    
        tsd.pop(0)
    
    for col in tsd:
        del col[0:2]
    
    names = []
    for i in range(1,3,1):    
        names_hold = ['o%s.1' % (i), 'o%s.2' % (i), 'o%s.3' % (i), 'o%s.4' % (i), 
                 'o%s.5' % (i), 'o%s.6' % (i), 'o%s.7' % (i), 'o%s.8' % (i),
                 'o%s.9' % (i), 'o%s.10' % (i), 'o%s.11' % (i), 'o%s.12' % (i), 
                 'o%s.13' % (i), 'o%s.14' % (i), 'o%s.15' % (i), 'o%s.16' % (i),
                 'o%s.17' % (i), 'o%s.18' % (i), 'o%s.19' % (i), 'o%s.20' % (i), 
                 'o%s.21' % (i)]
    
        names.append(names_hold)
    
    
    obs_data = []
    obs_name = []
    j = 24
    for i in range(0, 2, 1):
        obs_data.append(flopy.modflow.HeadObservation(mf, layer = 0, row = 0, 
                                                  column = j, 
                                                  time_series_data = tsd,
                                                  names = names[i][:], 
                                                  obsname = 'o%s' % (i + 1)))
        j = j + 1
        
    
    hob = flopy.modflow.ModflowHob(mf, iuhobsv = 1098, obs_data=obs_data)
  
    # set up folder to save data to
    Path('./Data/Projection/LI_No_Red/20_Percent/%s' % (modelname)).mkdir(parents = True, 
                                                          exist_ok = True)
    os.chdir('./Data/Projection/LI_No_Red/20_Percent/%s' % (modelname))
    
    # Write the FloPy packages       
    mf.write_input()
    
    
    # Run MODFLOW
    success = mf.run_model(silent = True)
    
    os.chdir(working_folder)
    
#%%
# 30% pumping reduction scenario for lateral inflow dominated parameters
for k in range(0, len(lhs), 1):
    Lx = 40000.
    Ly = 800.
    ztop = 72.
    zbot = 0.
    nlay = 1
    nrow = 1
    ncol = 50
    delr = Lx/ncol
    delc = Ly/nrow
    botm = 0
    ss = 1E-5
    
    hk = 20
    vk = lhs.K_v[k]
    sy = lhs.Sy[k]
    LI = lhs.LI[k]
    eps = lhs.EPS[k]
    thts = 0.25
    thtr = thts - lhs.Sy[k]
    thti = (thts - lhs.Sy[k]) + 0.005
    modelname = 'Run_%s' % (lhs.Run[k])
    
    # Model name
    mf = flopy.modflow.Modflow(modelname, version = 'mfnwt',
                               exe_name = path2mf)
    
    # Stress period and time step setup
    nper = 401
    perlen = np.empty((401,), dtype = np.int32)
    perlen[::2] = perlen[::2] = 262
    perlen[1::2] = perlen[1::2] = 103
    nstp = np.empty((401,), dtype = np.int32)
    nstp[::2] = nstp[::2] = 262
    nstp[1::2] = nstp[1::2] = 103
    steady = [False for x in range (1,402)]
    tsmult = np.empty((401,), dtype = np.int32)
    tsmult = 1
    
    # Discretization (.dis) package defintion
    dis = flopy.modflow.ModflowDis(mf, nlay, nrow, ncol, delr = delr, 
                                   delc = delc, top = ztop, botm = botm, 
                                   nper = nper, perlen = perlen, nstp = nstp, 
                                   tsmult = tsmult, steady = steady)
    
    # Variables for the basic (.bas) package #
    ibound = np.ones((nlay, nrow, ncol), dtype = np.int32)
    strt = 40 * np.ones((nlay, nrow, ncol), dtype = np.float32)
    
    # Create the basic (.bas) package #
    bas = flopy.modflow.ModflowBas(mf, ibound = ibound, strt = strt)
    
    # Define the properties for the layer property flow (.lpf) package #
    laytyp = 1
    
    
    #  
    upw = flopy.modflow.ModflowUpw(mf, hk = hk, vka = vk, sy = sy, ss = ss,
                                    laytyp = laytyp, ipakcb = 53)
    
    # Define the preconditioned conjugate gradient (.nwt) package #
    nwt = flopy.modflow.ModflowNwt(mf, linmeth = 2, options = 'COMPLEX')
    
    # Creating the well inputs for the well (.wel) package #
    # It is important to adjust the distributed pumping volume to reflect
    # the length of the pumping season that is prescribed
    
    
    with open('./Inputs/Proj_PumpingRates_30.csv','r') as f:
        reader = csv.reader(f)
        pr = list(reader)
    
    pr.pop(0)
    pr_BAU, pr_LEMA = [list(i) for i in zip(*pr)]
    
    lay_num = np.zeros([145,50])
    row_num = np.zeros([145,50])
    col_num = np.ones([145,50])*list(range(0,50))
    no_pump = np.zeros([145,50])
    
    wel_nopump = np.dstack((lay_num, row_num, col_num, no_pump))
    
    
    lay_num = np.zeros([145,50])
    row_num = np.zeros([145,50])
    col_num = np.ones([145,50])*list(range(0,50))
    
    
    PR = np.ones([145,50])
    
    for i in range(145):     
            PR[i,0:18] = pr_BAU[i]
            PR[i,18:32] = pr_BAU[i]
            PR[i,32:50] = pr_BAU[i]
    
    wel_PR = np.dstack((lay_num, row_num, col_num, PR))
    
    
    wel_nopump = wel_nopump.tolist()
    wel_PR = wel_PR.tolist()
    
    keys_nopump = list(range(112,401,2));
    keys_PR = list(range(111,401,2));
    
    
    wel_spd = {}
    
    for i in keys_nopump:
        for j in range(40):
            wel_spd[i] = wel_nopump[j]
            
    j = 0    
    for i in keys_PR:
            wel_spd[i] = wel_PR[j]
            j = j + 1
    
    
    wel = flopy.modflow.ModflowWel(mf, ipakcb = 53, 
                                   stress_period_data = wel_spd)
    
    # Create the drain package
    lay = [0]*50
    row = [0]*50
    col = list(range(0,50,1))
    stag = [40]*50
    cond = [1000000]*50
    
    drn_loc = list(zip(lay, row, col, stag, cond))
    
    
    drn_dict = {}

    for d in range(111):
        drn_dict[d] = drn_loc
    
    drn = flopy.modflow.ModflowDrn(mf, ipakcb = 53,
                                   stress_period_data = drn_dict)
    
        
    # Create the flow and head boundary (.fhb) package
   
    nflw = 50
    lay = [0]*50
    row = [0]*50
    col = list(range(0,50,1))
    iaux = list(range(0,50,1))
    flwrat = [LI*800*800]*50


    ds5 = list(zip(lay, row, col, iaux, flwrat))
    
    fhb = flopy.modflow.ModflowFhb(mf, ipakcb = 53, nflw = nflw, ds5 = ds5)
                
    
    # Create the unsaturated zone flow package
    uzgag = {65: [0, 9, 65, 2],
              66: [0, 24, 66, 2],
              67: [0, 39, 67, 2]}
    
    with open('./Inputs/Proj_DeepPerc_30.csv','r') as f:
        reader = csv.reader(f)
        inf = list(reader)
    
    inf.pop(0)
    inf_BAU, inf_LEMA = [list(i) for i in zip(*inf)]
    
    
    inf_array = np.zeros([401, 50])
    for i in range(401):
            inf_array[i,0:18] = inf_BAU[i]
            inf_array[i,18:32] = inf_BAU[i]
            inf_array[i,32:50] = inf_BAU[i]
    
    inf_list = np.split(inf_array, indices_or_sections = 401)
     
    inf_dict = {}
    
    for i in range(401):
        inf_dict[i] = inf_list[i]
    
    
    finf = inf_dict
    

    uzf = flopy.modflow.ModflowUzf1(mf, nuztop = 1, iuzfopt = 2, irunflg = 0, 
                                    ietflg = 0, ipakcb = 53, iuzfcb2 = 0, 
                                    ntrail2 = 20, nsets = 20, surfdep = 0,
                                    iuzfbnd = 1, irunbnd = 0, eps = eps, 
                                    thts = thts, thtr = thtr, thti = thti,
                                    specifythtr = True, specifythti = True,
                                    nosurfleak = True, finf = finf, pet = 0, 
                                    extdp = 0, netflux = None, uzgag = uzgag)
    
    # Creating the ouput control (.oc) package for all stress periods and # 
    # time steps  Model uses water year start date (October 1 as day 1) #
    # This will print the head and cell-by-cell budget for the first day #
    # of each month #
    spinup = [i for i in range(0,401,2) for _ in range(8)]
    spinup2 = [i for i in range(1,401,2) for _ in range(4)]
    
    
    spinup.extend(spinup2)
    
    oc_sp = sorted(spinup)
    
    timesteps_print = [25, 56, 86, 117, 148, 176, 207, 237, 6, 36, 67, 98]
    ts_sp = timesteps_print*201
    ts_sp2 = [25, 56, 86, 117, 148, 176, 207, 237]
    
    ts_sp.extend(ts_sp2)
    
    sp_keys = list(zip(oc_sp, ts_sp))
    
    oc_spd = dict.fromkeys(sp_keys, ['print head', 'print budget', 'print drawdown',
                                     'save head', 'save budget', 'save drawdown'])
    
    oc = flopy.modflow.ModflowOc(mf, stress_period_data=oc_spd, compact=True)
    
    with open('./Inputs/Head_Observations.csv','r') as f:
        reader = csv.reader(f)
        tsd = list(reader)    
        tsd.pop(0)
    
    for col in tsd:
        del col[0:2]
    
    names = []
    for i in range(1,3,1):    
        names_hold = ['o%s.1' % (i), 'o%s.2' % (i), 'o%s.3' % (i), 'o%s.4' % (i), 
                 'o%s.5' % (i), 'o%s.6' % (i), 'o%s.7' % (i), 'o%s.8' % (i),
                 'o%s.9' % (i), 'o%s.10' % (i), 'o%s.11' % (i), 'o%s.12' % (i), 
                 'o%s.13' % (i), 'o%s.14' % (i), 'o%s.15' % (i), 'o%s.16' % (i),
                 'o%s.17' % (i), 'o%s.18' % (i), 'o%s.19' % (i), 'o%s.20' % (i), 
                 'o%s.21' % (i)]
    
        names.append(names_hold)
    
    
    obs_data = []
    obs_name = []
    j = 24
    for i in range(0, 2, 1):
        obs_data.append(flopy.modflow.HeadObservation(mf, layer = 0, row = 0, 
                                                  column = j, 
                                                  time_series_data = tsd,
                                                  names = names[i][:], 
                                                  obsname = 'o%s' % (i + 1)))
        j = j + 1
        
    
    hob = flopy.modflow.ModflowHob(mf, iuhobsv = 1098, obs_data=obs_data)
  
    # set up folder to save data to
    Path('./Data/Projection/LI_No_Red/30_Percent/%s' % (modelname)).mkdir(parents = True, 
                                                          exist_ok = True)
    os.chdir('./Data/Projection/LI_No_Red/30_Percent/%s' % (modelname))
    
    # Write the FloPy packages       
    mf.write_input()
    
    
    # Run MODFLOW
    success = mf.run_model(silent = True)
    
    os.chdir(working_folder)