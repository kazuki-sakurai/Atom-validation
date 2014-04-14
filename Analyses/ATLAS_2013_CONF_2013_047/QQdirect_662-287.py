#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'QQdirect_662-287'

    table_name = '$\\tilde q \\tilde q$ direct (662, 287): (ATLAS\\_CONF\\_2013\\_047)'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde q \\tilde q \\to (q \\chi_1^0)(q \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde q} = 662$~GeV, $m_{\\tilde \\chi_1^0} = 287$~GeV.
        \\item  The number of events: $10^4$.
        \\item  Event Generator: {\\tt MadGraph 5 and Pythia 6}.
                The MLM merging is used with the shower-$k_T$ scheme implemented in MadGraph 5 and Pythia 6, where we take xqcut = qcut = $M_{\\rm SUSY}/4$ with MSUSY being the mass of the heavier SUSY particles in the production.      
        \\end{itemize}    
    '''
    table_caption = '''
        The cut-flow table for C medium signal region: $\\tilde q \\tilde q$ direct (662, 287).
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    eff_dict['No cut'] = 1.
    err_dict['No cut'] = 0.

    #for key in eff_dict: print key
    #exit()

    Ntot_exp = 10000.
    per = 100.
    
    initial_list = [ 
                    ["No cut",                     1944.9,   "No cut"],    
                    ["base: 0 lepton",             1910.0,   "base: 0 lepton"],
                    ["base: MET > 160",            1569.2,   "base: MET $>$ 160"],
                    ["base: pTj1 > 130",           1555.0,   "base: $p_T(j_1) > 130$"], 
                    ["base: pTj2 > 60",            1471.1,   "base: $p_T(j_2) > 60$"],
                    ["pTj3 > 60",                   686.7,   "$p_T(j_3) > 60$"],
                    ["pTj4 > 60",                   223.7,   "$p_T(j_4) > 60$"],                    
                    ["C base: dphi_min_23 > 0.4",   196.8,   "C base: $\\Delta \\phi(j_i, {\\rm MET}) > 0.4$"],
                    ["C base: dphi_min_inc > 0.2",  180.4,   "C base: $\\Delta \\phi(j_i>40, {\\rm MET}) > 0.2$"],
                    ["CM: MET/meff_4j > 0.25",      139.2,   "CM: ${\\rm MET}/m_{\\rm eff}(4j) > 0.25$"],
                    ["CM: meff_inc > 1200",          57.6,   "CM: $m_{\\rm eff}({\\rm inc}) > 1200$"]
                    ]
    #eff_dict = {}
    #err_dict = {}
    #for name, val, texname in initial_list:
    #    eff_dict[name] = eff_dict0[name]/eff_dict0["No cut"]
    #    err_dict[name] = err_dict0[name]/eff_dict0["No cut"]        

    NMC_first = Ntot_exp
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

