#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'L_T1bC1wN1_300-150-1'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list_SF = [ 
                    ['pT(lep1) > 25: SF',            2439.9],
                    ['Z veto: SF',                   1731.5],
                    ['Dphi_j > 1.0: SF',              928.9],
                    ['Dphi_b < 1.5: SF',              901.9],
                    ['mT2 > 90: SF',                   58.0],
                    ['mT2 > 120: SF',                   8.7],
                    ['mT2 > 100, pTj > 100, 50: SF',   24.8],
                    ['mT2 > 110, pTj > 20, 20: SF',    19.9]
                    ]

    initial_list_DF = [ 
                    ['pT(lep1) > 25: DF',            2560.7],
                    ['Dphi_j > 1.0: DF',             1315.3],
                    ['Dphi_b < 1.5: DF',             1274.0],
                    ['mT2 > 90: DF',                   77.1],
                    ['mT2 > 120: DF',                   9.4],
                    ['mT2 > 100, pTj > 100, 50: DF',   15.5],
                    ['mT2 > 110, pTj > 20, 20: DF',    16.5]
                    ]

    eff_dict = {}
    err_dict = {}
    for name, val in initial_list_SF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['pT(lep1) > 25: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['pT(lep1) > 25: SF']        
    for name, val in initial_list_DF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['pT(lep1) > 25: DF']
        err_dict[name] = err_dict0[name]/eff_dict0['pT(lep1) > 25: DF']        

    cutflow_generation(vname, initial_list_SF, ananame, eff_dict, err_dict, Ntot_exp)
    cutflow_generation(vname, initial_list_DF, ananame, eff_dict, err_dict, Ntot_exp)
