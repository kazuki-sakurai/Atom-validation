#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'L_T1bC1wN1_300-150-1'

    table_name = 'SR L: $\\tilde t_1(300) \\to b \\tilde \\chi_1^+(150) \\to W^+ \\tilde \\chi_1^0(1)$ (ATLAS\\_2014\\_I1286444 (1403.4853))'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde t_1 \\tilde t_1^*: \\tilde t_1 \\to b \\tilde \\chi_1^+ \\to W^+ \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde t_1} = 300$~GeV, $m_{\\tilde \\chi_1^\\pm} = 150$~GeV, $m_{\\tilde \\chi_1^0} = 1$~GeV.
        \\item  The number of events: $10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''
    table_caption_SF = '''
        The cut-flow table for the same flavour channel.
    '''
    table_caption_DF = '''
        The cut-flow table for the different flavour channel.
    '''


    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list_SF = [ 
                    ['pT(lep1) > 25: SF',            2439.9,  '$p_T(\\ell_1) > 25$: SF'],
                    ['Z veto: SF',                   1731.5,  '$Z$ veto: SF'],
                    ['Dphi_j > 1.0: SF',              928.9,  '$\\Delta \\phi_j > 1.0$: SF'],
                    ['Dphi_b < 1.5: SF',              901.9,  '$\\Delta \\phi_b < 1.5$: SF'],
                    ['mT2 > 90: SF',                   58.0,  '$m_{T2} > 90$: SF'],
                    ['mT2 > 120: SF',                   8.7,  '$m_{T2} > 120$: SF'],
                    ['mT2 > 100, pTj > 100, 50: SF',   24.8,  '$m_{T2} > 100, p_T(j) > 100, 50$: SF'],
                    ['mT2 > 110, pTj > 20, 20: SF',    19.9,  '$m_{T2} > 110, p_T(j) > 20, 20$: SF']
                    ]

    i_denom_SF = ['', 0, 1, 2, 3, 4, 4, 4]

    initial_list_DF = [ 
                    ['pT(lep1) > 25: DF',            2560.7,  '$p_T(\\ell_1) > 25$: DF'],
                    ['Dphi_j > 1.0: DF',             1315.3,  '$\\Delta \\phi_j > 1.0$: DF'],
                    ['Dphi_b < 1.5: DF',             1274.0,  '$\\Delta \\phi_b < 1.5$: DF'],
                    ['mT2 > 90: DF',                   77.1,  '$m_{T2} > 90$: DF'],
                    ['mT2 > 120: DF',                   9.4,  '$m_{T2} > 120$: DF'],
                    ['mT2 > 100, pTj > 100, 50: DF',   15.5,  '$m_{T2} > 100, p_T(j) > 100, 50$: DF'],
                    ['mT2 > 110, pTj > 20, 20: DF',    16.5,  '$m_{T2} > 110, p_T(j) > 20, 20$: DF']
                    ]

    i_denom_DF = ['', 0, 1, 2, 3, 3, 3]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list_SF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['pT(lep1) > 25: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['pT(lep1) > 25: SF']        
    for name, val, texname in initial_list_DF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['pT(lep1) > 25: DF']
        err_dict[name] = err_dict0[name]/eff_dict0['pT(lep1) > 25: DF']        

    NMC_first_SF = Ntot_exp * eff_dict0['pT(lep1) > 25: SF'] # geussed from Atom efficiency 
    table_lines_SF = cutflow_generation(ananame, vname+'_SF', table_caption_SF, initial_list_SF, eff_dict, err_dict, NMC_first_SF)
    NMC_first_DF = Ntot_exp * eff_dict0['pT(lep1) > 25: DF'] # geussed from Atom efficiency     
    table_lines_DF = cutflow_generation(ananame, vname+'_DF', table_caption_DF, initial_list_DF, eff_dict, err_dict, NMC_first_DF)

    fout = open(vname + '.tex', 'w')
    tex = tex_format()
    fout.write(tex.begin_document)
    fout.write('\n')
    fout.write('\\subsection*{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in table_lines_SF: fout.write(t + '\n')
    fout.write('\n')        
    for t in table_lines_DF: fout.write(t + '\n')    
    fout.write('\n')            
    fout.write(tex.end_document)

