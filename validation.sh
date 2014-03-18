#!/bin/bash

valdir=`pwd`

if [[ -f $1 ]]; then
    while read line; do 
        firstletter=`echo $line | cut -c1`
        if [[ $firstletter != "#" ]]; then 
            alist0+=($line)
        fi
    done < $1    
else
    alist0=($@)
fi

for ana in ${alist0[@]}; do
    if [[ -d $valdir/Analyses/$ana ]]; then
        alist+=($ana)
    else
        echo "#----------------------------------------------------------#"
        echo "ERROR!!!"
        echo "$ana does not exist."
        echo "#----------------------------------------------------------#"        
    fi
done 

source envsetting.sh

for ana in ${alist[@]}; do

    get_names $ana
    for ((i=0; i < ${#fname_list[@]}; i++)); do    
        vname=${vname_list[$i]}
        fname=${fname_list[$i]}

        if [[ ! -f $valdir/../Validation-events/$ana/$fname ]]; then
            echo $ana/$fname does not exist.
            echo Download from the server.
            cd $valdir/../Validation-events/$ana
            linkhead='atom@lxplus.cern.ch:www/Validation-events/'
            scp $linkhead$fname.gz .
            gunzip $fname.gz
            cd $valdir
        fi

        script=$valdir/Analyses/$ana/script.sh
        sed -e "s|ATOM_PATH|$atom_path|g" job.sh | sed -e "s|ANA|$ana|g" | sed -e "s|VNAME|$vname|g" | sed -e "s|FNAME|$fname|g" > $script
        chmod 755 $script
        nix-shell $nixpkgs_path -A hepNixOverlay.dev.AtomDev --command $script

    done    
done


