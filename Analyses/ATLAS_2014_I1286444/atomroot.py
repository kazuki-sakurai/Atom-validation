#! /usr/bin/env python

"""
    Reads the Atom.root file and extracts the Efficiencies and Cuts.
    Passes everything to a AtomResult object with has some associated
    methods to get to interesting subsets of the result.
"""

__author__ = "Andreas Weiler <andreas.weiler@desy.de>"
__version__ = "0.1"

import ROOT
import sys
import os

FINALSTATE=True

def prettyprint(matrix):
    s = [[str(e).split('\x00')[0]  for e in row] for row in matrix]
    lens = [len(max(col, key=len)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print '\n'.join(table)

def prettyprint2file(matrix, filename):
    s = [[str(e).split('\x00')[0] for e in row] for row in matrix]
    lens = [len(max(col, key=len)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    # print '\n'.join(table)
    ffile = open(filename, 'w')
    ffile.write('\n'.join(table))
    ffile.close()


class AtomResult:
    """
    Allows to extract information in python friendly form
    from the ATOM-root output
    """
    def __init__(self, resultEff, resultCut, resultSub):
        print "New ATOM result with", len(resultEff), "entries."
        self.Efficiencies = resultEff
        self.Cuts = resultCut
        self.SubProcesses = resultSub
        pass

    def getAnalysis(self, ananameIn, procidIn):
        for ananame, effname, procid, effvalue, efferror in self.Efficiencies:
            if procid == procidIn and ananame == ananameIn:
                print ananame, effname, procid, effvalue, efferror

# Efficiency methods

    def getEfficiency(self, ananameIn, effnameIn):
        for ananame, effname, procid, effvalue, efferror in self.Efficiencies:
            if procid == 0 and ananame == ananameIn and effnameIn == effname:
                return effvalue

    def listSignalRegions(self, ananameIn):
        returnlist = []
        for ananame, effname, procid, effvalue, efferror in self.Efficiencies:
            if procid == 0 and ananame == ananameIn and effname.find("CR") == -1:
                returnlist.append(effname)
        return returnlist

    def listAnalyses(self):
        returnlist = []
        firstrun = True
        ananameold = ""
        for ananame, effname, procid, effvalue, efferror in self.Efficiencies:
            if firstrun:
                ananameold = ananame
                returnlist.append(ananame)
                firstrun = False
            if ananame != ananameold:
                returnlist.append(ananame)
                ananameold = ananame
        return returnlist

    def listControlRegions(self, ananameIn):
        returnlist = []
        for ananame, effname, procid, effvalue, efferror in self.Efficiencies:
            if procid == 0 and ananame == ananameIn and effname.find("CR") > -1:
                returnlist.append(effname)
        return returnlist

    def printEfficiencies(self,ananameIn):
        _returnlist = []
        _returnlist.append(["Name", "Value", "Error"])
        for ananame, effname, procid, effvalue, efferror in self.Efficiencies:
            if procid == 0 and ananame == ananameIn and effname.find("CR") == -1:
                _returnlist.append([effname, effvalue, efferror])
        prettyprint(_returnlist)

    def printAllEfficiencies(self,ananameIn, CR = False):
        _returnlist = []
        _returnlist.append(["Name", "Value", "Error"])
        for ananame, effname, procid, effvalue, efferror in self.Efficiencies:
            if ananame == ananameIn and effname.find("CR") == -1:
                _returnlist.append([effname, procid, effvalue, efferror])
        prettyprint(_returnlist)

# Cut methods

    def getCut(self, ananameIn, cutnameIn):
        for ananame, cutname, description, idx, parent_idx,value, error, logderiv_value,logderiv_error in self.Cuts:
            if ananame == ananameIn and cutnameIn == cutname:
                return value
    def listCuts(self, ananameIn):
        returnlist = []
        for ananame, cutname, description, idx, parent_idx,value, error, logderiv_value,logderiv_error in self.Cuts:
            if ananame == ananameIn:
                returnlist.append(cutname)
        return returnlist

    def printCuts(self,ananameIn):
        _returnlist = []
        _returnlist.append(["idx", "cutname", "value", "error", "dlogeff/dlogcut"])
        for ananame, cutname, description, idx, parent_idx,value, error, logderiv_value,logderiv_error in self.Cuts:
            if ananame == ananameIn:
                    _returnlist.append([idx, cutname, value, error, logderiv_value])
        prettyprint(_returnlist)


    def efficiencies_in_order(self, ananameIn, eff_atlas, CR = False):
        _returnlist = []
        _returnlist.append(["Name", "Value", "Error"])
        eff_list = {}

        effname_list = []
        atlas_vals = []
        for elem in eff_atlas:
            if isinstance(elem, str): 
                effname_list.append(elem)
            else:
                atlas_vals.append(elem)

        for effname_elem in effname_list:
            for ananame, effname, procid, effvalue, efferror in self.Efficiencies:
                realname = str(effname).split('\x00')[0]
                if procid == 0 and ananame == ananameIn and effname.find("CR") == -1 and effname_elem == realname:
                    eff_list[effname_elem] = effvalue

        #for i in range(len(effname_list)):
        #    print i, effname_list[i]
        #print ""        

        print "Name:"                
        print "{",
        for i in range(len(effname_list)):
            strout = str( '"' + effname_list[i] + '"') + ","
            if i == len(effname_list) - 1: 
                strout = str('"' + effname_list[i] + '"')
            print strout,
        print "}"        

        print "atom:"        
        print "{",
        for i in range(len(effname_list)):
            strout = str(eff_list[effname_list[i]]) + ","
            if i == len(effname_list) - 1: strout = str(eff_list[effname_list[i]])
            print strout,
        print "}"        

        print "ATLAS:"
        print "{",
        for i in range(len(effname_list)):
            strout = str(atlas_vals[i]) + ","
            if i == len(effname_list) - 1: strout = str(atlas_vals[i])
            print strout,
        print "}"        



def ReadROOTfile(filename):


    f = ROOT.TFile(filename)

    resulteff = []

    entr = ROOT.Efficiencies.GetEntries()
    ROOT.Efficiencies.GetEntry(0)

    i=0
    for jentry in xrange(entr):
        ananame = ROOT.Efficiencies.analysis
        effname = ROOT.Efficiencies.name
        procid = ROOT.Efficiencies.procid
        effvalue = ROOT.Efficiencies.value
        efferror = ROOT.Efficiencies.error
        resulteff.append([ananame, effname, procid, effvalue, efferror])
        i += 1
        ROOT.Efficiencies.GetEntry(i)

    entr = ROOT.Cuts.GetEntries()
    ROOT.Cuts.GetEntry(0)

    resultscut = []
    i=0
    for jentry in xrange(entr):
        ananame = ROOT.Cuts.analysis
        cutname = ROOT.Cuts.name
        description = ROOT.Cuts.description
        idx = ROOT.Cuts.idx
        parent_idx = ROOT.Cuts.parent_idx
        value = ROOT.Cuts.value
        error = ROOT.Cuts.error
        logderiv_value = ROOT.Cuts.logderiv_value
        logderiv_error = ROOT.Cuts.logderiv_error
        resultscut.append([ananame, cutname, description, idx, parent_idx, value, error, logderiv_value,logderiv_error ])
        i += 1
        ROOT.Cuts.GetEntry(i)

    i=0
    entr = ROOT.SubProcesses.GetEntries()
    ROOT.SubProcesses.GetEntry(0)

    resultssubprocesses = []

    for jentry in xrange(entr):
        procid = ROOT.SubProcesses.procid
        particles = ROOT.SubProcesses.particles
        resultssubprocesses.append([procid, particles])
        i += 1
        ROOT.SubProcesses.GetEntry(i)

    if FINALSTATE:
        print "Writing final states ... "
        resultsfinalstate = []
        i=0
        entr = ROOT.FinalStates.GetEntries()
        ROOT.FinalStates.GetEntry(0)

        for jentry in xrange(entr):
            event_num = ROOT.FinalStates.event_num
            analysis = ROOT.FinalStates.analysis
            name = ROOT.FinalStates.name
            barcode = ROOT.FinalStates.barcode
            pdgcode = ROOT.FinalStates.pdgcode
            label = ROOT.FinalStates.label
            px = ROOT.FinalStates.px
            py = ROOT.FinalStates.py
            pz = ROOT.FinalStates.pz
            E = ROOT.FinalStates.E
            m = ROOT.FinalStates.m
            resultsfinalstate.append([event_num, analysis, name, barcode, pdgcode, label, px, py, pz, E, m])
            i += 1
            ROOT.FinalStates.GetEntry(i)

        #prettyprint2file(resultsfinalstate,filename+'.atomreco')
        #print "Wrote " + str(event_num) + " events."
    atomout = AtomResult(resulteff, resultscut, resultssubprocesses)
    return atomout



##### main

def main():

    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

    import sys

    if len(sys.argv) > 1:
        filename = sys.argv[1]

    atomout = ReadROOTfile(filename)

    for anaNAME in atomout.listAnalyses():
        print "\n", anaNAME
        atomout.printCuts(anaNAME)
        print "\n"
        atomout.printEfficiencies(anaNAME)
        print "\n\n"

        print "### 130, 0 ###"
        eff_atlas = [
                    "MET > 50",                       3256.49,                                                
                    ">= 2 central jets",              2304.39,                    
                    "2 leading jets central",         2170.64,
                    "4th leading jet veto (pT > 25)", 1891.79,
                    "baseline lepton veto",           1860.44, 
                    "mjj > 50",                       1765.78,                    
                    "mT > 40",                        1461.14,                    
                    "mCT > 160",                      176.80,                    
                    "MET > 100",                      140.10,                    
                    "exactly 2 leading bjets",        45.62,                    
                    "SRA: 100 < mT < 130",            8.72,                    
                    "SRB: mT > 130",                  0.35                    
                    ]
        atomout.efficiencies_in_order(anaNAME, eff_atlas)

        print "### 225, 0 ###"
        eff_atlas = [
                    "MET > 50",                       600.45,                                                
                    ">= 2 central jets",              458.03,                    
                    "2 leading jets central",         439.07,
                    "4th leading jet veto (pT > 25)", 369.43,
                    "baseline lepton veto",           363.35, 
                    "mjj > 50",                       345.63,                    
                    "mT > 40",                        305.45,                    
                    "mCT > 160",                      52.48,                    
                    "MET > 100",                      45.48,                    
                    "exactly 2 leading bjets",        13.93,                    
                    "SRA: 100 < mT < 130",            2.55,                    
                    "SRB: mT > 130",                  5.68                    
                    ]
        atomout.efficiencies_in_order(anaNAME, eff_atlas)

    return atomout

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    atomout = main()

