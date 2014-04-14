#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'Zjets_350'

    table_name = 'Zjets SR: S2 (ATLAS\\_2014\\_I1286761 (1403.5294))'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde \\chi_1^\\pm \\tilde \\chi_2^0 \\to (W^\\pm \\tilde \\chi_1^0) (Z \\tilde \\chi_1^0)$: forcing $Z \\to \\ell^+ \\ell^-$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = m_{\\tilde \\chi_2^0} = 350$~GeV, $m_{\\tilde \\chi_1^0} = 50$~GeV.
        \\item  The number of events: $2 \\cdot 10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for the S2 signal region.
    '''


    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list = [ 
                    ['= 2 OSlep pT > 35, 20: SF',   16.3 + 16.4,  '$= 2$ OSlep $p_T > 35, 20$: SF'],
                    ['Zjets: > 1 light jets',       13.1 + 13.2,  'Zjets: $> 1$ light jets'],
                    ['Zjets: No b- and F-jets',      9.8 +  9.5,  'Zjets: No b- and F-jets'],
                    ['Zjets: Z window',              9.4 +  9.1,  'Zjets: $Z$ window'],
                    ['Zjets: pTll > 80',             8.2 +  8.0,  'Zjets: $p_T^{\\ell \\ell} > 80$'],
                    ['Zjets: METrel > 80',           5.4 +  5.1,  'Zjets: METrel $>$ 80'],
                    ['Zjets: 0.3 < dRll < 1.5',      4.6 +  4.2,  'Zjets: $0.3 < \\Delta R (\\ell \\ell) < 1.5$'],
                    ['Zjets: 50 < mjj < 100',        3.1 +  2.7,  'Zjets: $50 < m_{jj} < 100$'],
                    ['Zjets: 2 light jets pT > 45',  1.9 +  1.8,  'Zjets: 2 light jets $p_T > 45$']
                    ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']        

    NMC_first = Ntot_exp * eff_dict0['= 2 OSlep pT > 35, 20: SF'] # geussed from Atom efficiency 
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
