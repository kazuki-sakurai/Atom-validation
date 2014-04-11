#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'H160_T1bC1wN1_250-106-60'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list_SF = [ 
                    ['pT(lep1) > 25: SF',            2613.5],
                    ['H160: =2 b-jets: SF',          1074.1],
                    ['H160: mT2(b-jet) > 160: SF',    151.9],
                    ['H160: mT2 < 90: SF',            147.6],
                    ['H160: pT(lep1) < 60: SF',        75.3]]

    initial_list_DF = [ 
                    ['pT(lep1) > 25: DF',            2470.4],
                    ['H160: =2 b-jets: DF',           893.5],
                    ['H160: mT2(b-jet) > 160: DF',    137.7],
                    ['H160: mT2 < 90: DF',            135.0],
                    ['H160: pT(lep1) < 60: DF',        58.2]]

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



