#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'EN1_250'

    table_name = '$\\tilde e^\\pm(250) \\to e^\\pm \\tilde \\chi_1^0(10)$ (ATLAS\\_CONF\\_2013\\_049)'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde e^+ \\tilde e^-: \\tilde e^\\pm \\to e^\\pm \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde e} = 250$~GeV, $m_{\\tilde \\chi_1^0} = 10$~GeV.
        \\item  The number of events: $2 \\cdot 10^3$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for the $ee$ channel.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 5000.
    per = 100.
    
    initial_list = [ 
                        ['ee: Trigger',   55.,  '$ee$: Trigger'],
                        ['ee: Z-veto',    54.,  '$ee$: $Z$ veto'],                        
                        ['ee: Jet veto',  20.,  '$ee$: Jet veto'],
                        ['ee: METrel',    17.,  '$ee$: ${\\rm MET}^{\\rm rel}$'],
                        ['ee: mT2 > 90',  12.2, '$ee$: $m_{T2} > 90$'],
                        ['ee: mT2 > 110', 10.5, '$ee$: $m_{T2} > 110$']
                        ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list:
        try:
            eff_dict[name] = eff_dict0[name]/eff_dict0['ee: Trigger']
            err_dict[name] = err_dict0[name]/eff_dict0['ee: Trigger']        
            NMC_first = Ntot_exp * eff_dict0['ee: Trigger'] # geussed from Atom efficiency             
        except:
            eff_dict[name] = 0.
            err_dict[name] = 0.
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
