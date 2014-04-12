#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *


if __name__ == '__main__':

    vname = 'GttN1_0L7J'

    table_name = '0-lepton 7-jet channel, Gtt model (ATLAS\\_CONF\\_2013\\_061)'
    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde g \\tilde g \\to (t \\bar t \\tilde \\chi_1^0) (t \\bar t \\tilde \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde g} = 1300$~GeV, $m_{\\tilde \\chi_1^0} = 100$~GeV.
        \\item  The number of events: $5 \\cdot 10^3$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for the 0-lepton 7-jet channel in Gtt model.
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
                    ["No cut",                     100.0, "No cut"],  # 0
                    ["0l-base: njet30 >= 4",       96.9,  "0l-base: $\\ge 4$ jets $(p_T > 30)$"], # 1
                    ["0l-base: pT1 > 90",          96.9,  "0l-base: $p_T(j_1) > 90$"], # 2
                    ["0l-base: MET > 150",         88.3,  "0l-base: MET $>$ 150"], # 3
                    ["0l-base: lepton veto",       45.9,  "0l-base: Lepton veto"], # 4
                    ["0l-base: delphi_4min > 0.5", 30.0,  "0l-base: $\\Delta \\phi_{\\rm min}^{4j} > 0.5$"], # 5
                    ["0l-base: MET/meff_4j > 0.2", 25.9,  "0l-base: ${\\rm MET}/m_{\\rm eff}^{4j} > 0.2$"], # 6

                    ["SR-0l-7j: njet30 >= 7",      24.6,  "SR-0l-7j: $\\ge 7$ jets $(p_T > 30)$"], # 7
                    ["SR-0l-7j: njet30_b >= 3",    11.5,  "SR-0l-7j: $\\ge 3$ $b$-jets $(p_T > 30)$"], # 8

                    ["SR-0l-7j-A: MET > 200",      11.3,  "SR-0l-7j-A: MET $>$ 200"], # 9
                    ["SR-0l-7j-A",                 11.3,  "SR-0l-7j-A"], # 10

                    ["SR-0l-7j-B: MET > 350",       9.2,  "SR-0l-7j-B: MET $>$ 350"], # 11
                    ["SR-0l-7j-B",                  9.2,  "SR-0l-7j-B"], # 12

                    ["SR-0l-7j-C: MET > 250",      10.8,  "SR-0l-7j-C: MET $>$ 250"], # 13
                    ["SR-0l-7j-C",                  9.5,  "SR-0l-7j-C"], # 14
                    ]

    i_denom = []
    for i in range(len(initial_list)): i_denom.append(i-1)
    i_denom[9] = 8
    i_denom[11] = 8
    i_denom[13] = 8

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


