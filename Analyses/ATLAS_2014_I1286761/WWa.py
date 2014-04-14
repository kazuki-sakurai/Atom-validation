#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'WWa'

    table_name = '$\\tilde \\chi_1^\\pm(100) \\to W^\\pm \\tilde \\chi_1^0(0)$ (ATLAS\\_2014\\_I1286761 (1403.5294))'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde \\chi_1^+ \\tilde \\chi_1^-: \\tilde \\chi_1^\\pm \\to W^\\pm \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = 100$~GeV, $m_{\\tilde \\chi_1^0} = 0$~GeV.
        \\item  The number of events: $5 \\cdot 10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption_SF = '''
        The cut-flow table for the same flavour channel.
    '''
    table_caption_DF = '''
        The cut-flow table for the different flavour channel.
    '''


    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000.
    per = 100.
    
    initial_list_SF = [ 
                        ['= 2 OSlep pT > 35, 20: SF',  402.1 + 521.6, '$= 2$ OSlep $p_T > 35, 20$: SF'],
                        ['Jet Veto: SF',               198.6 + 258.6, 'Jet Veto: SF'],
                        ['Z Veto: SF',                 165.0 + 212.0, '$Z$ Veto: SF'],
                        ['WWa: pTll > 80: SF',          28.0 +  35.3, 'WWa: $p_T(\\ell \\ell) > 80$: SF'],
                        ['WWa: METrel > 80: SF',        14.7 +  22.8, 'WWa: METrel $>$ 80: SF'],
                        ['WWa: mll < 120: SF',           9.2 +  16.4, 'WWa: $m_{\\ell \\ell} < 120$: SF']
                        ]

    initial_list_DF = [ 
                        ['= 2 OSlep pT > 35, 20: DF',  741.3, '$= 2$ OSlep $p_T > 35, 20$: DF'],
                        ['Jet Veto: DF',               370.1, 'Jet Veto: DF'],
                        ['Z Veto: DF',                 370.1, '$Z$ Veto: DF'],
                        ['WWa: pTll > 80: DF',          57.0, 'WWa: $p_T(\\ell \\ell) > 80$: DF'],
                        ['WWa: METrel > 80: DF',        35.7, 'WWa: METrel $>$ 80: DF'],
                        ['WWa: mll < 120: DF',          24.4, 'WWa: $m_{\\ell \\ell} < 120$: DF']
                       ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list_SF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: SF']        
    for name, val, texname in initial_list_DF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: DF']
        err_dict[name] = err_dict0[name]/eff_dict0['= 2 OSlep pT > 35, 20: DF']        

    NMC_first_SF = Ntot_exp * eff_dict0['= 2 OSlep pT > 35, 20: SF'] # geussed from Atom efficiency 
    table_lines_SF = cutflow_generation(ananame, vname+'_SF', table_caption_SF, initial_list_SF, eff_dict, err_dict, NMC_first_SF)
    NMC_first_DF = Ntot_exp * eff_dict0['= 2 OSlep pT > 35, 20: DF'] # geussed from Atom efficiency     
    table_lines_DF = cutflow_generation(ananame, vname+'_DF', table_caption_DF, initial_list_DF, eff_dict, err_dict, NMC_first_DF)

    fout = open(vname + '.tex', 'w')
    tex = tex_format()
    fout.write(tex.begin_document)
    fout.write('\n')
    fout.write('\\subsection{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in table_lines_SF: fout.write(t + '\n')
    fout.write('\n')        
    for t in table_lines_DF: fout.write(t + '\n')    
    fout.write('\n')            
    fout.write(tex.end_document)

