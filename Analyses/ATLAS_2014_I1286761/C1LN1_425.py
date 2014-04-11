#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'C1LN1_425'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 40000.
    per = 100.
    
    initial_list_SF = [ 
                        ['= 2 OSlep pT > 35, 20: SF',  20.5 + 19.9],
                        ['Jet Veto: SF',                8.3 +  8.0],
                        ['Z Veto: SF',                  7.8 +  7.7],
                        ['mT2 90: SF',                  4.8 +  4.9],
                        ['mT2 120: SF',                 3.8 +  3.9],
                        ['mT2 150: SF',                 2.7 +  3.0]]

    initial_list_DF = [ 
                        ['= 2 OSlep pT > 35, 20: DF',  31.3],
                        ['Jet Veto: DF',               12.3],
                        ['Z Veto: DF',                 12.3],
                        ['mT2 90: DF',                  7.9],
                        ['mT2 120: DF',                 6.3],
                        ['mT2 150: DF',                 4.6]]

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


