#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'WWa'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list_SF = [ 
                        ['= 2 OSlep pT > 35, 20: SF',  402.1 + 521.6],
                        ['Jet Veto: SF',               198.6 + 258.6],
                        ['Z Veto: SF',                 165.0 + 212.0],
                        ['WWa: pTll > 80: SF',          28.0 +  35.3],
                        ['WWa: METrel > 80: SF',        14.7 +  22.8],
                        ['WWa: mll < 120: SF',           9.2 +  16.4]]

    initial_list_DF = [ 
                        ['= 2 OSlep pT > 35, 20: DF',  741.3],
                        ['Jet Veto: DF',               370.1],
                        ['Z Veto: DF',                 370.1],
                        ['WWa: pTll > 80: DF',          57.0],
                        ['WWa: METrel > 80: DF',        35.7],
                        ['WWa: mll < 120: DF',          24.4]]

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



