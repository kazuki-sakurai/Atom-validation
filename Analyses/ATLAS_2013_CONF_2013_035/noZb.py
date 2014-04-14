#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'noZb'

    table_name = 'SR noZb: (ATLAS\\_CONF\\_2013\\_035)'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde \\chi_1^\\pm \\tilde \\chi_2^0 \\to (W^\\pm \\chi_1^0)(Z \\tilde \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = m_{\\tilde \\chi_2^0} = 150$~GeV, $m_{\\tilde \\chi_1^0} = 75$~GeV.
        \\item  The number of events: $5 \\cdot 10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''
    table_caption = '''
        The cut-flow table for the noZb signal region.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    #for key in eff_dict0: print key
    #exit()

    Ntot_exp = 20000.
    per = 100.
    
    initial_list = [ 
                    ['Lepton multi',         227.3,  'Lepton multiplicity'],
                    ['SFOS requirement',     226.5,  'SFOS requirement'],
                    ['b veto',               211.0,  '$b$-jet veto'],
                    ['Z veto',               196.6,  '$Z$ veto'],
                    ['SRnoZb: MET > 75',      53.8,  'SRnoZb: MET $>$ 75'],
                    ['SRnoZb: mSFOS 60-81',   27.1,  'SRnoZb: mSFOS 60-81'],
                    ['SRnoZb: SRnoZc veto',   26.3,  'SRnoZb: SRnoZc veto']
                    ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['Lepton multi']
        err_dict[name] = err_dict0[name]/eff_dict0['Lepton multi']        

    NMC_first = Ntot_exp * eff_dict0['Lepton multi'] # geussed from Atom efficiency 
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

