#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'QQdirect_450-400'

    table_name = '$\\tilde q \\tilde q$ direct (450, 400): (ATLAS\\_CONF\\_2013\\_047)'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde q \\tilde q \\to (q \\chi_1^0)(q \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde q} = 450$~GeV, $m_{\\tilde \\chi_1^0} = 400$~GeV.
        \\item  The number of events: $2 \\cdot 10^4$.
        \\item  Event Generator: {\\tt MadGraph 5 and Pythia 6}.
                The MLM merging is used with the shower-$k_T$ scheme implemented in MadGraph 5 and Pythia 6, where we take xqcut = qcut = $M_{\\rm SUSY}/4$ with MSUSY being the mass of the heavier SUSY particles in the production.      
        \\end{itemize}    
    '''
    table_caption = '''
        The cut-flow table for A medium signal region: $\\tilde q \\tilde q$ direct (450, 400).
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    eff_dict['No cut'] = 1.
    err_dict['No cut'] = 0.

    #for key in eff_dict0: print key
    #exit()

    Ntot_exp = 20000.
    per = 100.
    
    initial_list = [ 
                    ["No cut",                     27288.6,   "No cut"],    
                    ["base: 0 lepton",             24528.0,   "base: 0 lepton"],
                    ["base: MET > 160",             4082.9,   "base: MET $>$ 160"],
                    ["base: pTj1 > 130",            3527.9,   "base: $p_T(j_1) > 130$"], 
                    ["base: pTj2 > 60",             2463.8,   "base: $p_T(j_2) > 60$"],                          
                    ["A base: dphi_min_23 > 0.4",   1919.9,   "A base: $\\Delta \\phi(j_i, {\\rm MET}) > 0.4$"],                    
                    ["AM: MET/sqrtHT > 15",          723.0,   "AM: ${\\rm MET}/\\sqrt{H_T} > 15$"],
                    ["AM: meff_inc > 1600",           36.2,   "AM: $_{\\rm meff}({\\rm inc}) > 1600$"]
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

