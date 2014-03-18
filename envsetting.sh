#!/bin/bash

export nixpkgs_path=$HOME/atom/src/nixpkgs
export atom_path=$HOME/atom/Atom-target

get_names ()
{
    ana=$1
    vname=()
    fname=()
    if [[ $ana == "ATLAS_2013_CONF_2013_024" ]]; then

        vname_list+=("stopR")
        fname_list+=("GttN1_GttN1_1E2.hepmc")

        vname_list+=("stopL")
        fname_list+=("GttN1_GttN1_1E2.hepmc")

    fi
}
