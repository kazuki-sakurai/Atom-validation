#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'GQdirect_1425-525'

    table_name = '$\\tilde q \\tilde q$ direct (1425, 400): (ATLAS\\_CONF\\_2013\\_047)'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde q \\tilde g \\to (q \\chi_1^0)(q q \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde g} = 1425$~GeV, $m_{\\tilde q} = 1368$~GeV, $m_{\\tilde \\chi_1^0} = 525$~GeV.
        \\item  The number of events: $5 \\cdot 10^3$.
        \\item  Event Generator: {\\tt MadGraph 5 and Pythia 6}.
                The MLM merging is used with the shower-$k_T$ scheme implemented in MadGraph 5 and Pythia 6, where we take xqcut = qcut = $M_{\\rm SUSY}/4$ with MSUSY being the mass of the heavier SUSY particles in the production.      
        \\end{itemize}    
    '''
    table_caption = '''
        The cut-flow table for the B medium signal region: $\\tilde q \\tilde g$ direct (1425, 525).
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    eff_dict['No cut'] = 1.
    err_dict['No cut'] = 0.

    #for key in eff_dict0: print key
    #exit()

    Ntot_exp = 5000.
    per = 100.
    
    initial_list = [ 
                    ["No cut",                    100.0,   "No cut"],    
                    ["base: 0 lepton",             98.0,   "base: 0 lepton"],
                    ["base: MET > 160",            93.3,   "base: MET $>$ 160"],
                    ["base: pTj1 > 130",           93.3,   "base: $p_T(j_1) > 130$"], 
                    ["base: pTj2 > 60",            92.4,   "base: $p_T(j_2) > 60$"],    
                    ["pTj3 > 60",                  68.5,   "pTj3 > 60"],              
                    ["B base: dphi_min_23 > 0.4",  60.4,   "B base: $\\Delta \\phi(j_i, {\\rm MET}) > 0.4$"],                    
                    ["BT: MET/meff_3j > 0.4",      44.8,   "BT: ${\\rm MET}/m_{\\rm eff}(3j) > 0.4$"],
                    ["BT: meff_inc > 1800",        27.5,   "BT: $m_{\\rm eff}({\\rm inc}) > 1800$"]
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
    fout.write('\\subsection*{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in table_lines: fout.write(t + '\n')
    fout.write('\n')        
    fout.write(tex.end_document)

