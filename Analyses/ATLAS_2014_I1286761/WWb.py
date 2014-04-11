#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'WWb'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list_SF = [ 
                        ['= 2 OSlep pT > 35, 20: SF',  139.6 + 168.7],
                        ['Jet Veto: SF',                65.7 +  78.2],
                        ['Z Veto: SF',                  55.5 +  65.5],
                        ['WWb: mt2 > 90: SF',            4.5 +   5.2],
                        ['WWb: mll < 170: SF',           3.9 +   4.5]]

    initial_list_DF = [ 
                        ['= 2 OSlep pT > 35, 20: DF',  253.8],
                        ['Jet Veto: DF',               118.6],
                        ['Z Veto: DF',                 118.6],
                        ['WWb: mt2 > 90: DF',            8.0],
                        ['WWb: mll < 170: DF',           7.2]]

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

