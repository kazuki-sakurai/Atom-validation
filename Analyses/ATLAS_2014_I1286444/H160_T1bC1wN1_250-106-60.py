#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'H160_T1bC1wN1_250-106-60'

    table_name = 'SR H160: $\\tilde t_1(250) \\to b \\tilde \\chi_1^+(106) \\to W^+ \\tilde \\chi_1^0(60)$ (ATLAS\\_2014\\_I1286444 (1403.4853))'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde t_1 \\tilde t_1^*: \\tilde t_1 \\to b \\tilde \\chi_1^+ \\to W^+ \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde t_1} = 250$~GeV, $m_{\\tilde \\chi_1^\\pm} = 106$~GeV, $m_{\\tilde \\chi_1^0} = 60$~GeV.
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
                    ['pT(lep1) > 25: SF',            2613.5,  '$p_T(\\ell_1) > 25$: SF'],
                    ['H160: =2 b-jets: SF',          1074.1,  'H160: $=2 b$-jets: SF'],
                    ['H160: mT2(b-jet) > 160: SF',    151.9,  'H160: $m_{T2}({\\rm b-jet}) > 160$: SF'],
                    ['H160: mT2 < 90: SF',            147.6,  'H160: $m_{T2} < 90$: SF'],
                    ['H160: pT(lep1) < 60: SF',        75.3,  'H160: $p_T(\\ell_1) < 60$: SF']]

    initial_list_DF = [ 
                    ['pT(lep1) > 25: DF',            2470.4,  '$p_T(\\ell_1) > 25$: DF'],,  '$p_T(\\ell_1) > 25$: DF'],
                    ['H160: =2 b-jets: DF',           893.5,  'H160: $=2 b$-jets: DF'],
                    ['H160: mT2(b-jet) > 160: DF',    137.7,  'H160: $m_{T2}({\\rm b-jet}) > 160$: DF'],
                    ['H160: mT2 < 90: DF',            135.0,  'H160: $m_{T2} < 90$: DF'],
                    ['H160: pT(lep1) < 60: DF',        58.2,  'H160: $p_T(\\ell_1) < 60$: DF']]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list_SF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['pT(lep1) > 25: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['pT(lep1) > 25: SF']        
    for name, val, texname in initial_list_DF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['pT(lep1) > 25: DF']
        err_dict[name] = err_dict0[name]/eff_dict0['pT(lep1) > 25: DF']        

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

