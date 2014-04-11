#! /usr/bin/env python

__author__ = "Kazuki Sakurai <kazuki.sakurai@kcl.ac.uk>"
__version__ = "0.1"

import ROOT
import sys
import os


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


