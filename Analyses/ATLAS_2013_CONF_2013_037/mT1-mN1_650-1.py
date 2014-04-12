#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *


if __name__ == '__main__':

    vname = 'mT1-mN1_650-1'

    table_name = '$\\tilde t_1(650) \\to t \\tilde \\chi_1^0(1)$ (ATLAS\\_CONF\\_2013\\_037)'
    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde t_1 \\tilde t_1^* \\to (t \\tilde \\chi_1^0) (\\bar t \\tilde \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde t_1} = 650$~GeV, $m_{\\tilde \\chi_1^0} = 1$~GeV.
        \\item  The number of events: $5 \\cdot 10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for the $\\tilde t_1(500) \\to t \\tilde \\chi_1^0(200)$ model.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    Ntot_exp = 50004.0 
    per = 100.

    eff_dict['[01] No cut'] = 1.
    err_dict['[01] No cut'] = 0.

    #for key in eff_dict0: print key
    #exit()

    Ntrigger = 215340.1 + 209318.5

    initial_list = [ 
                    ["[01] No cut",                  50004.0,           "[00] No cut"],    # 0                        
                    ["[02] Lepton (=1 signal)",      6229.3 + 5557.1,   "[02] Lepton ($=1$ signal)"],  # 1
                    ["[03] 4jets (80,60,40,25)",     4149.2 + 3704.8,   "[03] 4jets (80,60,40,25)"],    # 2
                    ["[04] >=1b in 4 leading jets",  3524.6 + 3145.2,   "[04] $>=1$ b in 4 leading jets"],  # 3
                    ["[05] MET > 100",               3258.2 + 2930.0,   "[05] MET $>$ 100"],  # 4
                    ["[06] MET/sqrt(HT) > 5",        3186.6 + 2884.2,   "[06] ${\\rm MET}/\\sqrt(H_T) > 5$"], # 5    
                    ["[07] delPhi(J2,MET) > 0.8",    2906.7 + 2649.1,   "[07] $\\Delta \\phi(j_2, {\\rm MET}) > 0.8$"], # 6

                    ["[SRtN2] MET > 200",            2425.0 + 2210.6,   "[SRtN2] MET $>$ 200"], # 7        
                    ["[SRtN2] MET/sqrt(HT) > 13",    1755.3 + 1619.1,   "[SRtN2] ${\\rm MET}/\\sqrt(H_T) > 13$"], # 8
                    ["[SRtN2] mT > 140",             1619.5 + 1474.9,   "[SRtN2] $m_T > 140$"], # 9

                    ["[SRtN3] MET > 275",            1843.4 + 1691.0,   "[SRtN3] MET $>$ 275"],  # 10
                    ["[SRtN3] MET/sqrt(HT) > 11",    1843.4 + 1649.1,   "[SRtN3] $MET/\\sqrt(H_T) > 11$"], # 11  
                    ["[SRtN3] mT > 200",             1461.4 + 1308.7,   "[SRtN3] $m_T > 200$"],  # 12

                    ["[SRbC1-3] MET > 150",          2669.9 + 2448.0,   "[SRbC1-3] MET $>$ 150"],  # 13
                    ["[SRbC1-3] MET/sqrt(HT) > 7",   2622.2 + 2404.3,   "[SRbC1-3] ${\\rm MET}/\\sqrt(H_T) > 7$"],  # 14
                    ["[SRbC1-3] mT > 120",           2303.9 + 2088.3,   "[SRbC1-3] $m_T > 120$"],  # 15
                    ["[SRbC1-3] MET > 160",          2284.4 + 2065.6,   "[SRbC1-3] MET $>$ 160"],  # 16
                    ["[SRbC1-3] MET/sqrt(HT) > 8",   2238.8 + 2017.8,   "[SRbC1-3] ${\\rm MET}/\\sqrt(H_T) > 8$"], # 17
                    ["[SRbC1-3] meff > 550",         2223.5 + 1999.6,   "[SRbC1-3] $m_{\\rm eff} > 550$"],  # 18
                    ["[SRbC1-3] meff > 700",         2066.8 + 1851.7,   "[SRbC1-3] $m_{\\rm eff} > 700$"],  # 19

                    ["SRtN2",                        827.07 + 779.26,   "SRtN2"], # 20
                    ["SRtN3",                        702.92 + 656.11,   "SRtN3"], # 21                  
                    ["SRbC1",                        1673.95+ 1533.48,  "SRbC1"], # 22                     
                    ["SRbC2",                        492.09 + 452.51,   "SRbC2"], # 23                
                    ["SRbC3",                        274.80 + 248.60,   "SRbC3"]  # 24    
                    ]

    i_denom = []
    for i in range(len(initial_list)): i_denom.append(i-1)
    i_denom[10] = 6
    i_denom[13] = 6
    i_denom[20] = 9
    i_denom[21] = 12
    i_denom[22] = 6
    i_denom[23] = 6
    i_denom[24] = 6

    NMC_first = initial_list[0][1] 
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


