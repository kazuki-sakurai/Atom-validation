#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *


if __name__ == '__main__':

    vname = 'C1wN1N2hN1_130'

    table_name = '$(m_{\\tilde \\chi_2^0}, m_{\\tilde \\chi_1^0}) = (130, 0)$ (ATLAS\\_CONF\\_2013\\_091)'
    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde \\chi_1^\\pm \\tilde \\chi_2^0 \\to (W^\\pm \\tilde \\chi_1^0)(Z \\tilde \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = m_{\\tilde \\chi_2^0} = 130$~GeV, $m_{\\tilde \\chi_1^0} = 0$~GeV.
        \\item  The number of events: $5 \\cdot 10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for $(m_{\\tilde \\chi_2^0}, m_{\\tilde \\chi_1^0}) = (130, 0)$.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 50000.
    per = 100.

    #for key in eff_dict0: print key
    #exit()

    initial_list = [ 
                    ["MET > 50",                       3256.49,   "MET $>$ 50"],
                    [">= 2 central jets",              2304.39,   "$>= 2$ central jets"],
                    ["2 leading jets central",         2170.64,   "2 leading jets central"],
                    ["4th leading jet veto (pT > 25)", 1891.79,   "4th leading jet veto ($p_T > 25$)"],
                    ["baseline lepton veto",           1860.44,   "baseline lepton veto"],
                    ["mjj > 50",                       1765.78,   "$m_{jj} > 50$"], 
                    ["mT > 40",                        1461.14,   "$m_T > 40$"],      
                    ["mCT > 160",                      176.80,    "$m_{CT} > 160$"],                 
                    ["MET > 100",                      140.10,    "exactly 2 leading bjets"],
                    ["exactly 2 leading bjets",        45.62,     "exactly 2 leading bjets"],
                    ["SRA: 100 < mT < 130",            8.72,      "SRA: $100 < m_T < 130$"], 
                    ["SRB: mT > 130",                  0.35,      "SRB: $m_T > 130$"]                    
                    ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['MET > 50']
        err_dict[name] = err_dict0[name]/eff_dict0['MET > 50']        

    NMC_first = Ntot_exp * eff_dict['MET > 50'] # guessed from Atom efficiency 
    texlines = cutflow_generation(ananame, vname, table_caption, initial_list, eff_dict, err_dict, NMC_first)    

    fout = open(vname + '.tex', 'w')
    tex = tex_format()
    fout.write(tex.begin_document)
    fout.write('\n')
    fout.write('\\subsection{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in texlines: fout.write(t + '\n')
    fout.write(tex.end_document)


