#!/bin/bash
#
# Created on Sun Mar 31 00:50:27 IST 2019
#
#
if [ $# -ne 3 ]; then
  echo "--------------------------------------------------------------------------"
  echo "Usage: generate_strain_files.sh [scp_input] [DFT-functional] [system_name]"
  echo "--------------------------------------------------------------------------"
  exit
fi
#
export scf_input=$1
export func=$2
export sys_name=$3
#
strain_intial="-15"
strain_final="15"
strain_incr="1"
#
export pseudo_dir="/usr/share/espresso/pseudo/"
#

#
export v1_x=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 2p|gawk {'print $1'}|xargs`
export v1_y=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 2p|gawk {'print $2'}|xargs`
export v1_z=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 2p|gawk {'print $3'}|xargs`
#
export v2_x=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 3p|gawk {'print $1'}|xargs`
export v2_y=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 3p|gawk {'print $2'}|xargs`
export v2_z=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 3p|gawk {'print $3'}|xargs`
#
export v3_x=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 4p|gawk {'print $1'}|xargs`
export v3_y=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 4p|gawk {'print $2'}|xargs`
export v3_z=`grep CELL_PARAMETERS -A 3 $scf_input|sed -n 4p|gawk {'print $3'}|xargs`
#
export nat=`grep nat $scf_input|gawk -F= {'print $2'}|xargs`
export ntyp=`grep ntyp $scf_input|gawk -F= {'print $2'}|xargs`
export nbnd=`grep nbnd $scf_input|gawk -F= {'print $2'}|xargs`
export ecutwfc=`grep ecutwfc $scf_input|gawk -F= {'print $2'}|xargs`
#
for strain in $(seq $strain_intial $strain_incr $strain_final);do
for strain_direction in "UNIAXIAL_X" "UNIAXIAL_Y" "UNIAXIAL_Z" "BIAXIAL_XY" "BIAXIAL_XY" "BIAXIAL_XZ";do

printf "Generating $sys_name.$func.$strain_direction.$strain.vcrelax.in"
cat > $sys_name.$func.$strain_direction.$strain.vcrelax.in << EOF
&CONTROL
                       title = '$sys_name.$func.$strain_direction.$strain.vcrelax'
                 calculation = 'vc-relax'
                restart_mode = 'from_scratch'
                      outdir = './$sys_name.$func.$strain_direction.$strain.vcrelax'
                  pseudo_dir = '$pseudo_dir'
                     tstress = .true.
                     tprnfor = .true.
                   verbosity = 'high'
               etot_conv_thr = 1.0D-6
               forc_conv_thr = 1.0D-5
                       nstep = 5000
/

&SYSTEM
                       ibrav = 0
                         nat = $nat
                        ntyp = $ntyp
                        nbnd = $nbnd
                     ecutwfc = $ecutwfc
/

&ELECTRONS
                    conv_thr = 1.0D-8
            diago_cg_maxiter = 5000
            electron_maxstep = 5000
             diagonalization = 'cg'
/

&IONS
                ion_dynamics = 'bfgs'
/

&CELL
                       press = 0.0D0
              press_conv_thr = 0.1D0
                 cell_factor = 3.0
                 cell_dofree = 'AAAAA'
/

$(grep ATOMIC_SPECIES -A $ntyp $scf_input)

$(grep ATOMIC_POSITIONS -A $nat $scf_input)
 
CELL_PARAMETERS {angstrom}
EOF

if [ "$strain_direction" == "UNIAXIAL_X" ];then
  temp1=`bc -l <<< "$strain/100"`
  temp2=`bc -l <<< "$temp1 + 1"`
  v1_x_u=`bc -l <<< "$temp2 * $v1_x"`
  echo $v1_x_u $v1_y $v1_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v2_x $v2_y $v2_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v3_x $v3_y $v3_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  sed -i 's/AAAAA/xy/g' $sys_name.$func.$strain_direction.$strain.vcrelax.in
fi


if [ "$strain_direction" == "UNIAXIAL_Y" ];then
  temp1=`bc -l <<< "$strain/100"`
  temp2=`bc -l <<< "$temp1 + 1"`
  v2_y_u=`bc -l <<< "$temp2 * $v2_y"`
  echo $v1_x $v1_y $v1_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v2_x $v2_y $v2_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v3_x $v3_y $v3_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  sed -i 's/AAAAA/yz/g' $sys_name.$func.$strain_direction.$strain.vcrelax.in
fi


if [ "$strain_direction" == "UNIAXIAL_Z" ];then
  temp1=`bc -l <<< "$strain/100"`
  temp2=`bc -l <<< "$temp1 + 1"`
  v3_z_u=`bc -l <<< "$temp2 * $v3_z"`
  echo $v1_x $v1_y $v1_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v2_x $v2_y $v2_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v3_x $v3_y $v3_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  sed -i 's/AAAAA/xz/g' $sys_name.$func.$strain_direction.$strain.vcrelax.in
fi


if [ "$strain_direction" == "BIAXIAL_XY" ];then
  temp1=`bc -l <<< "$strain/100"`
  temp2=`bc -l <<< "$temp1 + 1"`
  v1_x_u=`bc -l <<< "$temp2 * $v1_x"`
  v2_y_u=`bc -l <<< "$temp2 * $v2_y"`
  echo $v1_x_u $v1_y $v1_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v2_x $v2_y_u $v2_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v3_x $v3_y $v3_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  sed -i 's/AAAAA/z/g' $sys_name.$func.$strain_direction.$strain.vcrelax.in
fi


if [ "$strain_direction" == "BIAXIAL_YZ" ];then
  temp1=`bc -l <<< "$strain/100"`
  temp2=`bc -l <<< "$temp1 + 1"`
  v2_y_u=`bc -l <<< "$temp2 * $v2_y"`
  v3_z_u=`bc -l <<< "$temp2 * $v3_z"`
  echo $v1_x $v1_y $v1_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v2_x $v2_y_u $v2_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v3_x $v3_y $v3_z_u >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  sed -i 's/AAAAA/x/g' $sys_name.$func.$strain_direction.$strain.vcrelax.in
fi


if [ "$strain_direction" == "BIAXIAL_XZ" ];then
  temp1=`bc -l <<< "$strain/100"`
  temp2=`bc -l <<< "$temp1 + 1"`
  v1_x_u=`bc -l <<< "$temp2 * $v1_x"`
  v3_z_u=`bc -l <<< "$temp2 * $v3_z"`
  echo $v1_x_u $v1_y $v1_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v2_x $v2_y $v2_z >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  echo $v3_x $v3_y $v3_z_u >> $sys_name.$func.$strain_direction.$strain.vcrelax.in
  sed -i 's/AAAAA/y/g' $sys_name.$func.$strain_direction.$strain.vcrelax.in
fi



grep K_POINTS -A 1 $scf_input >> $sys_name.$func.$strain_direction.$strain.vcrelax.in

printf ".... Done\n"
done
done