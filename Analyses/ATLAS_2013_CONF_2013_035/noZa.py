#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'noZa'

    table_name = 'SR noZa: (ATLAS\\_CONF\\_2013\\_035)'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde \\chi_1^\\pm \\tilde \\chi_2^0 \\to (\\ell^\\pm \\nu \\tilde \\chi_1^0)(\\ell^+ \\ell^- \\tilde \\chi_1^0)$ via an on-shell $\\tilde \\ell_L$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = m_{\\tilde \\chi_2^0} = 192.5$~GeV, $m_{\\tilde \\ell_L} = 175$~GeV, $m_{\\tilde \\chi_1^0} = 157.5$~GeV.
        \\item  The number of events: $10^3$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''
    table_caption = '''
        The cut-flow table for the noZa signal region.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    #for key in eff_dict0: print key
    #exit()

    Ntot_exp = 25000.
    per = 100.
    
    initial_list = [ 
                    ['Lepton multi',        537.1,  'Lepton multiplicity'],
                    ['SFOS requirement',    536.3,  'SFOS requirement'],
                    ['b veto',              491.0,  '$b$-jet veto'],
                    ['Z veto',              476.3,  '$Z$ veto'],
                    ['SRnoZa: MET > 50',    161.2,  'SRnoZa: MET $>$ 50'],
                    ['SRnoZa: mSFOS < 60',  141.2,  'SRnoZa: mSFOS $<$ 60'],
                    ['SRnoZa: SRnoZc veto', 141.2,  'SRnoZa: SRnoZc veto']
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

