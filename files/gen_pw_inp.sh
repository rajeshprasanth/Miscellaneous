#!/bin/bash
#------------------------------------------------------------------------------------
# Created on Tue Nov  5 05:12:46 IST 2019
# Author :: Rajesh Prashanth Anandavadivel <rajeshprasanth@rediffmail.com>
#------------------------------------------------------------------------------------
#
export relax_direction=$1
export axial_type=$2
export sign=$3
export strain=$4
export v_1_1=$5
export v_1_2=$6
export v_1_3=$7
export v_2_1=$8
export v_2_2=$9
export v_2_3=${10}
export v_3_1=${11}
export v_3_2=${12}
export v_3_3=${13}

cat > Li3Sb.vcrelax.$axial_type.$relax_direction.$sign.$strain.in << EOF
&CONTROL
                       title = 'Li3Sb.vcrelax.$axial_type.$relax_direction.$sign.$strain'
                 calculation = 'vc-relax'
                restart_mode = 'from_scratch'
                      outdir = './Li3Sb.vcrelax.$axial_type.$relax_direction.$sign.$strain'
                  pseudo_dir = '/usr/share/espresso/pseudo/'
                     tstress = .true.
                     tprnfor = .true.
                   verbosity = 'high'
               etot_conv_thr = 1.0D-7
               forc_conv_thr = 1.0D-6
/

&SYSTEM
                       ibrav = 0
                         nat = 3
                        ntyp = 2
                        nbnd = 16
                     ecutwfc = 60
                   nosym_evc = .true.
/

&ELECTRONS
                    conv_thr = 1.0D-9
            diago_cg_maxiter = 5000
            electron_maxstep = 5000
             diagonalization = 'cg'
/

&IONS
                ion_dynamics = 'bfgs'
/

&CELL
                       press = 0.0D0
                 cell_dofree = '$relax_direction'
              press_conv_thr = 0.1D0
                 cell_factor = 3.0D0
/

ATOMIC_SPECIES
Li       6.941 		 Li.pbe-mt_fhi.UPF
Bi 	 208.9804 	 Bi.pbe-mt_fhi.UPF

ATOMIC_POSITIONS {crystal}
  Li      0.50000000000000   0.50000000000000   0.50000000000000  ! // Li 
  Li      0.25000000000000   0.25000000000000   0.25000000000000  ! // Li 
  Li      0.75000000000000   0.75000000000000   0.75000000000000  ! // Li 
  Bi      0.00000000000000   0.00000000000000   0.00000000000000  ! // Sb 
  
CELL_PARAMETERS {angstrom}
   $v_1_1   $v_1_2  $v_1_3
   $v_2_1   $v_2_2  $v_2_3
   $v_3_1   $v_3_2  $v_3_3
    
K_POINTS {automatic}
10 10 10 0 0 0
EOF

cat > Li3Bi.vcrelax.$axial_type.$relax_direction.$sign.$strain.in << EOF
&CONTROL
                       title = 'Li3Bi.vcrelax.$axial_type.$relax_direction.$sign.$strain'
                 calculation = 'vc-relax'
                restart_mode = 'from_scratch'
                      outdir = './Li3Bi.vcrelax.$axial_type.$relax_direction.$sign.$strain'
                  pseudo_dir = '/usr/share/espresso/pseudo/'
                     tstress = .true.
                     tprnfor = .true.
                   verbosity = 'high'
               etot_conv_thr = 1.0D-7
               forc_conv_thr = 1.0D-6
/

&SYSTEM
                       ibrav = 0
                         nat = 3
                        ntyp = 2
                        nbnd = 16
                     ecutwfc = 60
                   nosym_evc = .true.
/

&ELECTRONS
                    conv_thr = 1.0D-9
            diago_cg_maxiter = 5000
            electron_maxstep = 5000
             diagonalization = 'cg'
/

&IONS
                ion_dynamics = 'bfgs'
/

&CELL
                       press = 0.0D0
                 cell_dofree = '$relax_direction'
              press_conv_thr = 0.1D0
                 cell_factor = 3.0D0
/

ATOMIC_SPECIES
Li       6.941 		 Li.pbe-mt_fhi.UPF
Bi 	 208.9804 	 Bi.pbe-mt_fhi.UPF

ATOMIC_POSITIONS {crystal}
  Li      0.50000000000000   0.50000000000000   0.50000000000000  ! // Li 
  Li      0.25000000000000   0.25000000000000   0.25000000000000  ! // Li 
  Li      0.75000000000000   0.75000000000000   0.75000000000000  ! // Li 
  Bi      0.00000000000000   0.00000000000000   0.00000000000000  ! // Sb 
  
CELL_PARAMETERS {angstrom}
   $v_1_1   $v_1_2  $v_1_3
   $v_2_1   $v_2_2  $v_2_3
   $v_3_1   $v_3_2  $v_3_3
    
K_POINTS {automatic}
10 10 10 0 0 0
EOF
