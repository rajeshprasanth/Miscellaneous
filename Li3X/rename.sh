#!/bin/bash
#
# Created on Sun Jun  2 01:46:19 IST 2019
#
#
rm -rf comp_* log POSCARS
export PATH=$PATH:/home/priyanka/rajeshprashanth/devel/
./runme.sh > log

mydir=$PWD
for dir in $(ls -d comp_*);do
	cd $dir/CALCS
	for file in $(ls *.vasp);do
		$mydir/rename_poscar.sh $file
	done
	cd $mydir
done
mkdir POSCARS
find ./comp_* -name *.vasp|gawk {'print "cp",$1,"POSCARS/"'}|bash
