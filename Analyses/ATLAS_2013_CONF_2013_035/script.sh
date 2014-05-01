#!/bin/bash
wkdir=`pwd`
source /Users/sakurai/atom/Atom-target/bin/atomenv.sh
ana=ATLAS_2013_CONF_2013_035; vname=Zc; fname=C1wN1-N2zN1_250-0_5E3.hepmc

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
