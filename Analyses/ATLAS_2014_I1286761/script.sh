#!/bin/bash
wkdir=`pwd`
source /Users/sakurai/atom/Atom-target/bin/atomenv.sh
ana=ATLAS_2014_I1286761; vname=Zjets_350; fname=C1wN1-N2zN1_350-50_2E4.hepmc

######################################################

#atom --list-analyses
event_path=$wkdir/../Validation-events/$ana

cd $wkdir/Analyses/$ana
if [[ ! -d backup ]]; then
    mkdir backup
fi
mv $vname.root backup/
atom -a $ana $event_path/$fname && mv atom.yoda.root $vname.root #&& mv atom.yoda.yoda $vname.yoda

######################################################
cd $wkdir
