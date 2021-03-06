#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *


if __name__ == '__main__':

    vname = 'stopR'

    table_name = '$\\tilde t_R \\tilde t_R^* \\to t \\tilde \\chi_1^0 \\bar t \\tilde \\chi_1^0$ (ATLAS\\_CONF\\_2013\\_024)'
    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde t_{L/R} \\tilde t_{L/R}^* \\to t \\tilde \\chi_1^0 \\bar t \\tilde \\chi_1^0$.
        \\item  Mass: $m_{\\tilde t_{L/R}} = 600$~GeV, $m_{\\tilde \\chi_1^0} = 0$~GeV.
        \\item  The number of Atom MC events: $10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}            
    '''
    table_caption = '''
        The cut-flow table for the $\\tilde t_R \\tilde t_R^*$.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    Ntot_exp = 250000.
    per = 100.
    
    eff_dict['No-cut'] = 1.
    err_dict['No-cut'] = 0.

    initial_list = [ # ATLAS results: number is scalled for the 600 stop xsec with 20.5/fb
                    ['No-cut',                        507.3,  'No cut'],
                    ['Muon veto',                     381.2,  '$\\mu$ veto'],                            
                    ['Electron veto',                 284.1,  '$e$ veto'],                    
                    ['MET > 130',                     263.1,  'MET $>$ 130'],
                    ['Jet multiplicity and pT',        97.3,  '$N_{\\rm jets}$ and $p_T$'],
                    ['MET_track > 30',                 96.3,  '$\\rm MET_{track} > 30$'], 
                    ['delPhi(MET, MET_track) < pi/3',  90.3,  '$\\Delta \\phi (\\rm MET, MET_{track}) < \\pi/3$'],
                    ['delPhi(jet, MET) > pi/5',        77.1,  '$\\Delta \\phi (\\rm jet, MET) > \\pi/5$'],
                    ['Tau veto',                       67.4,  '$\\tau$ veto'], 
                    [">= 2-bjet",                      29.5,  '$\ge$ 2-bjets'],     
                    ['mT(bjet, MET) > 175',            20.2,  '$m_T(\\rm bjet, MET) > 175$'], 
                    ['80 < m^0_jjj < 270',             17.8,  '$80 < m^0_{jjj} < 270$'],   
                    ['80 < m^1_jjj < 270',             10.9,  '$80 < m^1_{jjj} < 270$'],                  
                    ['SR1: MET > 200',                 10.3,  'SR1: $\\rm MET > 200$'],                    
                    ['SR2: MET > 300',                  7.8,  'SR2: $\\rm MET > 300$'],                    
                    ['SR3: MET > 350',                  6.1,  'SR3: $\\rm MET > 350$']
                    ]

    NMC_first = Ntot_exp * initial_list[0][1] / initial_list[0][1]
    texlines = cutflow_generation(ananame, vname, table_caption, initial_list, eff_dict, err_dict, NMC_first)

    fout = open(vname + '.tex', 'w')
    tex = tex_format()
    fout.write(tex.begin_document)
    fout.write('\n')
    fout.write('\\subsection{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in texlines: fout.write(t + '\n')
    fout.write(tex.end_document)

