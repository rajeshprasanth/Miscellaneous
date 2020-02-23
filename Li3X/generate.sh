#!/bin/bash
#
#
for func in "pbe" "pw";do
for file in $(basename -s .vasp *.vasp);do
./AFLOWQE $file.vasp .$func.mt-fhi.UPF template $file.$func.vcrelax
done
done