#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'Zc'

    table_name = 'SR Zc: (ATLAS\\_CONF\\_2013\\_035)'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde \\chi_1^\\pm \\tilde \\chi_2^0 \\to (W^\\pm \\chi_1^0)(Z \\tilde \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = m_{\\tilde \\chi_2^0} = 250$~GeV, $m_{\\tilde \\chi_1^0} = 0$~GeV.
        \\item  The number of events: $5 \\cdot 10^3$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''
    table_caption = '''
        The cut-flow table for the Zc signal region.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    #for key in eff_dict0: print key
    #exit()

    Ntot_exp = 20000.
    per = 100.
    
    initial_list = [ 
                    ['Lepton multi',           40.0,  'Lepton multiplicity'],
                    ['SFOS requirement',       39.7,  'SFOS requirement'],
                    ['b veto',                 36.4,  '$b$-jet veto'],
                    ['Z requirement',          34.4,  '$Z$ requirement'],
                    ['SRZc: MET > 120',        17.7,  'SRZc: MET > 120'],
                    ['SRZc: mT > 110',         12.0,  'SRZc: $m_T > 110$']
                    ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['Lepton multi']
        err_dict[name] = err_dict0[name]/eff_dict0['Lepton multi']        

    table_lines = cutflow_generation(ananame, vname, table_caption, initial_list, eff_dict, err_dict, Ntot_exp)

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

