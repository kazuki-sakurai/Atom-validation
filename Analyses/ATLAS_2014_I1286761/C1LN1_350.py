#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'C1LN1_350'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 40000.
    per = 100.
    
    initial_list_SF = [ 
                        ['= 2 OSlep pT > 35, 20: SF',  52.0 + 47.8],
                        ['Jet Veto: SF',               22.4 + 20.7],
                        ['Z Veto: SF',                 21.2 + 19.3],
                        ['mT2 90: SF',                 12.7 + 11.5],
                        ['mT2 120: SF',                 9.4 + 8.7],
                        ['mT2 150: SF',                 6.2 + 5.7]]

    initial_list_DF = [ 
                        ['= 2 OSlep pT > 35, 20: DF',  77.7],
                        ['Jet Veto: DF',               32.4],
                        ['Z Veto: DF',                 32.4],
                        ['mT2 90: DF',                 19.1],
                        ['mT2 120: DF',                14.7],
                        ['mT2 150: DF',                10.1]]

    eff_dict = {}
    err_dict = {}
    for name, val in initial_list_SF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']        
    for name, val in initial_list_DF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: DF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: DF']        

    cutflow_generation(vname, initial_list_SF, ananame, eff_dict, err_dict, Ntot_exp)
    cutflow_generation(vname, initial_list_DF, ananame, eff_dict, err_dict, Ntot_exp)
