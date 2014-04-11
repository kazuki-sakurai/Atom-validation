#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'Zjets_250'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list = [ 
                    ['= 2 OSlep pT > 35, 20: SF',   63.2 + 71.0],
                    ['Zjets: > 1 light jets',       48.7 + 54.6],
                    ['Zjets: No b- and F-jets',     36.8 + 40.9],
                    ['Zjets: Z window',             35.5 + 39.2],
                    ['Zjets: pTll > 80',            27.4 + 29.2],
                    ['Zjets: METrel > 80',          12.5 + 14.7],
                    ['Zjets: 0.3 < dRll < 1.5',      9.6 + 10.2],
                    ['Zjets: 50 < mjj < 100',        6.1 +  6.6],
                    ['Zjets: 2 light jets pT > 45',  2.9 +  3.5]]

    eff_dict = {}
    err_dict = {}
    for name, val in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']        

    cutflow_generation(vname, initial_list, ananame, eff_dict, err_dict, Ntot_exp)
