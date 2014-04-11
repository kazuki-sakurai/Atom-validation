#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'Zjets_350'

if __name__ == '__main__':

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list = [ 
                    ['= 2 OSlep pT > 35, 20: SF',   16.3 + 16.4],
                    ['Zjets: > 1 light jets',       13.1 + 13.2],
                    ['Zjets: No b- and F-jets',      9.8 +  9.5],
                    ['Zjets: Z window',              9.4 +  9.1],
                    ['Zjets: pTll > 80',             8.2 +  8.0],
                    ['Zjets: METrel > 80',           5.4 +  5.1],
                    ['Zjets: 0.3 < dRll < 1.5',      4.6 +  4.2],
                    ['Zjets: 50 < mjj < 100',        3.1 +  2.7],
                    ['Zjets: 2 light jets pT > 45',  1.9 +  1.8]]

    eff_dict = {}
    err_dict = {}
    for name, val in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']        

    cutflow_generation(vname, initial_list, ananame, eff_dict, err_dict, Ntot_exp)



