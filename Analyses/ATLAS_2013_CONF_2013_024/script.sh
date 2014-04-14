#!/bin/bash
wkdir=`pwd`
source /Users/sakurai/atom/Atom-target/bin/atomenv.sh
ana=ATLAS_2013_CONF_2013_024; vname=stopR; fname=V024_LHC8_T1tN1_95right_600-1.hepmc

######################################################

#atom --list-analyses
event_path=$wkdir/../Validation-events/$ana

cd $wkdir/Analyses/$ana
atom -a $ana $event_path/$fname && mv atom.yoda.root $vname.root #&& mv atom.yoda.yoda $vname.yoda

######################################################
cd $wkdir
