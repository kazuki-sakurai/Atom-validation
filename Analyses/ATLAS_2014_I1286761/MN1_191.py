#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'MN1_191'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 5000.
    per = 100.
    
    initial_list = [ 
                    ['= 2 OSlep pT > 35, 20: SF',  147.8],
                    ['Jet Veto: SF',                64.7],
                    ['Z Veto: SF',                  60.0],
                    ['mT2 90: SF',                  21.7],
                    ['mT2 120: SF',                  8.5],
                    ['mT2 150: SF',                  1.1]]

    eff_dict = {}
    err_dict = {}
    for name, val in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']        

    cutflow_generation(vname, initial_list, ananame, eff_dict, err_dict, Ntot_exp)

