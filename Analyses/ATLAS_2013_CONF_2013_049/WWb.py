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

    table_name = '$\\tilde \\chi_1^\\pm(140) \\to W^\\pm \\tilde \\chi_1^0(20)$ (ATLAS\\_CONF\\_2013\\_049)'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde \\chi_1^+ \\tilde \\chi_1^-: \\tilde \\chi_1^\\pm \\to W^\\pm \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = 140$~GeV, $m_{\\tilde \\chi_1^0} = 20$~GeV.
        \\item  The number of events: $5 \\cdot 10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for WWb signal region.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    #for key in eff_dict0: print key
    #exit()

    Ntot_exp = 100000.
    per = 100.
    
    initial_list = [ 
                    ["WW: Jet veto",             139.,  "WW: Jet veto"],
                    ["WW: pT_l1>35, pT_l2>20",   103.,  "WW: $p_T(\\ell_1) > 35, p_T(\\ell_2) > 20$"],
                    ["WWb",                      8.2,   "WWb"]
                    ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['WW: Jet veto']
        err_dict[name] = err_dict0[name]/eff_dict0['WW: Jet veto']        

    NMC_first = Ntot_exp * eff_dict0['WW: Jet veto'] # geussed from Atom efficiency 
    table_lines = cutflow_generation(ananame, vname, table_caption, initial_list, eff_dict, err_dict, NMC_first)

    fout = open(vname + '.tex', 'w')
    tex = tex_format()
    fout.write(tex.begin_document)
    fout.write('\n')
    fout.write('\\subsection{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in table_lines: fout.write(t + '\n')
    fout.write('\n')        
    fout.write(tex.end_document)


