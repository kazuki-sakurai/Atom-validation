#!/bin/bash
wkdir=`pwd`
source ATOM_PATH/bin/atomenv.sh
ana=ANA; vname=VNAME; fname=FNAME

######################################################

#atom --list-analyses
event_path=$wkdir/../Validation-events/$ana

cd $wkdir/Analyses/$ana
if [[ ! -d backup ]]; then
    mkdir backup
fi
mv $vname.root backup/
atom -a $ana $event_path/$fname -H $vname 

######################################################
cd $wkdir