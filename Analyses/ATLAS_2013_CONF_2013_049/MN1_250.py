#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'MN1_250'

    table_name = '$\\tilde \\mu^\\pm(250) \\to \\mu^\\pm \\tilde \\chi_1^0(10)$ (ATLAS\\_CONF\\_2013\\_049)'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde \\mu^+ \\tilde \\mu^-: \\tilde \\mu^\\pm \\to \\mu^\\pm \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde \\mu} = 250$~GeV, $m_{\\tilde \\chi_1^0} = 10$~GeV.
        \\item  The number of events: $2 \\cdot 10^3$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for the $\\mu \\mu$ channel.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 5000.
    per = 100.
    
    initial_list = [ 
                        ['mm: Trigger',   50.,  '$\\mu \\mu$: Trigger'],
                        ['mm: Z-veto',    49.,  '$\\mu \\mu$: $Z$ veto'],                        
                        ['mm: Jet veto',  20.,  '$\\mu \\mu$: Jet veto'],
                        ['mm: METrel',    17.,  '$\\mu \\mu$: ${\\rm MET}^{\\rm rel}$'],
                        ['mm: mT2 > 90',  12.5, '$\\mu \\mu$: $m_{T2} > 90$'],
                        ['mm: mT2 > 110', 11.2, '$\\mu \\mu$: $m_{T2} > 110$']
                        ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['mm: Trigger']
        err_dict[name] = err_dict0[name]/eff_dict0['mm: Trigger']        

    NMC_first = Ntot_exp * eff_dict0['mm: Trigger'] # geussed from Atom efficiency 
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
    fout.close()
