#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *


if __name__ == '__main__':

    vname = 'GttN1_1L6J'

    table_name = '1-lepton 6-jet channel, Gtt model (ATLAS\\_CONF\\_2013\\_061)'
    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde g \\tilde g \\to (t \\bar t \\tilde \\chi_1^0) (t \\bar t \\tilde \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde g} = 1300$~GeV, $m_{\\tilde \\chi_1^0} = 100$~GeV.
        \\item  The number of events: $5 \\cdot 10^3$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for the 1-lepton 6-jet channel in Gtt model.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    Ntot_exp = 100000. 
    per = 100.

    eff_dict['No cut'] = 1.
    err_dict['No cut'] = 0.

    #for key in eff_dict0: print key
    #exit()

    initial_list = [ 
                    ["No cut",                           100.0,  "No cut"],  # 0    
                    ["1l-base: njet30 >= 4",              96.9,  "1l-base: $\\ge 4$ jets $(p_T > 30)$"],  # 1    
                    ["1l-base: pT1 > 90",                 96.8,  "1l-base: $p_T(j_1) > 90$"],  # 2
                    ["1l-base: MET > 150",                88.3,  "1l-base: MET $>$ 150"],  # 3
                    ["1l-base: nlep >= 1",                40.9,  "1l-base: $>= 1$ signal lepton"],  # 4
                    ["SR-1l-6j: njet30 >= 6",             37.3,  "SR-1l-6j: $\\ge 6$ jets $(p_T > 30)$"],  # 5
                    ["SR-1l-6j: njet30_b >= 3",           14.3,  "SR-1l-6j: $\\ge 3$ $b$-jets $(p_T > 30)$"],  # 6

                    ["SR-1l-6j-A: mT > 140",              11.3,  "SR-1l-6j-A: $m_T > 140$"],  # 7
                    ["SR-1l-6j-A: MET > 175",             10.9,  "SR-1l-6j-A: MET $>$ 175"],  # 8
                    ["SR-1l-6j-A: MET/sqrt(HT_inc) > 5",  10.8,  "SR-1l-6j-A: ${\\rm MET}/\\sqrt(H_T({\\rm inc})) > 5$"],  # 9
                    ["SR-1l-6j-A",                        10.8,  "SR-1l-6j-A"],  # 10

                    ["SR-1l-6j-B: mT > 140",              11.3,  "SR-1l-6j-B: $m_T > 140$"],  # 11
                    ["SR-1l-6j-B: MET > 225",             10.0,  "SR-1l-6j-B: MET $>$ 225"],  # 12
                    ["SR-1l-6j-B: MET/sqrt(HT_inc) > 5",  10.0,  "SR-1l-6j-B: $MET/\\sqrt(H_T({\\rm inc})) > 5$"],  # 13
                    ["SR-1l-6j-B",                        10.0,  "SR-1l-6j-B"],  # 14

                    ["SR-1l-6j-C: mT > 160",              10.7,  "SR-1l-6j-C: $m_T > 160$"],  # 15
                    ["SR-1l-6j-C: MET > 275",              8.8,  "SR-1l-6j-C: MET $>$ 275"],  # 16
                    ["SR-1l-6j-C: MET/sqrt(HT_inc) > 5",   8.8,  "SR-1l-6j-C: ${\\rm MET}/\\sqrt(H_T({\\rm inc})) > 5$"],  # 17
                    ["SR-1l-6j-C",                         8.8,  "SR-1l-6j-C"]  # 18

                    ]

    i_denom = []
    for i in range(len(initial_list)): i_denom.append(i-1)
    i_denom[7] = 6
    i_denom[11] = 6
    i_denom[15] = 6

    NMC_first = Ntot_exp 
    texlines = cutflow_generation(ananame, vname, table_caption, initial_list, eff_dict, err_dict, NMC_first, i_denom)    

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


