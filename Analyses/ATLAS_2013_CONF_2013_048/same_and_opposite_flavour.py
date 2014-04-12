#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *

if __name__ == '__main__':

    vname = 'same_and_opposite_flavour'

    table_name = '$\\tilde t_1(400) \\to b \\tilde \\chi_1^+(250) \\to W^+ \\tilde \\chi_1^0(1)$ (ATLAS\\_CONF\\_2013\\_048)'
    description = '''
        \\begin{itemize}
        \\item  Process: $pp \\to \\tilde t_1 \\tilde t_1^*: \\tilde t_1 \\to b \\tilde \\chi_1^+ \\to W^+ \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde t_1} = 400$~GeV, $m_{\\tilde \\chi_1^\\pm} = 250$~GeV, $m_{\\tilde \\chi_1^0} = 1$~GeV.
        \\item  The number of events: $3 \\cdot 10^4$.
        \\item  Event Generator: {\\tt MadGraph 5} and {\\tt Pythia 6}.    
        \\end{itemize}    
    '''
    table_caption_SF = '''
        The cut-flow table for the same flavour channel.
    '''
    table_caption_DF = '''
        The cut-flow table for the opposite flavour channel.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict0, err_dict0, pid = GetEfficiencies(inputfile)

    Ntot_exp = 50000.
    per = 100.
    
    initial_list_SF = [ 
                    ["Same Flavour",          1369.5,  "Same Flavour"],
                    ["SF: Opposite Sign",     1339.6,  "SF: Opposite Sign"],              
                    ["SF: m_ll > 20",         1322.3,  "SF: $m_{\\ell \\ell} > 20$"],
                    ["SF: Leading lepton pT", 1301.2,  "SF: Leading lepton $p_T$"],
                    ["SF: |m_ll - mZ| > 20",  963.8,   "SF: $|m_{\\ell \\ell} - m_Z| > 20$"],
                    ["SF: delPhi_min > 1",    506.2,   "SF: $\\Delta \\phi_{\\rm min} > 1$"],               
                    ["SF: delPhi_b < 1.5",    487.3,   "SF: $\\Delta \\phi_b < 1.5$"],       
                    ["SF: M90",               107.5,   "SF: M90"],
                    ["SF: M100",              45.8,    "SF: M100"], 
                    ["SF: M110",              51.8,    "SF: M110"],
                    ["SF: M120",              34.3,    "SF: M120"]
                    ]


    initial_list_DF = [ 
                    ["Opposite Flavour",      1301.1, "Opposite Flavour"],                          
                    ["OF: Opposite Sign",     1267.6, "OF: Opposite Sign"],          
                    ["OF: m_ll > 20",         1254.5, "OF: $m_{\\ell \\ell} > 20$"],
                    ["OF: Leading lepton pT", 1233.7, "OF: Leading lepton $p_T$"],
                    ["OF: delPhi_min > 1",    607.3,  "OF: $\\Delta \\phi_{\\rm min} > 1$"],                                
                    ["OF: delPhi_b < 1.5",    586.1,  "OF: $\\Delta \\phi_b < 1.5$"],
                    ["OF: M90",               123.7,  "OF: M90"],
                    ["OF: M100",              43.3,   "OF: M100"],
                    ["OF: M110",              65.8,   "OF: M110"],      
                    ["OF: M120",              47.4,   "OF: M120"]
                    ]     

    eff_dict = {}
    err_dict = {}
    for name, val, texname in initial_list_SF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['Same Flavour']
        err_dict[name] = err_dict0[name]/eff_dict0['Same Flavour']        
    for name, val, texname in initial_list_DF:
        eff_dict[name] = eff_dict0[name]/eff_dict0['Opposite Flavour']
        err_dict[name] = err_dict0[name]/eff_dict0['Opposite Flavour']        

    NMC_first_SF = initial_list_SF[0][1]
    table_lines_SF = cutflow_generation(ananame, vname+'_SF', table_caption_SF, initial_list_SF, eff_dict, err_dict, NMC_first_SF)
    NMC_first_DF = initial_list_DF[0][1]
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

