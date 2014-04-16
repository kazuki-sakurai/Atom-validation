#!usr/bin/env python

import sys
import os
from functions import *

def ToTexFormat(t):
    res = ''
    for p in t.split('_'): res += p + '\\_'
    return res[:-2]

Input = ''
try:
    for i in range(1, len(sys.argv)): Input = sys.argv[i] + ' '
except: pass

if Input == '': Input = 'analyses_list'

infile = 'tex/list.dat'
os.system('sh for_tex.sh ' + Input + ' > ' + infile)

ana_list = []
vname_dict = {}
vlist = []
for line in open(infile):
    tag, name = line.split()
    if tag == 'ananame':
        if len(ana_list) > 0: vname_dict[ana] = vlist 
        vlist = []
        ana_list.append(name)        
        ana = name
    if tag == 'vname': vlist.append(name)
vname_dict[ana] = vlist 

#for ana in ana_list:
#    print ana
#    for vname in vname_dict[ana]: print '  ', vname

for ana in ana_list:
    tabdir = 'tex/' + ana 
    os.system('rm -rf ' + tabdir)                
    os.system('mkdir ' + tabdir)            
    for vname in vname_dict[ana]:        
        target = 'Analyses/' + ana + '/' + vname + '.tex'
        if os.path.exists(target):
            tabpath = tabdir + '/' + vname + '.tab.tex'
            ftab = open(tabpath, 'w')
            print tabpath
            flag = False
            for line in open(target):
                if len(line.split("begin{document}")) == 2: 
                    flag = True
                    continue
                if len(line.split("end{document}")) == 2: break 
                if flag: ftab.write(line)
            ftab.close() 
        else:
            print '#' * 50
            print 'Error!!!'
            print target + '  does not exist!!'            
            print '#' * 50
            exit()


tex = tex_format()

output = 'tex/CF_table.tex'

fout = open(output, 'w')

fout.write(tex.begin_document_CF)
fout.write('\n')

line_list = []
for ana in ana_list:
    anatex = ToTexFormat(ana)
    line_list.append('\\section{' + anatex + '}' + '\n')
    line_list.append('\n')    
    for vname in vname_dict[ana]: 
        tname = ana + '/' + vname + '.tab.tex'
        line_list.append('\\input{' + tname + '}' + '\n')
        line_list.append('\\newpage')
    line_list.append('\\newpage')
    line_list.append('~')    
    line_list.append('\\newpage')    

for t in line_list: fout.write(t)

fout.write('\n')
fout.write(tex.end_document)




