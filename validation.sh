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

source ./setting.sh

if [[ ! -d $valdir/../Validation-events ]]; then
    echo $valdir/../Validation-events' will be created. OK?'  
    echo '[y]/[n]'
    read flag
    if [[ $flag == 'y' ]]; then
        mkdir $valdir/../Validation-events
    else
        echo 'Abort'; exit 
    fi 
fi

for ana in ${alist[@]}; do

    echo $ana
    unset vname_list; unset fname_list

    get_names $ana

    #for ((i=0; i < ${#fname_list[@]}; i++)); do    
    #    echo ${vname_list[$i]}, ${fname_list[$i]}
    #done

    for ((i=0; i < ${#fname_list[@]}; i++)); do    
        vname=${vname_list[$i]}
        fname=${fname_list[$i]}

        echo $vname, $fname

        if [[ ! -d $valdir/../Validation-events/$ana ]]; then
            mkdir $valdir/../Validation-events/$ana
        fi

        while [[ ! -f $valdir/../Validation-events/$ana/$fname ]]; do
            echo $ana/$fname does not exist.
            echo 'Download from the server? [y]/[n]'
            read answer
            if [[ $answer == 'y' ]]; then
                cd $valdir/../Validation-events/$ana
                linkhead='atom@lxplus.cern.ch:www/Validation-events'
                scp $linkhead'/'$ana'/'$fname.gz ./temp.gz && mv temp.gz $fname.gz && gunzip -f $fname.gz
                cd $valdir
            else                
                break
            fi
        done

        script=$valdir/Analyses/$ana/script.sh
        sed -e "s|ATOM_PATH|$atom_path|g" job.sh | sed -e "s|ANA|$ana|g" | sed -e "s|VNAME|$vname|g" | sed -e "s|FNAME|$fname|g" > $script
        chmod 755 $script
        #nix-shell $nixpkgs_path -A hepNixOverlay.dev.AtomDev --command $script

        source $script

        cd $valdir/Analyses/$ana
        if [[ ! -d backup ]]; then
            mkdir backup
        fi
        if [[ -f $vname.tex ]]; then
            mv $vname.tex backup/            
            mv $vname.out backup/            
        fi        
        ./$vname.py $vname.root | tee $vname.out
        #pdflatex $vname.tex
        cd $valdir

    done    
done

#sh write_table.sh
