#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import ROOT
import sys
import os

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


def show_cutflow(ananame, vname, expname, name_list, 
                 eff_exp, err_exp, eff_atom, err_atom, ratio_eff, ratio_eff_sig, 
                 Reff_exp, Rerr_exp, Reff_atom, Rerr_atom, ratio_R, ratio_R_sig):

    sp = {}
    sp['num'] = 3
    sp['eff_exp'] = 6
    sp['err_exp'] = 5
    sp['eff_atom'] = 7
    sp['err_atom'] = 5
    sp['ratio_eff'] = 11
    sp['ratio_eff_sig'] = 18
    sp['Reff_exp'] = 5
    sp['Rerr_exp'] = 5
    sp['Reff_atom'] = 6
    sp['Rerr_atom'] = 5
    sp['ratio_R'] = 11
    sp['ratio_R_sig'] = 18
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
    head += ('R_' + expname + ' ').rjust(sp['Reff_exp'] + 4 + sp['Rerr_exp']) 
    head += ('R_Atom ').rjust(sp['Reff_atom'] + 4 + sp['Rerr_atom']) 
    head += ('Atom/' + expname).rjust(sp['ratio_eff']) 
    head += ('(Atom-' + expname + ')/Err').rjust(sp['ratio_eff_sig'])  

    print head

    print '-' * 158

    for i in range(len(name_list)):

        pm = '    '
        xxerr_exp = ''
        xxerr_atom = ''
        xxratio_eff = ratio_eff[i]
        xxratio_eff_sig = ratio_eff_sig[i]        
        if i > 0:
            xxerr_exp = str(round(err_exp[i], 2))
            xxerr_atom = str(round(err_atom[i], 2))            
            xxratio_eff = str(round(ratio_eff[i], 2))
            xxratio_eff_sig = str(round(ratio_eff_sig[i], 2))        
            pm = ' +- '

        line  = str(i).rjust(sp['num']) + name_list[i].rjust(sp['name']) + ' | ' 
        line += str(round(eff_exp[i], 2)).rjust(sp['eff_exp']) + pm + xxerr_exp.ljust(sp['err_exp']) 
        line += str(round(eff_atom[i], 2)).rjust(sp['eff_atom']) + pm + xxerr_atom.ljust(sp['err_atom'])

        line += xxratio_eff.rjust(sp['ratio_eff'])             
        line += xxratio_eff_sig.rjust(sp['ratio_eff_sig'])             

        #######################################################
        line += ' | '                

        xxReff_exp = Reff_exp[i]
        xxRerr_exp = Rerr_exp[i]
        xxReff_atom = Reff_atom[i]
        xxRerr_atom = Rerr_atom[i]
        xxratio_R = ratio_R[i]
        xxratio_R_sig = ratio_R_sig[i]
        if i > 0:
            xxReff_exp = str(round(Reff_exp[i], 2))
            xxRerr_exp = str(round(Rerr_exp[i], 2))
            xxReff_atom = str(round(Reff_atom[i], 2))
            xxRerr_atom = str(round(Rerr_atom[i], 2))
            xxratio_R = str(round(ratio_R[i], 2))
            xxratio_R_sig = str(round(ratio_R_sig[i], 2))
        line += xxReff_exp.rjust(sp['Reff_exp']) + pm + xxRerr_exp.ljust(sp['Rerr_exp']) 
        line += xxReff_atom.rjust(sp['Reff_atom']) + pm + xxRerr_atom.ljust(sp['Rerr_atom']) 
        line += xxratio_R.rjust(sp['ratio_R']) 
        line += xxratio_R_sig.rjust(sp['ratio_R_sig']) 

        print line

    print ' ' * 158

