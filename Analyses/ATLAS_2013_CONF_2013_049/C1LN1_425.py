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

    table_name = '$\\tilde \\chi_1^\\pm(425) \\to (\\ell \\tilde \\nu(250)  ~{\\rm or}~ \\nu \\tilde \\ell(75)) \\to \\nu \\ell  \\tilde \\chi_1^0(0)$ (ATLAS\\_CONF\\_2013\\_049)'
    description = ''

    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde \\chi_1^+ \\tilde \\chi_1^-: \\tilde \\chi_1^\\pm \\to (\\ell \\tilde \\nu  ~{\\rm or}~ \\nu \\tilde \\ell) \\to \\nu \\ell  \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde \\chi_1^\\pm} = 425$~GeV, $m_{\\tilde \\ell/\\tilde \\nu} = 250$~GeV, $m_{\\tilde \\chi_1^0} = 75$~GeV.
        \\item  The number of events: $2 \\cdot 10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption_ee = '''
        The cut-flow table for the $ee$ channel.
    '''
    table_caption_mm = '''
        The cut-flow table for the $\\mu \\mu$ channel.
    '''
    table_caption_em = '''
        The cut-flow table for the $e \\mu$ channel.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    #for key in eff_dict0: print key
    #exit()

    Ntot_exp = 40000.
    per = 100.
    
    initial_list_ee = [ 
                        ['ee: Trigger',   20.,  '$ee$: Trigger'],
                        ['ee: Z-veto',    19.,  '$ee$: $Z$ veto'],                        
                        ['ee: Jet veto',   7.0, '$ee$: Jet veto'],
                        ['ee: METrel',     6.0, '$ee$: ${\\rm MET}^{\\rm rel}$'],
                        ['ee: mT2 > 90',   4.3, '$ee$: $m_{T2} > 90$'],
                        ['ee: mT2 > 110',  3.7, '$ee$: $m_{T2} > 110$']
                        ]

    initial_list_mm = [ 
                        ['mm: Trigger',   20.,  '$\\mu \\mu$: Trigger'],
                        ['mm: Z-veto',    19.,  '$\\mu \\mu$: $Z$ veto'],                        
                        ['mm: Jet veto',   7.,  '$\\mu \\mu$: Jet veto'],
                        ['mm: METrel',     6.,  '$\\mu \\mu$: ${\\rm MET}^{\\rm rel}$'],
                        ['mm: mT2 > 90',   4.3, '$\\mu \\mu$: $m_{T2} > 90$'],
                        ['mm: mT2 > 110',  3.7, '$\\mu \\mu$: $m_{T2} > 110$']
                        ]

    initial_list_em = [ 
                        ['em: Trigger',   31.,  '$e \\mu$: Trigger'],
                        ['em: Z-veto',    29.,  '$e \\mu$: $Z$ veto'],                        
                        ['em: Jet veto',  11.,  '$e \\mu$: Jet veto'],
                        ['em: METrel',     9.,   '$e \\mu$: ${\\rm MET}^{\\rm rel}$'],
                        ['em: mT2 > 90',   6.7, '$e \\mu$: $m_{T2} > 90$'],
                        ['em: mT2 > 110',  5.7,  '$e \\mu$: $m_{T2} > 110$']
                        ]

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list_ee:
        eff_dict[name] = eff_dict0[name]/eff_dict0['ee: Trigger']
        err_dict[name] = err_dict0[name]/eff_dict0['ee: Trigger']        
    for name, val, texname in initial_list_mm:
        eff_dict[name] = eff_dict0[name]/eff_dict0['mm: Trigger']
        err_dict[name] = err_dict0[name]/eff_dict0['mm: Trigger']        
    for name, val, texname in initial_list_em:
        eff_dict[name] = eff_dict0[name]/eff_dict0['em: Trigger']
        err_dict[name] = err_dict0[name]/eff_dict0['em: Trigger']        

    NMC_first_ee = Ntot_exp * eff_dict0['ee: Trigger'] # geussed from Atom efficiency 
    table_lines_ee = cutflow_generation(ananame, vname+'_ee', table_caption_ee, initial_list_ee, eff_dict, err_dict, NMC_first_ee)
    NMC_first_mm = Ntot_exp * eff_dict0['mm: Trigger'] # geussed from Atom efficiency 
    table_lines_mm = cutflow_generation(ananame, vname+'_mm', table_caption_mm, initial_list_mm, eff_dict, err_dict, NMC_first_mm)
    NMC_first_em = Ntot_exp * eff_dict0['em: Trigger'] # geussed from Atom efficiency 
    table_lines_em = cutflow_generation(ananame, vname+'_em', table_caption_em, initial_list_em, eff_dict, err_dict, NMC_first_em)

    fout = open(vname + '.tex', 'w')
    tex = tex_format()
    fout.write(tex.begin_document)
    fout.write('\n')
    fout.write('\\subsection*{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in table_lines_ee: fout.write(t + '\n')
    fout.write('\n')            
    for t in table_lines_mm: fout.write(t + '\n')
    fout.write('\n')            
    for t in table_lines_em: fout.write(t + '\n')
    fout.write('\n')                
    fout.write(tex.end_document)

