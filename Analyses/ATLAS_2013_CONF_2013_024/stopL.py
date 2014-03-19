#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

vname = 'stopL'

if __name__ == '__main__':
    inputfile = sys.argv[1]

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    Ntot_exp = 250000.
    per = 100.
    
    eff_dict['No-cut'] = 1.
    err_dict['No-cut'] = 0.

    initial_list = [ # ATLAS results: number is scalled for the 600 stop xsec with 20.5/fb
                    ['No-cut',                        507.3],
                    ["Muon veto",                     382.2],                            
                    ["Electron veto",                 292.3],                    
                    ["MET > 130",                     270.1],
                    ["Jet multiplicity and pT",       92.2],
                    ["MET_track > 30",                90.5], 
                    ["delPhi(MET, MET_track) < pi/3", 84.3],                    
                    ["delPhi(jet, MET) > pi/5",       72.0],                    
                    ["Tau veto",                      61.9],                    
                    [">= 2-bjet",                     31.5],                    
                    ["mT(bjet, MET) > 175",           23.6],                    
                    ["80 < m^0_jjj < 270",            20.4],                    
                    ["80 < m^1_jjj < 270",            11.9],                    
                    ["SR1: MET > 200",                11.2],                    
                    ["SR2: MET > 300",                8.3],                    
                    ["SR3: MET > 350",                6.6]
                    ]

    #######################################################
    #          Setting experimental efficiencies          #  
    #######################################################
    name_list = []
    eff_exp = []
    err_exp = []
    nev_exp = []
    for name, inival in initial_list:
        name_list.append(name)
        eff = inival/initial_list[0][1]
        nev = Ntot_exp * eff
        nerr = sqrt(nev)
        eff_err = nerr/Ntot_exp

        eff_exp.append(per * eff)
        err_exp.append(per * eff_err)
        nev_exp.append(nev)

    #######################################################
    #          Setting experimental efficiencies          #  
    #######################################################
    eff_atom = []
    err_atom = []
    ratio_eff = ['']
    ratio_eff_sig = ['']
    for i in range(len(name_list)):          
        name = name_list[i]
        eff = eff_dict[name]
        err = err_dict[name]
        eff_atom.append(per * eff)
        err_atom.append(per * err)
        if i > 0:
            ratio_eff.append( eff_atom[i]/eff_exp[i] )
            err = sqrt(err_atom[i]**2 + err_exp[i]**2)
            ratio_eff_sig.append( (err_atom[i] - err_exp[i])/err )

    #######################################################
    #          Setting relative efficiencies              #  
    #######################################################
    Reff_exp = ['']
    Rerr_exp = ['']
    Reff_atom = ['']
    Rerr_atom = ['']
    ratio_R = ['']
    ratio_R_sig = ['']    
    for i in range(1, len(name_list)):      
        nev = nev_exp[i]
        prevnev = nev_exp[i - 1]
        Reff_exp.append(nev/prevnev)
        Rerr_exp.append(sqrt(nev)/prevnev)

        eff = eff_atom[i]
        err = eff_atom[i]        
        preveff = eff_atom[i - 1]
        Reff_atom.append(eff/preveff)
        Rerr_atom.append(err/preveff)

        ratio_R.append( Rerr_atom[i]/Rerr_exp[i] )
        err = sqrt(Rerr_exp[i]**2 + Rerr_atom[i]**2)
        ratio_R_sig.append( (Rerr_atom[i] - Rerr_exp[i])/err )


    #######################################################
    #                       Display                       #  
    #######################################################
    show_cutflow(ananame, vname, 'ATLAS', name_list, 
                 eff_exp, err_exp, eff_atom, err_atom, ratio_eff, ratio_eff_sig, 
                 Reff_exp, Rerr_exp, Reff_atom, Rerr_atom, ratio_R, ratio_R_sig)    




