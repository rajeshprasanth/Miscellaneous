#!/usr/bin/python
#
import sys
import os
#
v1_x = float(sys.argv[1])
v1_y = float(sys.argv[2])
v1_z = float(sys.argv[3])
#
v2_x = float(sys.argv[4])
v2_y = float(sys.argv[5])
v2_z = float(sys.argv[6])
#
v3_x = float(sys.argv[7])
v3_y = float(sys.argv[8])
v3_z = float(sys.argv[9])
#
strain_percentd = float(sys.argv[10])
#
systemname = sys.argv[11]
#
uniaxial_qe_setting=['yz','xz','xy']
uniaxial_cell=['x','y','z']
#
biaxial_qe_setting=['z','x','y']
biaxial_cell=['xy','yz','xz']
#
def uniaxial_x(x,strain_comp):
	print straincalc(x,strain_comp)
	
def straincalc(initial,strain_percent):
	final = float(initial) + ((float(strain_percent)*inital)/100)
	return final
	
uniaxial_x(v1_x,strain_percentd)
