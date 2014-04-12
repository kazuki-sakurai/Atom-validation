#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'GG1step_1265'

    table_name = '$\\tilde g \\tilde g$ one step (1265, 865, 465): (ATLAS\\_CONF\\_2013\\_047)'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde g \\tilde g: \\tilde g \\to q q \\chi_1^\\pm \\to W^\\pm q q \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde q} = 1265$~GeV, $m_{\\tilde \\chi_1^\\pm} = 865$~GeV, $m_{\\tilde \\chi_1^0} = 465$~GeV.
        \\item  The number of events: $2 \\cdot 10^4$.
        \\item  Event Generator: {\\tt MadGraph 5 and Pythia 6}.
                The MLM merging is used with the shower-$k_T$ scheme implemented in MadGraph 5 and Pythia 6, where we take xqcut = qcut = $M_{\\rm SUSY}/4$ with MSUSY being the mass of the heavier SUSY particles in the production.      
        \\end{itemize}    
    '''
    table_caption = '''
        The cut-flow table for E tight signal region: $\\tilde g \\tilde g$ one step (1265, 865, 465).
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    eff_dict['No cut'] = 1.
    err_dict['No cut'] = 0.

    #for key in eff_dict: print key
    #exit()

    Ntot_exp = 20000.
    per = 100.
    
    initial_list = [ 
                    ["No cut",                     100.0,   "No cut"],    
                    ["base: 0 lepton",              63.5,   "base: 0 lepton"],
                    ["base: MET > 160",             55.6,   "base: MET $>$ 160"],
                    ["base: pTj1 > 130",            55.6,   "base: $p_T(j_1) > 130$"], 
                    ["base: pTj2 > 60",             55.6,   "base: $p_T(j_2) > 60$"],
                    ["pTj3 > 60",                   55.4,   "$p_T(j_3) > 60$"],
                    ["pTj4 > 60",                   53.4,   "$p_T(j_4) > 60$"],
                    ["pTj5 > 60",                   46.3,   "$p_T(j_5) > 60$"],                  
                    ["pTj6 > 60",                   31.7,   "$p_T(j_6) > 60$"],                                      
                    ["E base: dphi_min_23 > 0.4",   26.5,   "E base: $\\Delta \\phi(j_i, {\\rm MET}) > 0.4$"],
                    ["E base: dphi_min_inc > 0.2",  21.3,   "E base: $\\Delta \\phi(j_i>40, {\\rm MET}) > 0.2$"],
                    ["ET: MET/meff_6j > 0.25",       12.0,   "ET: ${\\rm MET}/m_{\\rm eff}(6j) > 0.25$"],
                    ["ET: meff_inc > 1500",           7.9,   "ET: $m_{\\rm eff}({\\rm inc}) > 1500$"]
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

