#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import sys
import os
from math import *
sys.path.append('../..')
from functions import *


if __name__ == '__main__':

    vname = 'mT1-mN1_500-200'

    table_name = '$\\tilde t_1(500) \\to t \\tilde \\chi_1^0(200)$ (ATLAS\\_CONF\\_2013\\_037)'
    description = '''
        \\begin{itemize}
        \\item  Process: $\\tilde t_1 \\tilde t_1^* \\to (t \\tilde \\chi_1^0) (\\bar t \\tilde \\chi_1^0)$.
        \\item  Mass: $m_{\\tilde t_1} = 500$~GeV, $m_{\\tilde \\chi_1^0} = 200$~GeV.
        \\item  The number of events: $10^4$.
        \\item  Event Generator: {\\tt Herwig++ 2.5.2}.    
        \\end{itemize}    
    '''

    table_caption = '''
        The cut-flow table for the $\\tilde t_1(500) \\to t \\tilde \\chi_1^0(200)$ model.
    '''

    inputfile = vname + '.root'
    if len(sys.argv) == 2: inputfile = sys.argv[1]    

    ananame, eff_dict, err_dict, pid = GetEfficiencies(inputfile)

    Ntot_exp = 99989.9
    per = 100.

    eff_dict['[01] No cut'] = 1.
    err_dict['[01] No cut'] = 0.

    #for key in eff_dict0: print key
    #exit()

    initial_list = [ 
                    ["[01] No cut",                  99989.9,             "[00] No cut"],    # 0                        
                    ["[02] Lepton (=1 signal)",      (11784.9+ 11025.8),  "[02] Lepton ($=1$ signal)"],  # 1
                    ["[03] 4jets (80,60,40,25)",     (6271.4 + 6062.9),   "[03] 4jets (80,60,40,25)"],    # 2
                    ["[04] >=1b in 4 leading jets",  (5388.8 + 5144.1),   "[04] $>=1$ b in 4 leading jets"],  # 3
                    ["[05] MET > 100",               (4392.5 + 4252.2),   "[05] MET $>$ 100"],  # 4
                    ["[06] MET/sqrt(HT) > 5",        (4285.9 + 4161.5),   "[06] ${\\rm MET}/\\sqrt(H_T) > 5$"], # 5    
                    ["[07] delPhi(J2,MET) > 0.8",    (3816.5 + 3816.5),   "[07] $\\Delta \\phi(j_2, {\\rm MET}) > 0.8$"], # 6

                    ["[SRtN2] MET > 200",            (2185.9 + 2123.0),   "[SRtN2] MET $>$ 200"], # 7        
                    ["[SRtN2] MET/sqrt(HT) > 13",    (1172.0 + 1158.7),   "[SRtN2] ${\\rm MET}/\\sqrt(H_T) > 13$"], # 8
                    ["[SRtN2] mT > 140",             (973.9  +  937.6),   "[SRtN2] $m_T > 140$"], # 9

                    ["[SRtN3] MET > 275",            (965.0  + 903.9),    "[SRtN3] MET $>$ 275"],  # 10
                    ["[SRtN3] MET/sqrt(HT) > 11",    (937.4  + 883.1),    "[SRtN3] $MET/\\sqrt(H_T) > 11$"], # 11  
                    ["[SRtN3] mT > 200",             (565.6  + 487.6),    "[SRtN3] $m_T > 200$"],  # 12

                    ["[SRbC1-3] MET > 150",          (3080.1 + 2950.1),   "[SRbC1-3] MET $>$ 150"],  # 13
                    ["[SRbC1-3] MET/sqrt(HT) > 7",   (3017.2 + 2898.3),   "[SRbC1-3] ${\\rm MET}/\\sqrt(H_T) > 7$"],  # 14
                    ["[SRbC1-3] mT > 120",           (2347.1 + 2230.9),   "[SRbC1-3] $m_T > 120$"],  # 15
                    ["[SRbC1-3] MET > 160",          (2256.6 + 2133.8),   "[SRbC1-3] MET $>$ 160"],  # 16
                    ["[SRbC1-3] MET/sqrt(HT) > 8",   (2174.8 + 2085.3),   "[SRbC1-3] ${\\rm MET}/\\sqrt(H_T) > 8$"], # 17
                    ["[SRbC1-3] meff > 550",         (2042.0 + 1972.2),   "[SRbC1-3] $m_{\\rm eff} > 550$"],  # 18
                    ["[SRbC1-3] meff > 700",         (1397.8 + 1263.8),   "[SRbC1-3] $m_{\\rm eff} > 700$"],  # 19

                    ["SRtN2",                        (408.46 + 431.46),   "SRtN2"], # 20
                    ["SRtN3",                        (191.84 + 190.26),   "SRtN3"], # 21                  
                    ["SRbC1",                        (1566.12+ 1543.63),  "SRbC1"], # 22                     
                    ["SRbC2",                        (297.30 + 298.78),   "SRbC2"], # 23                
                    ["SRbC3",                        (84.32  + 75.32),    "SRbC3"]  # 24    
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


