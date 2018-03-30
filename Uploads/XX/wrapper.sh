#!/bin/bash


PBE_PSEUDO_1="Si.pbe-mt_fhi.UPF"
PBE_PSEUDO_2="Ge.pbe-mt_fhi.UPF"
PBE_PSEUDO_3="Sn.pbe-mt_fhi.UPF"
PW_PSEUDO_1="Si.pw-mt_fhi.UPF"
PW_PSEUDO_2="Ge.pw-mt_fhi.UPF"
PW_PSEUDO_3="Sn.pw-mt_fhi.UPF"

NETWORK_PSEUDO="http://www.quantum-espresso.org/wp-content/uploads/upf_files/"
LOCAL_PSEUDO="/home/rajeshprashanth/pseudo"

wget $NETWORK_PSEUDO/$PBE_PSEUDO_1 
wget $NETWORK_PSEUDO/$PBE_PSEUDO_2 
wget $NETWORK_PSEUDO/$PBE_PSEUDO_3 
wget $NETWORK_PSEUDO/$PW_PSEUDO_1
wget $NETWORK_PSEUDO/$PW_PSEUDO_2 
wget $NETWORK_PSEUDO/$PBE_PSEUDO_3 

mv *UPF $LOCAL_PSEUDO

pw.x < Sn4Ge4-site1-pbe.in > Sn4Ge4-site1-pbe.out
pw.x < Sn4Ge4-site2-pbe.in > Sn4Ge4-site2-pbe.out
pw.x < Sn4Ge4-site3-pbe.in > Sn4Ge4-site3-pbe.out
pw.x < Sn4Ge4-site4-pbe.in > Sn4Ge4-site4-pbe.out
pw.x < Sn4Ge4-site1-pw.in > Sn4Ge4-site1-pw.out
pw.x < Sn4Ge4-site2-pw.in > Sn4Ge4-site2-pw.out
pw.x < Sn4Ge4-site3-pw.in > Sn4Ge4-site3-pw.out
pw.x < Sn4Ge4-site4-pw.in > Sn4Ge4-site4-pw.out

grep ! *out

mail -s ":::Quantum-Espresso job Completed on $HOSTNAME:::" rajeshprasanth@rediffmail.com < temp
