#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import ROOT
import sys
import os
from math import *
from tex_witter import *

col = {
    'clear': '\033[0m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m'
}

def GetEfficiencies(filename):

    f = ROOT.TFile(filename)

    resulteff = []

    Nentries = ROOT.Efficiencies.GetEntries()

    effi = {}
    err = {}
    pid = {}
    ana_dict = {} 
    for i in xrange(Nentries):
        ROOT.Efficiencies.GetEntry(i)        
        name = ROOT.Efficiencies.name.split('\x00')[0]        
        ana = ROOT.Efficiencies.analysis
        ana_dict[ana] = ana
        __pid = ROOT.Efficiencies.procid
        __effi  = ROOT.Efficiencies.value
        __err  = ROOT.Efficiencies.error
        if __pid != 0: continue
        effi[name] = __effi
        err[name] = __err
        pid[name] = __pid

    AnaList = ana_dict.keys()
    if len(AnaList) > 1:
        print 'ERROR! More than one Analysis are found!!'
        for ana in AnaList: print ana

    return AnaList[0], effi, err, pid


def cutflow_generation(ananame, vname, table_name, description, table_caption, 
                       initial_list, eff_dict, err_dict, Ntot_exp):

    per = 100.

    #######################################################
    #          Setting experimental efficiencies          #  
    #######################################################
    name_list = []
    texname_list = []
    eff_exp = []
    err_exp = []
    nev_exp = []
    for name, inival, texname in initial_list:
        name_list.append(name)
        texname_list.append(texname)
        eff = inival/initial_list[0][1]
        nev = Ntot_exp * eff
        nerr = sqrt(nev)
        eff_err = nerr/Ntot_exp

        eff_exp.append(per * eff)
        err_exp.append(per * eff_err)
        nev_exp.append(nev)

    #######################################################
    #          Setting experimental efficiencies          #  
    #######################################################
    eff_atom = []
    err_atom = []
    ratio_eff = ['']
    ratio_eff_sig = ['']
    for i in range(len(name_list)):          
        name = name_list[i]
        eff = eff_dict[name]
        err = err_dict[name]
        eff_atom.append(per * eff)
        err_atom.append(per * err)
        if i > 0:
            ratio_eff.append( eff_atom[i]/eff_exp[i] )
            err = sqrt(err_atom[i]**2 + err_exp[i]**2)
            ratio_eff_sig.append( (eff_atom[i] - eff_exp[i])/err )

    #######################################################
    #          Setting relative efficiencies              #  
    #######################################################
    i_denom = ['']
    Reff_exp = ['']
    Rerr_exp = ['']
    Reff_atom = ['']
    Rerr_atom = ['']
    ratio_R = ['']
    ratio_R_sig = ['']    
    for i in range(1, len(name_list)):      
        nev = nev_exp[i]
        iprev = i - 1
        prevnev = nev_exp[iprev]
        Reff_exp.append(nev/prevnev)
        Rerr_exp.append(sqrt(nev)/prevnev)

        eff = eff_atom[i]
        err = err_atom[i]        
        preveff = eff_atom[iprev]
        Reff_atom.append(eff/preveff)
        Rerr_atom.append(err/preveff)

        i_denom.append(iprev)

        ratio_R.append( Reff_atom[i]/Reff_exp[i] )

        error = sqrt(Rerr_exp[i]**2 + Rerr_atom[i]**2)
        ratio_R_sig.append( (Reff_atom[i] - Reff_exp[i])/error )

    #######################################################
    #                       Display                       #  
    #######################################################
    show_cutflow(ananame, vname, 'Exp', name_list, 
                 eff_exp, err_exp, eff_atom, err_atom, ratio_eff, ratio_eff_sig, 
                 i_denom, Reff_exp, Rerr_exp, Reff_atom, Rerr_atom, ratio_R, ratio_R_sig)    

    texlines = make_table(ananame, vname, table_name, description, table_caption, 
               texname_list, eff_exp, err_exp, eff_atom, err_atom, ratio_eff, ratio_eff_sig, 
               i_denom, Reff_exp, Rerr_exp, Reff_atom, Rerr_atom, ratio_R, ratio_R_sig)

    return texlines


def strout(val, n, sp, defcol='clear', warncol='clear', flag=False):

    if flag == False:
        return col[defcol] + str(round(val, 2)).rjust(sp) + col['clear']
    else:
        return col[warncol] + str(round(val, 2)).rjust(sp) + col['clear']

def show_cutflow(ananame, vname, expname, name_list, 
                 eff_exp, err_exp, eff_atom, err_atom, ratio_eff, ratio_eff_sig, 
                 i_denom, Reff_exp, Rerr_exp, Reff_atom, Rerr_atom, ratio_R, ratio_R_sig):

    sp = {}
    sp['num'] = 3
    sp['eff_exp'] = 6
    sp['err_exp'] = 5
    sp['eff_atom'] = 7
    sp['err_atom'] = 5
    sp['ratio_eff'] = 11
    sp['ratio_eff_sig'] = 16
    sp['i_denom'] = 3    
    sp['Reff_exp'] = 6
    sp['Rerr_exp'] = 5
    sp['Reff_atom'] = 6
    sp['Rerr_atom'] = 5
    sp['ratio_R'] = 11
    sp['ratio_R_sig'] = 16
    sp['name'] = max([len(name) for name in name_list]) + 2

    print ' ' * 158

    print str(ananame) + ': ' + str(vname)

    print '-' * 158

    head  = '#'.rjust(sp['num']) + ('cut name').rjust(sp['name']) 
    head += ' | ' 
    head += ('eff_' + expname + ' ').rjust(sp['eff_exp'] + 4 + sp['err_exp']) 
    head += ('eff_Atom ').rjust(sp['eff_atom'] + 4 + sp['err_atom']) 
    head += ('Atom/' + expname).rjust(sp['ratio_eff']) 
    head += ('(Atom-' + expname + ')/Err').rjust(sp['ratio_eff_sig'])  
    head += ' | '
    head += '#/?'
    head += ('R_' + expname + ' ').rjust(sp['Reff_exp'] + 4 + sp['Rerr_exp']) 
    head += ('R_Atom ').rjust(sp['Reff_atom'] + 4 + sp['Rerr_atom']) 
    head += ('Atom/' + expname).rjust(sp['ratio_eff']) 
    head += ('(Atom-' + expname + ')/Err').rjust(sp['ratio_eff_sig'])  

    print head

    print '-' * 158

    for i in range(len(name_list)):

        warning = []

        pm = '    '
        xxeff_exp = strout(eff_exp[i], 2, sp['eff_exp'])                
        xxeff_atom = strout(eff_atom[i], 2, sp['eff_atom'])                        
        xxerr_exp = ' '.rjust(sp['err_exp'])
        xxerr_atom = ' '.rjust(sp['err_atom'])
        xxratio_eff = ' '.rjust(sp['ratio_eff'])
        xxratio_eff_sig = ' '.rjust(sp['ratio_eff_sig'])
        if i > 0:
            xxerr_exp = strout(err_exp[i], 2, sp['err_exp'])
            xxerr_atom = strout(err_atom[i], 2, sp['err_atom'])            
            if abs(1. - ratio_eff[i]) > 0.3 and abs(ratio_eff_sig[i]) > 3.: 
                xxratio_eff = strout(ratio_eff[i], 2, sp['ratio_eff'], 'red')
            elif abs(1. - ratio_eff[i]) > 0.3:
                xxratio_eff = strout(ratio_eff[i], 2, sp['ratio_eff'], 'blue')
            else:
                xxratio_eff = strout(ratio_eff[i], 2, sp['ratio_eff'], 'green')
            xxratio_eff_sig = strout(ratio_eff_sig[i], 2, sp['ratio_eff_sig'])

            pm = ' +- '

        line  = str(i).rjust(sp['num']) + name_list[i].rjust(sp['name']) + ' | ' 
        line += xxeff_exp + pm + xxerr_exp 
        line += xxeff_atom + pm + xxerr_atom 
        line += xxratio_eff        
        line += xxratio_eff_sig

        #######################################################
        line += ' | '                

        xxReff_exp = ' '.rjust(sp['Reff_exp'])
        xxRerr_exp = ' '.rjust(sp['Rerr_exp'])
        xxReff_atom = ' '.rjust(sp['Reff_atom'])
        xxRerr_atom = ' '.rjust(sp['Rerr_atom'])
        xxratio_R = ' '.rjust(sp['ratio_R'])
        xxratio_R_sig = ' '.rjust(sp['ratio_R_sig'])
        if i > 0:
            xxReff_exp = strout(Reff_exp[i], 2, sp['Reff_exp'])
            xxRerr_exp = strout(Rerr_exp[i], 2, sp['Rerr_exp'])
            xxReff_atom = strout(Reff_atom[i], 2, sp['Reff_atom'])
            xxRerr_atom = strout(Rerr_atom[i], 2, sp['Rerr_atom'])
            if abs(1. - ratio_R[i]) > 0.3 and abs(ratio_R_sig[i]) > 5.:
                xxratio_R = strout(ratio_R[i], 2, sp['ratio_R'], 'red')
            elif abs(1. - ratio_R[i]) > 0.3:
                xxratio_R = strout(ratio_R[i], 2, sp['ratio_R'], 'blue')
            else:
                xxratio_R = strout(ratio_R[i], 2, sp['ratio_R'], 'green')
            xxratio_R_sig = strout(ratio_R_sig[i], 2, sp['ratio_R_sig'])
        line += str(i_denom[i]).rjust(sp['i_denom'])
        line += xxReff_exp + pm + xxRerr_exp 
        line += xxReff_atom + pm + xxRerr_atom 
        line += xxratio_R 
        line += xxratio_R_sig

        print line 


    print ' ' * 158
