#!/bin/bash

###########################################################

export nixpkgs_path=$HOME/atom/src/nixpkgs
export atom_path=$HOME/atom/Atom-target

###########################################################

get_names ()
{
    ana=$1
    unset vname; vname=()
    unset fname; fname=()

    if [[ $ana == "ATLAS_2014_I1286761" ]]; then

        #vname_list+=("EN1_191")
        #fname_list+=("EeN1_191-90_2E3.hepmc")

        #vname_list+=("MN1_191")
        #fname_list+=("MmN1_191-90_2E3.hepmc")

        #vname_list+=("EN1_250")
        #fname_list+=("EeN1_250-10_2E3.hepmc")

        #vname_list+=("MN1_250")
        #fname_list+=("MmN1_250-10_2E3.hepmc")

        #vname_list+=("C1LN1_350")
        #fname_list+=("C1lLlN1_350-175-0_1E4.hepmc")

        #vname_list+=("C1LN1_425")
        #fname_list+=("C1lLlN1_425-250-75_1E4.hepmc")

        #vname_list+=("WWa")
        #fname_list+=("C1wN1_100-0_5E4.hepmc")

        vname_list+=("WWb")
        fname_list+=("C1wN1_140-20_5E4.hepmc")

        #vname_list+=("WWc")
        #fname_list+=("C1wN1_200-0_5E4.hepmc")

        #vname_list+=("Zjets_250")
        #fname_list+=("C1wN1-N2zN1_250-0_5E4.hepmc")

        #vname_list+=("Zjets_350")
        #fname_list+=("C1wN1-N2zN1_350-50_5E4.hepmc")

    fi


    if [[ $ana == "ATLAS_2014_I1286444" ]]; then

        vname_list+=("H160_T1bC1wN1_300-150-50")
        fname_list+=("T1bC1wN1_300-150-50_N10000.hepmc")

        vname_list+=("H160_T1bC1wN1_250-106-60")
        fname_list+=("T1bC1wN1_250-106-60_N10000.hepmc")

        vname_list+=("L_T1bC1wN1_300-150-1")
        fname_list+=("T1bC1wN1_300-150-1_N10000.hepmc")

        vname_list+=("L_T1bC1wN1_400-390-195")
        fname_list+=("T1bC1wN1_400-390-195_N20000.hepmc")

    fi


    if [[ $ana == "ATLAS_2013_CONF_2013_024" ]]; then

        vname_list+=("stopL")
        fname_list+=("V024_LHC8_T1tN1_100left_600-1.hepmc")

        vname_list+=("stopR")
        fname_list+=("V024_LHC8_T1tN1_95right_600-1.hepmc")
    fi

    ############################################################

    if [[ $ana == "ATLAS_2013_CONF_2013_035" ]]; then

        vname_list+=("noZa")
        fname_list+=("C1-L-N1_192.5-175-157.5_1E3.hepmc")

        vname_list+=("noZb")
        fname_list+=("C1wN1-N2zN1_150-75_1E4.hepmc")

        vname_list+=("noZc")
        fname_list+=("C1-L-N1_500-250-0_5E3.hepmc")

        vname_list+=("Za")
        fname_list+=("C1wN1-N2zN1_100-0_2E4.hepmc")

        vname_list+=("Zb")
        fname_list+=("C1wN1-N2zN1_150-0_3E4.hepmc")

        vname_list+=("Zc")
        fname_list+=("C1wN1-N2zN1_250-0_5E3.hepmc")

    fi

    ############################################################

    if [[ $ana == "ATLAS_2013_CONF_2013_037" ]]; then

        vname_list+=("mT1-mN1_500-200")
        fname_list+=("V037_70right_LHC8_T1tN1_500-200.hepmc")

        vname_list+=("mT1-mN1_650-1")
        fname_list+=("V037_70right_LHC8_T1tN1_650-1.hepmc")

    fi

    ############################################################

    if [[ $ana == "ATLAS_2013_CONF_2013_047" ]]; then

        vname_list+=("QQdirect_450-400")
        fname_list+=("QQj_450-400_1E4.hepmc")

        vname_list+=("QQdirect_850-100")
        fname_list+=("QQ_850-100_5E3.hepmc")

        vname_list+=("QQdirect_662-287")
        fname_list+=("QQj_662-287_1E4.hepmc")

        vname_list+=("GQdirect_1425-525")
        fname_list+=("GQ_1425-525_5E3.hepmc")

        vname_list+=("GQdirect_1612-37")
        fname_list+=("GQ_1612-37_5E3.hepmc")

        vname_list+=("GGdirect_1162-337")
        fname_list+=("GG_1162-337_5E3.hepmc")

        vname_list+=("GG1step_1065")
        fname_list+=("GC1N1_1065-785-505_2E4.hepmc")

        vname_list+=("GG1step_1265")
        fname_list+=("GC1N1_1265-865-465_2E4.hepmc")

    fi

    ############################################################

    if [[ $ana == "ATLAS_2013_CONF_2013_048" ]]; then

        vname_list+=("same_and_opposite_flavour")
        fname_list+=("T1bC1wN1_400-250-1_5E4.hepmc")

    fi

    ############################################################

    if [[ $ana == "ATLAS_2013_CONF_2013_049" ]]; then

        #vname_list+=("EN1_191")
        #fname_list+=("EeN1_191-90_2E3.hepmc")

        #name_list+=("MN1_191")
        #fname_list+=("MmN1_191-90_2E3.hepmc")

        #vname_list+=("EN1_250")
        #fname_list+=("EeN1_250-10_2E3.hepmc")

        #vname_list+=("MN1_250")
        #fname_list+=("MmN1_250-10_2E3.hepmc")

        #vname_list+=("C1LN1_350")
        #fname_list+=("C1lLlN1_350-175-0_1E4.hepmc")

        #vname_list+=("C1LN1_425")
        #fname_list+=("C1lLlN1_425-250-75_1E4.hepmc")

        #vname_list+=("WWa")
        #fname_list+=("C1wN1_100-0_5E4.hepmc")

        vname_list+=("WWb")
        fname_list+=("C1wN1_140-20_5E4.hepmc")

        #vname_list+=("WWc")
        #fname_list+=("C1wN1_200-0_5E4.hepmc")

    fi

    ############################################################

    if [[ $ana == "ATLAS_2013_CONF_2013_061" ]]; then

        vname_list+=("GbbN1_0L4J")
        fname_list+=("GbbN1_1300-100.hepmc")

        vname_list+=("GttN1_0L7J")
        fname_list+=("LHC8_GttN1.hepmc")

        vname_list+=("GttN1_1L6J")
        fname_list+=("LHC8_GttN1.hepmc")

    fi

    ############################################################

    if [[ $ana == "ATLAS_2013_CONF_2013_093" ]]; then

        vname_list+=("C1wN1N2hN1_130")
        fname_list+=("C1wN1-N2hN1_130-0_5E4.hepmc")

        vname_list+=("C1wN1N2hN1_225")
        fname_list+=("C1wN1-N2hN1_225-0_5E4.hepmc")

    fi

}
