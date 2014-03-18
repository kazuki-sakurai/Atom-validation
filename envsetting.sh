#!/bin/bash

###########################################################

export nixpkgs_path=$HOME/atom/src/nixpkgs
export atom_path=$HOME/atom/Atom-target

###########################################################

get_names ()
{
    ana=$1
    vname=()
    fname=()
    if [[ $ana == "ATLAS_2013_CONF_2013_024" ]]; then

        vname_list+=("stopL")
        fname_list+=($ana"/V024_LHC8_T1tN1_100left_600-1.hepmc")

        vname_list+=("stopR")
        fname_list+=($ana"/V024_LHC8_T1tN1_95right_600-1.hepmc")

    fi
}
