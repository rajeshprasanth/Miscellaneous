#!/bin/bash
#
#
for pressure in 0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
do

cat > 9013925.pz.$pressure.vcrelax.in << EOF
&CONTROL
                   title = '9013925'
             calculation = 'vc-relax'
            restart_mode = 'from_scratch'
                  outdir = './output'
              pseudo_dir = '/var/lib/rundeck/pseudo'
                 tstress = .true.
                 tprnfor = .true.
           etot_conv_thr = 1.0D-10
           forc_conv_thr = 1.0D-8
/
&SYSTEM
                   ibrav = 0
                       A = 5.42020
                     nat = 2
                    ntyp = 2
		 ecutwfc = 80
             occupations = 'smearing'
                smearing = 'm-v'
                 degauss = 0.022
/
&ELECTRONS
                conv_thr = 1.0D-10
        diago_cg_maxiter = 5000
         diagonalization = 'cg'
/
&IONS
            ion_dynamics = 'bfgs'
/
&CELL
                   press = $pressure
             cell_factor = 3.0
          press_conv_thr = 0.1D0
/

ATOMIC_SPECIES
  Cu   63.54600  Cu.pz-hgh.UPF
  Cl   35.45150  Cl.pz-hgh.UPF

ATOMIC_POSITIONS {crystal}
Cu   0.000000000000000   0.000000000000000   0.000000000000000 
Cl   0.250000000000000   0.250000000000000   0.250000000000000 

CELL_PARAMETERS {alat}
  0.500000000000000   0.500000000000000   0.000000000000000 
  0.500000000000000   0.000000000000000   0.500000000000000 
  0.000000000000000   0.500000000000000   0.500000000000000 

K_POINTS automatic
10 10 10  0 0 0
EOF
done

for pressure in 0 5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
do

cat > 9013925.pbe.$pressure.vcrelax.in << EOF
&CONTROL
                   title = '9013925'
             calculation = 'vc-relax'
            restart_mode = 'from_scratch'
                  outdir = './output'
              pseudo_dir = '/var/lib/rundeck/pseudo'
                 tstress = .true.
                 tprnfor = .true.
           etot_conv_thr = 1.0D-10
           forc_conv_thr = 1.0D-8
/
&SYSTEM
                   ibrav = 0
                       A = 5.42020
                     nat = 2
                    ntyp = 2
		 ecutwfc = 80
             occupations = 'smearing'
                smearing = 'm-v'
                 degauss = 0.022
/
&ELECTRONS
                conv_thr = 1.0D-10
        diago_cg_maxiter = 5000
         diagonalization = 'cg'
/
&IONS
            ion_dynamics = 'bfgs'
/
&CELL
                   press = $pressure
             cell_factor = 3.0
          press_conv_thr = 0.1D0
/

ATOMIC_SPECIES
  Cu   63.54600  Cu.pbe-mt_fhi.UPF
  Cl   35.45150  Cl.pbe-mt_fhi.UPF

ATOMIC_POSITIONS {crystal}
Cu   0.000000000000000   0.000000000000000   0.000000000000000 
Cl   0.250000000000000   0.250000000000000   0.250000000000000 

CELL_PARAMETERS {alat}
  0.500000000000000   0.500000000000000   0.000000000000000 
  0.500000000000000   0.000000000000000   0.500000000000000 
  0.000000000000000   0.500000000000000   0.500000000000000 

K_POINTS automatic
10 10 10  0 0 0
EOF
done


