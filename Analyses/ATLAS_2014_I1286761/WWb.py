#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'WWb'

    table_name = '$\\tilde \\chi_1^\\pm(140) \\to W^\\pm \\tilde \\chi_1^0(20)$ (ATLAS\\_2014\\_I1286761 (1403.5294))'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde \\chi_1^+ \\tilde \\chi_1^-: \\tilde \\chi_1^\\pm \\to W^\\pm \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = 140$~GeV, $m_{\\tilde \\chi_1^0} = 20$~GeV.
        \\item  The number of events: $5 \\cdot 10^4$.
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
                        ['= 2 OSlep pT > 35, 20: SF',  139.6 + 168.7, '$= 2$ OSlep $p_T > 35, 20$: SF'],
                        ['Jet Veto: SF',                65.7 +  78.2, 'Jet Veto: SF'],
                        ['Z Veto: SF',                  55.5 +  65.5, '$Z$ Veto: SF'],
                        ['WWb: mt2 > 90: SF',            4.5 +   5.2, 'WWb: $m_{T2} > 90$: SF'],
                        ['WWb: mll < 170: SF',           3.9 +   4.5, 'WWb: $m_{T2} < 170$: SF']
                        ]

    initial_list_DF = [ 
                        ['= 2 OSlep pT > 35, 20: DF',  253.8, '$= 2$ OSlep $p_T > 35, 20$: DF'],
                        ['Jet Veto: DF',               118.6, 'Jet Veto: DF'],
                        ['Z Veto: DF',                 118.6, '$Z$ Veto: DF'],
                        ['WWb: mt2 > 90: DF',            8.0, 'WWb: $m_{T2} > 90$: DF'],
                        ['WWb: mll < 170: DF',           7.2, 'WWb: $m_{\\ell \\ell} < 170$: DF'],
                        ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list_SF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']        
    for name, val, texname in initial_list_DF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: DF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: DF']        

    table_lines_SF = cutflow_generation(ananame, vname+'_SF', table_caption_SF, initial_list_SF, eff_dict, err_dict, Ntot_exp)
    table_lines_DF = cutflow_generation(ananame, vname+'_DF', table_caption_DF, initial_list_DF, eff_dict, err_dict, Ntot_exp)

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


