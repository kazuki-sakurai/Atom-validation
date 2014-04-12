#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *


if __name__ == '__main__':

    vname = 'GbbN1_0L4J'

    table_name = '0-lepton 4-jet channel, Gbb model (ATLAS\\_CONF\\_2013\\_061)'
    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde g \\tilde g \\to (b \\bar b \\tilde \\chi_1^0) (b \\bar b \\tilde \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde g} = 1300$~GeV, $m_{\\tilde \\chi_1^0} = 100$~GeV.
        \\item  The number of events: $10^3$.
        \\item  Event Generator: {\\tt MadGraph 5} and {\\tt Pythia 6}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for the 0-lepton 4-jet channel in Gbb model.
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
                    ["No cut",               100.0, "No cut"],  # 0
                    ["0l-base: njet30 >= 4", 95.4,  "0l-base: $\\ge 4$ jets $(p_T > 30)$"], # 1
                    ["0l-base: pT1 > 90",    95.4,  "0l-base: $p_T(j_1) > 90$"], # 2
                    ["0l-base: MET > 150",   88.7,  "0l-base: MET $>$ 150"], # 3
                    ["0l-base: lepton veto", 88.7,  "0l-base: Lepton veto"], # 4
                    ["0l-base: delphi_4min > 0.5",  58.5,  "0l-base: $\\Delta \\phi_{\\rm min}^{4j} > 0.5$"], # 5
                    ["0l-base: MET/meff_4j > 0.2",  46.2,  "0l-base: ${\\rm MET}/m_{\\rm eff}^{4j} > 0.2$"], # 6

                    ["SR-0l-4j-A: njet30 >= 4",    46.2,  "SR-0l-4j-A: $\\ge 4$ jets $(p_T > 30)$"], # 7
                    ["SR-0l-4j-A: njet30_b >= 3",  20.5,  "SR-0l-4j-A: $\\ge 3$ $b$-jets $(p_T > 30)$"], # 8
                    ["SR-0l-4j-A: MET > 200",      20.5,  "SR-0l-4j-A: MET $>$ 200"], # 9
                    ["SR-0l-4j-A: meff_4j > 1000", 20.3,  "SR-0l-4j-A: $m_{\\rm eff}^{4j} > 1000$"], # 10
                    ["SR-0l-4j-A",                 10.8,  "SR-0l-4j-A"], # 11

                    ["SR-0l-4j-B: njet50 >= 4",    42.8,  "SR-0l-4j-B: $\\ge 4$ jets $(p_T > 50)$"], # 12
                    ["SR-0l-4j-B: njet50_b >= 3",  17.9,  "SR-0l-4j-B: $\\ge 3$ $b$-jets $(p_T > 50)$"], # 13
                    ["SR-0l-4j-B: MET > 350",      16.2,  "SR-0l-4j-B: MET $>$ 350"], # 14
                    ["SR-0l-4j-B",                 15.9,  "SR-0l-4j-B"], # 15

                    ["SR-0l-4j-C: njet50 >= 4",    42.8,  "SR-0l-4j-C: $\\ge 4$ jets $(p_T > 50)$"], # 16
                    ["SR-0l-4j-C: njet50_b >= 3",  17.9,  "SR-0l-4j-C: $\\ge 3$ $b$-jets $(p_T > 50)$"], # 17
                    ["SR-0l-4j-C: MET > 250",      17.4,  "SR-0l-4j-C: MET $>$ 250"], # 18
                    ["SR-0l-4j-C",                 15.9,  "SR-0l-4j-C"], # 19
                    ]

    i_denom = []
    for i in range(len(initial_list)): i_denom.append(i-1)
    i_denom[7] = 6
    i_denom[12] = 6
    i_denom[16] = 6

    NMC_first = Ntot_exp  
    texlines = cutflow_generation(ananame, vname, table_caption, initial_list, eff_dict, err_dict, NMC_first, i_denom)    

    fout = open(vname + '.tex', 'w')
    tex = tex_format()
    fout.write(tex.begin_document)
    fout.write('\n')
    fout.write('\\subsection*{' + table_name + '} \n')
    fout.write('\n')    
    fout.write(description)    
    fout.write('\n')        
    for t in texlines: fout.write(t + '\n')
    fout.write(tex.end_document)


