#!/bin/bash
wkdir=`pwd`
source ATOM_PATH/bin/atomenv.sh
ana=ANA; vname=VNAME; fname=FNAME

######################################################

#atom --list-analyses
event_path=$wkdir/../Validation-events/$ana

cd $wkdir/Analyses/$ana
atom -a $ana $event_path/$fname 

######################################################
cd $wkdir