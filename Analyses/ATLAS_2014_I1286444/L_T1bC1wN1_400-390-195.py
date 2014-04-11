#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'L_T1bC1wN1_400-390-195'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list_SF = [ 
                    ['pT(lep1) > 25: SF',            3253.5],
                    ['Z veto: SF',                   2463.6],
                    ['Dphi_j > 1.0: SF',             1834.9],
                    ['Dphi_b < 1.5: SF',             1402.8],
                    ['mT2 > 90: SF',                  396.5],
                    ['mT2 > 120: SF',                 211.8],
                    ['mT2 > 100, pTj > 100, 50: SF',   21.7],
                    ['mT2 > 110, pTj > 20, 20: SF',    86.0]
                    ]

    initial_list_DF = [ 
                    ['pT(lep1) > 25: DF',            3131.4],
                    ['Dphi_j > 1.0: DF',             2390.1],
                    ['Dphi_b < 1.5: DF',             1800.5],
                    ['mT2 > 90: DF',                  500.0],
                    ['mT2 > 120: DF',                 248.4],
                    ['mT2 > 100, pTj > 100, 50: DF',   35.0],
                    ['mT2 > 110, pTj > 20, 20: DF',   116.1]
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


