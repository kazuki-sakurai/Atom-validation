#!/bin/bash
wkdir=`pwd`
source /Users/sakurai/atom/Atom-target/bin/atomenv.sh
ana=ATLAS_2014_I1286761; vname=Zjets_250; fname=C1wN1-N2zN1_250-0_2E4.hepmc

######################################################

#atom --list-analyses
event_path=$wkdir/../Validation-events/$ana

cd $wkdir/Analyses/$ana
atom -a $ana $event_path/$fname && mv atom.yoda.root $vname.root #&& mv atom.yoda.yoda $vname.yoda

######################################################
cd $wkdir
