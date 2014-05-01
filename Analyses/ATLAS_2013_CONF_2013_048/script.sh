#!/bin/bash
wkdir=`pwd`
source /Users/sakurai/atom/Atom-target/bin/atomenv.sh
ana=ATLAS_2013_CONF_2013_048; vname=same_and_opposite_flavour; fname=T1bC1wN1_400-250-1_5E4.hepmc

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
