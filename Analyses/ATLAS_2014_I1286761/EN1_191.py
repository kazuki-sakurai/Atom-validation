#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'EN1_191'

    table_name = '$\\tilde e^\\pm(191) \\to e^\\pm \\tilde \\chi_1^0(90)$ (ATLAS\\_2014\\_I1286761 (1403.5294))'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde e^+ \\tilde e^-: \\tilde e^\\pm \\to e^\\pm \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde e} = 191$~GeV, $m_{\\tilde \\chi_1^0} = 90$~GeV.
        \\item  The number of events: $2 \\cdot 10^3$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption_SF = '''
        The cut-flow table for the same flavour channel.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 5000.
    per = 100.
    
    initial_list_SF = [ 
                    ['= 2 OSlep pT > 35, 20: SF',  135.4, '$=2$ OSlep $p_T > 35, 20$: SF'],
                    ['Jet Veto: SF',                60.5, 'Jet veto: SF'],
                    ['Z Veto: SF',                  55.7, '$Z$ veto: SF'],
                    ['mT2 90: SF',                  21.8, '$m_{T2} > 90$: SF'],
                    ['mT2 120: SF',                  8.0, '$m_{T2} > 20$: SF'],
                    ['mT2 150: SF',                  0.6, '$m_{T2} > 150$: SF']
                    ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list_SF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']        

    table_lines_SF = cutflow_generation(ananame, vname+'_SF', table_caption_SF, initial_list_SF, eff_dict, err_dict, Ntot_exp)

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
    fout.write(tex.end_document)
