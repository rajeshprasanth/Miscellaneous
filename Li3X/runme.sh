#!/bin/bash
#
#

for sys in $(seq 7)
do
mkdir comp_$sys
cp SGO comp_$sys
cd comp_$sys
cat > INSOD <<EOF
#Title
Bi doped Li3Sb

# a,b,c,alpha,beta,gamma
6.5617540000 6.5617540000 6.5617540000 90.000 90.000 90.000

# nsp: Number of species
2

# symbol(1:nsp): Atom symbols
Li Sb

# natsp0(1:nsp): Number of atoms for each species in the assymetric unit 
2 1 

# coords0(1:nat0,1:3): Coordinates of each atom (one line per atom)
0.25000000000000   0.25000000000000   0.25000000000000
0.50000000000000   0.50000000000000   0.50000000000000
0.00000000000000   0.00000000000000   0.00000000000000

# na,nb,nc (supercell definition)
2 1 1

# sptarget: Species to be substituted
2

# nsubs: Number of substitutions in the supercell
$sys

# newsymbol(1:2): Symbol of atom to be inserted in the selected position, 
#                 symbol to be inserted in the rest of the positions for the same species.
Bi Sb 

# FILER, MAPPER
# # FILER:   0 (no calc files generated), 1 (GULP), 2 (METADISE), 11 (VASP)
# # MAPPER:  0 (no mapping, use currect structure), >0 (map to structure in MAPTO file)
# # (each position in old structure is mapped to MAPPER positions in new structure)
11 0

# This section is not read if VASP files are being created
# If FILER=1 then: 
# ishell(1:nsp) 0 core only / 1 core and shell (for the species listed in symbol(1:nsp)) 
0 1
# newshell(1:2) 0 core only / 1 core and shell (for the species listed in newsymbol(1:2))
0 0
EOF
sod_comb.sh
cd ..
done
