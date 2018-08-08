#!/usr/bin/env python

import sys
import spglib
import numpy as np
import time
import math
import spglib


#######################################################################
# Using the local Atoms-like class (BSD license) where a small set of #
# ASE Atoms features is comaptible but enough for this example.       #
#######################################################################
from atoms import Atoms

def print_realspace_lattice(scale,latvec):
	a,b,c,alpha,beta,gamma = compute_lattice_parameters(scale,latvec)
	print "\nREAL SPACE LATTICE"
	print "\tReal space a (ang/bohr) :: %f / %f" %(a,ang2bohr(a))
	print "\tReal space b (ang/bohr) :: %f / %f" %(b,ang2bohr(b))
	print "\tReal space c (ang/bohr) :: %f / %f" %(c,ang2bohr(c))
	print "\tReal space alpha (deg) :: %f" %(alpha)
	print "\tReal space beta  (deg) :: %f" %(beta)
	print "\tReal space gamma (deg) :: %f" %(gamma)
	print "\tReal space volume (ang^3/bohr^3):: %f / %f" %(volume(a,b,c,alpha,beta,gamma),volume(ang2bohr(a),ang2bohr(b),ang2bohr(c),alpha,beta,gamma))
	print "\tReal space c/a :: %f "%(c/a)

def print_pointgroup(dataset):
	spacegroup_type = spglib.get_spacegroup_type(dataset['hall_number'])
	print "\nPOINT GROUP OF CRYSTAL"
	print "\tPoint group (number) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[0]
	print "\tPoint group (crystal family) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[1]
	print "\tPoint group (crystal_system) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[2]
	print "\tPoint group (crystal_class) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[3]
	print "\tPoint group (HM_inter_full) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[4]
	print "\tPoint group (HM_inter_short) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[5]
	print "\tPoint group (shubnikov) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[6]
	print "\tPoint group (schoenflies) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[7]
	print "\tPoint group (orbifold) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[8]
	print "\tPoint group (coxeter) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[9]
	print "\tPoint group (order) :: ",pointgroup_database(spacegroup_type['pointgroup_schoenflies'])[10]

	
#-----------------------------------------------------------------------------------------	
def pointgroup_database(pointgroup_short):
	pointgroup_number = ""		# a
	pointgroup_crystal_family = ""	# b
	pointgroup_crystal_system = ""	# c
	pointgroup_crystal_class = ""	# d
	pointgroup_HM_inter_full = ""	# e
	pointgroup_HM_inter_short = ""	# f
	pointgroup_shubnikov = ""	# g
	pointgroup_schoenflies = ""	# h
	pointgroup_orbifold = ""	# i
	pointgroup_coxeter = ""		# j
	pointgroup_order = ""		# k
	#-------------------------#
	# Point group # 1         #
	#-------------------------#

	if pointgroup_short == "1":
		pointgroup_number = "1"
		pointgroup_crystal_family = "triclinic"
		pointgroup_crystal_system = "triclinic"
		pointgroup_crystal_class = "triclinic-pedial"
		pointgroup_HM_inter_full = "1"
		pointgroup_HM_inter_short = "1"
		pointgroup_shubnikov = "1"
		pointgroup_schoenflies = "C1"
		pointgroup_orbifold = "11"
		pointgroup_coxeter = "[]+"
		pointgroup_order = "1"

	#-------------------------#
	# Point group # 2         #
	#-------------------------#

	if pointgroup_short == "-1":
		pointgroup_number = "2"
		pointgroup_crystal_family = "triclinic"
		pointgroup_crystal_system = "triclinic"
		pointgroup_crystal_class = "triclinic-pinacoidal"
		pointgroup_HM_inter_full = "-1"
		pointgroup_HM_inter_short = "-1"
		pointgroup_shubnikov = "~2"
		pointgroup_schoenflies = "Ci = S2"
		pointgroup_orbifold = "x"
		pointgroup_coxeter = "[2+,2+]"
		pointgroup_order = "2"

	#-------------------------#
	# Point group # 3         #
	#-------------------------#

	if pointgroup_short == "2":
		pointgroup_number = "3"
		pointgroup_crystal_family = "monoclinic"
		pointgroup_crystal_system = "monoclinic"
		pointgroup_crystal_class = "monoclinic-sphenoidal"
		pointgroup_HM_inter_full = "2"
		pointgroup_HM_inter_short = "2"
		pointgroup_shubnikov = "2"
		pointgroup_schoenflies = "C2"
		pointgroup_orbifold = "22"
		pointgroup_coxeter = "[2+]"
		pointgroup_order = "2"

	#-------------------------#
	# Point group # 4         #
	#-------------------------#

	if pointgroup_short == "m":
		pointgroup_number = "4"
		pointgroup_crystal_family = "monoclinic"
		pointgroup_crystal_system = "monoclinic"
		pointgroup_crystal_class = "monoclinic-domatic"
		pointgroup_HM_inter_full = "m"
		pointgroup_HM_inter_short = "m"
		pointgroup_shubnikov = "m"
		pointgroup_schoenflies = "Cs = C1h"
		pointgroup_orbifold = "*"
		pointgroup_coxeter = "[]"
		pointgroup_order = "2"

	#-------------------------#
	# Point group # 5         #
	#-------------------------#

	if pointgroup_short == "2/m":
		pointgroup_number = "5"
		pointgroup_crystal_family = "monoclinic"
		pointgroup_crystal_system = "monoclinic"
		pointgroup_crystal_class = "monoclinic-prismatic"
		pointgroup_HM_inter_full = "2/m"
		pointgroup_HM_inter_short = "2/m"
		pointgroup_shubnikov = "2:m"
		pointgroup_schoenflies = "C2h"
		pointgroup_orbifold = "2*"
		pointgroup_coxeter = "[2,2+]"
		pointgroup_order = "4"

	#-------------------------#
	# Point group # 6         #
	#-------------------------#

	if pointgroup_short == "222":
		pointgroup_number = "6"
		pointgroup_crystal_family = "orthorhombic"
		pointgroup_crystal_system = "orthorhombic"
		pointgroup_crystal_class = "orthorhombic-sphenoidal"
		pointgroup_HM_inter_full = "222"
		pointgroup_HM_inter_short = "222"
		pointgroup_shubnikov = "2:2"
		pointgroup_schoenflies = "D2 = V"
		pointgroup_orbifold = "222"
		pointgroup_coxeter = "[2,2]+"
		pointgroup_order = "4"

	#-------------------------#
	# Point group # 7         #
	#-------------------------#

	if pointgroup_short == "mm2":
		pointgroup_number = "7"
		pointgroup_crystal_family = "orthorhombic"
		pointgroup_crystal_system = "orthorhombic"
		pointgroup_crystal_class = "orthorhombic-pyramidal"
		pointgroup_HM_inter_full = "mm2"
		pointgroup_HM_inter_short = "mm2"
		pointgroup_shubnikov = "2.m"
		pointgroup_schoenflies = "C2v"
		pointgroup_orbifold = "*22"
		pointgroup_coxeter = "[2]"
		pointgroup_order = "4"

	#-------------------------#
	# Point group # 8         #
	#-------------------------#

	if pointgroup_short == "mmm":
		pointgroup_number = "8"
		pointgroup_crystal_family = "orthorhombic"
		pointgroup_crystal_system = "orthorhombic"
		pointgroup_crystal_class = "orthorhombic-bipyramidal"
		pointgroup_HM_inter_full = "2/m 2/m 2/m"
		pointgroup_HM_inter_short = "mmm"
		pointgroup_shubnikov = "m.2:m"
		pointgroup_schoenflies = "D2h = Vh"
		pointgroup_orbifold = "*222"
		pointgroup_coxeter = "[2,2]"
		pointgroup_order = "8"

	#-------------------------#
	# Point group # 9         #
	#-------------------------#

	if pointgroup_short == "4":
		pointgroup_number = "9"
		pointgroup_crystal_family = "tetragonal"
		pointgroup_crystal_system = "tetragonal"
		pointgroup_crystal_class = "tetragonal-pyramidal"
		pointgroup_HM_inter_full = "4"
		pointgroup_HM_inter_short = "4"
		pointgroup_shubnikov = "4"
		pointgroup_schoenflies = "C4"
		pointgroup_orbifold = "44"
		pointgroup_coxeter = "[4]+"
		pointgroup_order = "4"

	#-------------------------#
	# Point group # 10        #
	#-------------------------#

	if pointgroup_short == "-4":
		pointgroup_number = "10"
		pointgroup_crystal_family = "tetragonal"
		pointgroup_crystal_system = "tetragonal"
		pointgroup_crystal_class = "tetragonal-disphenoidal"
		pointgroup_HM_inter_full = "-4"
		pointgroup_HM_inter_short = "-4"
		pointgroup_shubnikov = "~4"
		pointgroup_schoenflies = "S4"
		pointgroup_orbifold = "2x"
		pointgroup_coxeter = "[2+,4+]"
		pointgroup_order = "4"

	#-------------------------#
	# Point group # 11        #
	#-------------------------#

	if pointgroup_short == "4/m":
		pointgroup_number = "11"
		pointgroup_crystal_family = "tetragonal"
		pointgroup_crystal_system = "tetragonal"
		pointgroup_crystal_class = "tetragonal-dipyramidal"
		pointgroup_HM_inter_full = "4/m"
		pointgroup_HM_inter_short = "4/m"
		pointgroup_shubnikov = "4:m"
		pointgroup_schoenflies = "C4h"
		pointgroup_orbifold = "4*"
		pointgroup_coxeter = "[2,4+]"
		pointgroup_order = "8"

	#-------------------------#
	# Point group # 12         #
	#-------------------------#

	if pointgroup_short == "422":
		pointgroup_number = "12"
		pointgroup_crystal_family = "tetragonal"
		pointgroup_crystal_system = "tetragonal"
		pointgroup_crystal_class = "tetragonal-trapezoidal"
		pointgroup_HM_inter_full = "422"
		pointgroup_HM_inter_short = "422"
		pointgroup_shubnikov = "4:2"
		pointgroup_schoenflies = "D4"
		pointgroup_orbifold = "422"
		pointgroup_coxeter = "[4,2]+"
		pointgroup_order = "8"

	#-------------------------#
	# Point group # 13         #
	#-------------------------#

	if pointgroup_short == "4mm":
		pointgroup_number = "13"
		pointgroup_crystal_family = "tetragonal"
		pointgroup_crystal_system = "tetragonal"
		pointgroup_crystal_class = "ditetragonal-pyramidal"
		pointgroup_HM_inter_full = "4mm"
		pointgroup_HM_inter_short = "4mm"
		pointgroup_shubnikov = "4.m"
		pointgroup_schoenflies = "C4v"
		pointgroup_orbifold = "*44"
		pointgroup_coxeter = "[4]"
		pointgroup_order = "8"

	#-------------------------#
	# Point group # 14         #
	#-------------------------#

	if pointgroup_short == "-42m":
		pointgroup_number = "14"
		pointgroup_crystal_family = "tetragonal"
		pointgroup_crystal_system = "tetragonal"
		pointgroup_crystal_class = "tetragonal-scalenoidal"
		pointgroup_HM_inter_full = "-42m"
		pointgroup_HM_inter_short = "-42m"
		pointgroup_shubnikov = "~4.m"
		pointgroup_schoenflies = "D2d = Vd"
		pointgroup_orbifold = "2*2"
		pointgroup_coxeter = "[2+,4]"
		pointgroup_order = "8"

	#-------------------------#
	# Point group # 15         #
	#-------------------------#

	if pointgroup_short == "4/mmm":
		pointgroup_number = "15"
		pointgroup_crystal_family = "tetragonal"
		pointgroup_crystal_system = "tetragonal"
		pointgroup_crystal_class = "ditetragonal-dipyramidal"
		pointgroup_HM_inter_full = "4/m 2/m 2/m"
		pointgroup_HM_inter_short = "4/mmm"
		pointgroup_shubnikov = "m.4:m"
		pointgroup_schoenflies = "D4h"
		pointgroup_orbifold = "*422"
		pointgroup_coxeter = "[4,2]"
		pointgroup_order = "16"

	#-------------------------#
	# Point group # 16         #
	#-------------------------#

	if pointgroup_short == "3":
		pointgroup_number = "16"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "trigonal"
		pointgroup_crystal_class = "trigonal-pyramidal"
		pointgroup_HM_inter_full = "3"
		pointgroup_HM_inter_short = "3"
		pointgroup_shubnikov = "3"
		pointgroup_schoenflies = "C3"
		pointgroup_orbifold = "33"
		pointgroup_coxeter = "[3]+"
		pointgroup_order = "3"

	#-------------------------#
	# Point group # 17         #
	#-------------------------#

	if pointgroup_short == "-3":
		pointgroup_number = "17"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "trigonal"
		pointgroup_crystal_class = "rhombohedral"
		pointgroup_HM_inter_full = "-3"
		pointgroup_HM_inter_short = "-3"
		pointgroup_shubnikov = "~6"
		pointgroup_schoenflies = "S6 = C3i"
		pointgroup_orbifold = "3x"
		pointgroup_coxeter = "[2+,6+]"
		pointgroup_order = "6"

	#-------------------------#
	# Point group # 18        #
	#-------------------------#

	if pointgroup_short == "32":
		pointgroup_number = "18"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "trigonal"
		pointgroup_crystal_class = "trigonal-trapezoidal"
		pointgroup_HM_inter_full = "32"
		pointgroup_HM_inter_short = "32"
		pointgroup_shubnikov = "3:2"
		pointgroup_schoenflies = "D3"
		pointgroup_orbifold = "322"
		pointgroup_coxeter = "[3,2]+"
		pointgroup_order = "6"

	#-------------------------#
	# Point group # 19        #
	#-------------------------#

	if pointgroup_short == "3m":
		pointgroup_number = "19"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "trigonal"
		pointgroup_crystal_class = "ditrigonal-pyramidal"
		pointgroup_HM_inter_full = "3m"
		pointgroup_HM_inter_short = "3m"
		pointgroup_shubnikov = "3.m"
		pointgroup_schoenflies = "C3v"
		pointgroup_orbifold = "*33"
		pointgroup_coxeter = "[3]"
		pointgroup_order = "6"

	#-------------------------#
	# Point group # 20        #
	#-------------------------#

	if pointgroup_short == "-3m":
		pointgroup_number = "20"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "trigonal"
		pointgroup_crystal_class = "ditrigonal-scalahedral"
		pointgroup_HM_inter_full = "-3 2/m"
		pointgroup_HM_inter_short = "-3m"
		pointgroup_shubnikov = "~6.m"
		pointgroup_schoenflies = "D3d"
		pointgroup_orbifold = "2*3"
		pointgroup_coxeter = "[2+,6]"
		pointgroup_order = "12"

	#-------------------------#
	# Point group # 21        #
	#-------------------------#

	if pointgroup_short == "6":
		pointgroup_number = "21"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "hexagonal"
		pointgroup_crystal_class = "hexagonal-pyramidal"
		pointgroup_HM_inter_full = "6"
		pointgroup_HM_inter_short = "6"
		pointgroup_shubnikov = "6"
		pointgroup_schoenflies = "C6"
		pointgroup_orbifold = "66"
		pointgroup_coxeter = "[6]+"
		pointgroup_order = "6"

	#-------------------------#
	# Point group # 22        #
	#-------------------------#

	if pointgroup_short == "-6":
		pointgroup_number = "22"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "hexagonal"
		pointgroup_crystal_class = "trigonal-dipyramidal"
		pointgroup_HM_inter_full = "-6"
		pointgroup_HM_inter_short = "-6"
		pointgroup_shubnikov = "3:m"
		pointgroup_schoenflies = "C3h"
		pointgroup_orbifold = "3*"
		pointgroup_coxeter = "[2,3+]"
		pointgroup_order = "6"

	#-------------------------#
	# Point group # 23        #
	#-------------------------#

	if pointgroup_short == "6/m":
		pointgroup_number = "23"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "hexagonal"
		pointgroup_crystal_class = "hexagonal-dipyramidal"
		pointgroup_HM_inter_full = "6/m"
		pointgroup_HM_inter_short = "6/m"
		pointgroup_shubnikov = "6:m"
		pointgroup_schoenflies = "C6h"
		pointgroup_orbifold = "6*"
		pointgroup_coxeter = "[2,6+]"
		pointgroup_order = "12"

	#-------------------------#
	# Point group # 24        #
	#-------------------------#

	if pointgroup_short == "622":
		pointgroup_number = "24"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "hexagonal"
		pointgroup_crystal_class = "hexagonal-trapezoidal"
		pointgroup_HM_inter_full = "622"
		pointgroup_HM_inter_short = "622"
		pointgroup_shubnikov = "6:2"
		pointgroup_schoenflies = "D6"
		pointgroup_orbifold = "622"
		pointgroup_coxeter = "[6,2]+"
		pointgroup_order = "12"

	#-------------------------#
	# Point group # 25        #
	#-------------------------#

	if pointgroup_short == "6mm":
		pointgroup_number = "25"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "hexagonal"
		pointgroup_crystal_class = "dihexagonal-pyramidal"
		pointgroup_HM_inter_full = "6mm"
		pointgroup_HM_inter_short = "6mm"
		pointgroup_shubnikov = "6.m"
		pointgroup_schoenflies = "C6v"
		pointgroup_orbifold = "*66"
		pointgroup_coxeter = "[6]"
		pointgroup_order = "12"

	#-------------------------#
	# Point group # 26        #
	#-------------------------#

	if pointgroup_short == "-62m":
		pointgroup_number = "26"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "hexagonal"
		pointgroup_crystal_class = "ditrigonal-dipyramidal"
		pointgroup_HM_inter_full = "-6m2"
		pointgroup_HM_inter_short = "-62m"
		pointgroup_shubnikov = "m.3:m"
		pointgroup_schoenflies = "D3h"
		pointgroup_orbifold = "*322"
		pointgroup_coxeter = "[3,2]"
		pointgroup_order = "12"

	#-------------------------#
	# Point group # 27        #
	#-------------------------#

	if pointgroup_short == "6/mmm":
		pointgroup_number = "27"
		pointgroup_crystal_family = "hexagonal"
		pointgroup_crystal_system = "hexagonal"
		pointgroup_crystal_class = "dihexagonal-dipyramidal"
		pointgroup_HM_inter_full = "6/m 2/m 2/m"
		pointgroup_HM_inter_short = "6/mmm"
		pointgroup_shubnikov = "m.6:m"
		pointgroup_schoenflies = "D6h"
		pointgroup_orbifold = "*622"
		pointgroup_coxeter = "[6,2]"
		pointgroup_order = "24"

	#-------------------------#
	# Point group # 28        #
	#-------------------------#

	if pointgroup_short == "23":
		pointgroup_number = "28"
		pointgroup_crystal_family = "cubic"
		pointgroup_crystal_system = "cubic"
		pointgroup_crystal_class = "tetrahedral"
		pointgroup_HM_inter_full = "23"
		pointgroup_HM_inter_short = "23"
		pointgroup_shubnikov = "3/2"
		pointgroup_schoenflies = "T"
		pointgroup_orbifold = "332"
		pointgroup_coxeter = "[3,3]+"
		pointgroup_order = "12"

	#-------------------------#
	# Point group # 29        #
	#-------------------------#

	if pointgroup_short == "m-3":
		pointgroup_number = "29"
		pointgroup_crystal_family = "cubic"
		pointgroup_crystal_system = "cubic"
		pointgroup_crystal_class = "hextetrahedral"
		pointgroup_HM_inter_full = "2/m -3"
		pointgroup_HM_inter_short = "m-3"
		pointgroup_shubnikov = "~6/2"
		pointgroup_schoenflies = "Th"
		pointgroup_orbifold = "3*2"
		pointgroup_coxeter = "[3+,4]"
		pointgroup_order = "24"

	#-------------------------#
	# Point group # 30        #
	#-------------------------#

	if pointgroup_short == "432":
		pointgroup_number = "30"
		pointgroup_crystal_family = "cubic"
		pointgroup_crystal_system = "cubic"
		pointgroup_crystal_class = "diploidal"
		pointgroup_HM_inter_full = "432"
		pointgroup_HM_inter_short = "432"
		pointgroup_shubnikov = "3/4"
		pointgroup_schoenflies = "O"
		pointgroup_orbifold = "432"
		pointgroup_coxeter = "[4,3]+"
		pointgroup_order = "24"

	#-------------------------#
	# Point group # 31        #
	#-------------------------#

	if pointgroup_short == "-43m":
		pointgroup_number = "31"
		pointgroup_crystal_family = "cubic"
		pointgroup_crystal_system = "cubic"
		pointgroup_crystal_class = "gyroidal"
		pointgroup_HM_inter_full = "-43m"
		pointgroup_HM_inter_short = "-43m"
		pointgroup_shubnikov = "3/~4"
		pointgroup_schoenflies = "Td"
		pointgroup_orbifold = "*332"
		pointgroup_coxeter = "[3,3]"
		pointgroup_order = "24"

	#-------------------------#
	# Point group # 32        #
	#-------------------------#
	
	if pointgroup_short == "m-3m":
		pointgroup_number = "32"
		pointgroup_crystal_family = "cubic"
		pointgroup_crystal_system = "cubic"
		pointgroup_crystal_class = "hexoctahedral"
		pointgroup_HM_inter_full = "4/m -3 2/m"
		pointgroup_HM_inter_short = "m-3m"
		pointgroup_shubnikov = "~6/4"
		pointgroup_schoenflies = "Oh"
		pointgroup_orbifold = "*432"
		pointgroup_coxeter = "[4,3]"
		pointgroup_order = "48"
	
	return (pointgroup_number,pointgroup_crystal_family,pointgroup_crystal_system,pointgroup_crystal_class,pointgroup_HM_inter_full,pointgroup_HM_inter_short,pointgroup_shubnikov,pointgroup_schoenflies,pointgroup_orbifold,pointgroup_coxeter,pointgroup_order)
#-----------------------------------------------------------------------------------------	

def compute_lattice_parameters(scale,latvec):
	a = math.sqrt((scale*latvec[0][0])**2 + (scale*latvec[0][1])**2 + (scale*latvec[0][2])**2  )
	b = math.sqrt((scale*latvec[1][0])**2 + (scale*latvec[1][1])**2 + (scale*latvec[1][2])**2  )
	c = math.sqrt((scale*latvec[2][0])**2 + (scale*latvec[2][1])**2 + (scale*latvec[2][2])**2  )
	alpha_rad = math.acos(dot_product(latvec[1],latvec[2])/(b*c))
	beta_rad = math.acos(dot_product(latvec[2],latvec[0])/(c*a))
	gamma_rad = math.acos(dot_product(latvec[0],latvec[1])/(a*b))
	alpha = rad2deg(alpha_rad)
	beta = rad2deg(beta_rad)
	gamma = rad2deg(gamma_rad)
	return a,b,c,alpha,beta,gamma

def volume(a,b,c,alpha,beta,gamma):

	rad_alpha = deg2rad(alpha)
	rad_beta = deg2rad(beta)
	rad_gamma = deg2rad(gamma)
	sq_cos_alpha = math.cos(rad_alpha)**2
	sq_cos_beta = math.cos(rad_beta)**2
	sq_cos_gamma = math.cos(rad_gamma)**2
			
	
	part1 = a*b*c
	part2 = 1 - sq_cos_alpha - sq_cos_beta - sq_cos_gamma + 2 * (math.cos(rad_alpha)*math.cos(rad_beta)*math.cos(rad_gamma))
	
		
	vol = part1*math.sqrt(part2)
	return vol

def spacegroupdata(sysname,scale,latvec,numatom,species,coordinates):
	atomicseries = []
	#	
	for i in range(numatom):
		atomicseries.append(element2atomicnumber(species[i]))
	#
	system = (latvec,coordinates,atomicseries)
	dataset = spglib.get_symmetry_dataset(system)
	return dataset

def find_crystaltype(dataset):
	print "none"
#-----------------------#
# 1 Bohr = 1.889726 Ang #
#-----------------------#
def ang2bohr(ang):
	return (1.889726*ang)

#-----------------------#
# 1 Ang = 0.529177 Bohr #
#-----------------------#
def bohr2ang(bohr):
	return (0.529177*bohr)

#--------------------#
# 360 deg = 2 pi rad #
# 180 deg = pi rad   #
#--------------------#
def deg2rad(deg):
	return (math.pi*deg)/180
		
#--------------------#
# 360 deg = 2 pi rad #
# 180 deg = pi rad   #
#--------------------#
def rad2deg(rad):
	return (180*rad)/math.pi

#---------------------------------------------------------#
# a = a(0)i + a(1)j + a(2)k                               #
# b = b(0)i + b(1)j + c(2)k                               #
# a .dot. b =  [a(0)*b(0)] + [a(1)*b(1)] + [a(2)*b(3)]    #
#---------------------------------------------------------#
def dot_product(vector1, vector2):
	return (vector1[0]*vector2[0]) + (vector1[1]*vector2[1]) + (vector1[2]*vector2[2])
	

def element2atomicnumber(element):
	atom_lookup = {'H' : 1,'He' : 2,'Li' : 3,'Be' : 4,'B' : 5,'C' : 6,'N' : 7,'O' : 8,'F' : 9,'Ne' : 10,'Na' : 11,'Mg' : 12,'Al' : 13,'Si' : 14,'P' : 15,'S' : 16,'Cl' : 17,'Ar' : 18,'K' : 19,'Ca' : 20,'Sc' : 21,'Ti' : 22,'V' : 23,'Cr' : 24,'Mn' : 25,'Fe' : 26,'Co' : 27,'Ni' : 28,'Cu' : 29,'Zn' : 30,'Ga' : 31,'Ge' : 32,'As' : 33,'Se' : 34,'Br' : 35,'Kr' : 36,'Rb' : 37,'Sr' : 38,'Y' : 39,'Zr' : 40,'Nb' : 41,'Mo' : 42,'Tc' : 43,'Ru' : 44,'Rh' : 45,'Pd' : 46,'Ag' : 47,'Cd' : 48,'In' : 49,'Sn' : 50,'Sb' : 51,'Te' : 52,'I' : 53,'Xe' : 54,'Cs' : 55,'Ba' : 56,'La' : 57,'Ce' : 58,'Pr' : 59,'Nd' : 60,'Pm' : 61,'Sm' : 62,'Eu' : 63,'Gd' : 64,'Tb' : 65,'Dy' : 66,'Ho' : 67,'Er' : 68,'Tm' : 69,'Yb' : 70,'Lu' : 71,'Hf' : 72,'Ta' : 73,'W' : 74,'Re' : 75,'Os' : 76,'Ir' : 77,'Pt' : 78,'Au' : 79,'Hg' : 80,'Tl' : 81,'Pb' : 82,'Bi' : 83,'Po' : 84,'At' : 85,'Rn' : 86,'Fr' : 87,'Ra' : 88,'Ac' : 89,'Th' : 90,'Pa' : 91,'U' : 92,'Np' : 93,'Pu' : 94,'Am' : 95,'Cm' : 96,'Bk' : 97,'Cf' : 98,'Es' : 99,'Fm' : 100,'Md' : 101,'No' : 102,'Lr' : 103,'Rf' : 104,'Db' : 105,'Sg' : 106,'Bh' : 107,'Hs' : 108,'Mt' : 109,'Ds' : 110,'Rg' : 111,'Cn' : 112,'Nh' : 113,'Fl' : 114,'Mc' : 115,'Lv' : 116,'Ts' : 117,'Og' : 118
	}
	return atom_lookup[element]
	

