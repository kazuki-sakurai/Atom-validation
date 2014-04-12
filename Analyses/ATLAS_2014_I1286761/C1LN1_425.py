#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'C1LN1_425'

    table_name = '$\\tilde \\chi_1^\\pm(425) \\to (\\ell \\tilde \\nu(250)  ~{\\rm or}~ \\nu \\tilde \\ell(250)) \\to \\nu \\ell  \\tilde \\chi_1^0(75)$ (ATLAS\\_2014\\_I1286761 (1403.5294))'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde \\chi_1^+ \\tilde \\chi_1^-: \\tilde \\chi_1^\\pm \\to (\\ell \\tilde \\nu  ~{\\rm or}~ \\nu \\tilde \\ell) \\to \\nu \\ell  \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = 425$~GeV, $m_{\\tilde \\ell/\\tilde \\nu} = 250$~GeV, $m_{\\tilde \\chi_1^0} = 75$~GeV.
        \\item  The number of events: $10^4$.
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

    Ntot_exp = 40000.
    per = 100.
    
    initial_list_SF = [ 
                        ['= 2 OSlep pT > 35, 20: SF',  20.5 + 19.9, '$=2$ OSlep $p_T > 35, 20$: SF'],
                        ['Jet Veto: SF',                8.3 +  8.0, 'Jet veto: SF'],
                        ['Z Veto: SF',                  7.8 +  7.7, '$Z$ veto: SF'],
                        ['mT2 90: SF',                  4.8 +  4.9, '$m_{T2} > 90$: SF'],
                        ['mT2 120: SF',                 3.8 +  3.9, '$m_{T2} > 120$: SF'],
                        ['mT2 150: SF',                 2.7 +  3.0, '$m_{T2} > 150$: SF']
                        ]

    initial_list_DF = [ 
                        ['= 2 OSlep pT > 35, 20: DF',  31.3, '$=2$ OSlep $p_T > 35, 20$: DF'],
                        ['Jet Veto: DF',               12.3, 'Jet veto: DF'],
                        ['Z Veto: DF',                 12.3, '$Z$ veto: DF'],
                        ['mT2 90: DF',                  7.9, '$m_{T2} > 90$: DF'],
                        ['mT2 120: DF',                 6.3, '$m_{T2} > 120$: DF'],
                        ['mT2 150: DF',                 4.6, '$m_{T2} > 50$: DF']
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
    fout.write('\\subsection*{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in table_lines_SF: fout.write(t + '\n')
    fout.write('\n')        
    for t in table_lines_DF: fout.write(t + '\n')    
    fout.write('\n')            
    fout.write(tex.end_document)


