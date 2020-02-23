#!/bin/bash
#
# Created on Sun Jun  2 01:46:19 IST 2019
#
#
IN_POSCAR=$1
export IN_POSCAR
#
read -r -a element <<< $(sed -n 6p $IN_POSCAR)
read -r -a elementnum <<< $(sed -n 7p $IN_POSCAR)
var=""
for str in $(seq 0 $(echo "${#element[@]}-1"|bc)) ;do
	var+="${element[$str]}${elementnum[$str]}" 
done
mv $IN_POSCAR $var.$IN_POSCAR
