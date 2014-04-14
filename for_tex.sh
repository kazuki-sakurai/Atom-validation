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

source setting.sh

for ana in ${alist[@]}; do

    echo 'ananame  ' $ana
    unset vname_list; unset fname_list

    get_names $ana

    for ((i=0; i < ${#fname_list[@]}; i++)); do    
        vname=${vname_list[$i]}
        echo 'vname  ' $vname
    done
done

