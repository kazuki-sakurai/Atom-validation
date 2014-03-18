#!/bin/bash
wkdir=`pwd`
source /Users/sakurai/atom/Atom-target/bin/atomenv.sh
ana=ATLAS_2013_CONF_2013_024; vname=stopL; fname=GttN1_GttN1_1E2.hepmc

######################################################

#atom --list-analyses
event_path=$wkdir/../Validation-events/$ana

cd $wkdir/Analyses/$ana
atom -a $ana $event_path/$fname 

######################################################
cd $wkdir
