#!/usr/bin/env python

import sys
import spglib
import numpy as np
import time


def version():
	sga_major_number = 1
	sga_minor_number = 0
	sga_revision_number = 0
	spglib_major_number = list(spglib.get_version())[0]
	spglib_minor_number = list(spglib.get_version())[1]
	spglib_revision_number = list(spglib.get_version())[2]
	return(sga_major_number,sga_minor_number,sga_revision_number,spglib_major_number,spglib_minor_number,spglib_revision_number)

def banner():
	print("============================================================")
	print("=====               Space Group Analyser               =====")
	print("============================================================")
	a,b,c,d,e,f=version()
	timestamp = time.strftime('%m/%d/%Y %H:%M:%S')
	print("SGA Version :: %d.%d.%d\t\t Time :: %s" % (a,b,c,timestamp))
	print("\nRunning with Core SPGLIB %d.%d.%d\n" % (d,e,f))

def readinputfilename():
	if len(sys.argv) == 1 :
		print("****No Input file found in command line !!")
		print("****Running in user interactive mode.")
		inputfile = raw_input("Enter Input Structure file >>> ")
		print("****Input file name :: %s" % (inputfile))
		
	else:
		print("****Input file found in command line !!")
		print("****Running in batch mode.")
		print("****Input file name :: %s" % (sys.argv[1]))
		inputfile=sys.argv[1]
	try:
		fp = open(inputfile,'r')
		fp.close()
	except IOError:
		Error(inputfile)	
	print("\nReading data from input file\n")

	return inputfile

def parseinputfile(inputfile):
	coordinates,tempcoor = [],[]
	with open(inputfile,"r") as infile:
		for line in infile:
			if "SYSTEM NAME" in line:
				sysname = str(next(infile).strip())
			if "SCALING PARAMETER" in line:
				scale = float(next(infile))
			if "LATTICE VECTORS" in line:
				latvec1 = next(infile).split()
				latvec2 = next(infile).split()
				latvec3 = next(infile).split()
		
				latvec1_0 = float(latvec1[0])
				latvec1_1 = float(latvec1[1])
				latvec1_2 = float(latvec1[2])

				latvec2_0 = float(latvec2[0])
				latvec2_1 = float(latvec2[1])
				latvec2_2 = float(latvec2[2])

				latvec3_0 = float(latvec3[0])
				latvec3_1 = float(latvec3[1])
				latvec3_2 = float(latvec3[2])
						
				mlatvec1 = tuple([latvec1_0,latvec1_1,latvec1_2])
				mlatvec2 = tuple([latvec2_0,latvec2_1,latvec2_2])
				mlatvec3 = tuple([latvec3_0,latvec3_1,latvec3_2])
				
				latvec = [mlatvec1,mlatvec2,mlatvec3]
			if "NUMBER OF ATOMS" in line:
				numatom = int(next(infile))
			if "ATOMIC SPECIES" in line:
				species = (next(infile).strip().split())
			if "ATOMIC COORDINATES" in line:
				for i in range(int(numatom)):
					templines = next(infile) 
					x,y,z = templines.split()
					coordinates.append(tuple([float(x),float(y),float(z)]))
					
	return sysname,scale,latvec,numatom,species,coordinates

def print_inputdump(sysname,scale,latvec,numatom,species,coordinates):
		print("------------------------------------------------------------");
		print(" Input file dump")
		print("------------------------------------------------------------");
		print("System Name :: %s"%(str(sysname)))
		print("\nScale :: %5.5f\n"%(float(scale)))
		print("Scaled vector 1 :: %10.5f %10.5f %10.5f"%((latvec[0][0]*scale),(latvec[0][1]*scale),(latvec[0][2]*scale)))
		print("Scaled vector 2 :: %10.5f %10.5f %10.5f"%((latvec[1][0]*scale),(latvec[1][1]*scale),(latvec[1][2]*scale)))
		print("Scaled vector 3 :: %10.5f %10.5f %10.5f"%((latvec[2][0]*scale),(latvec[2][1]*scale),(latvec[2][2]*scale)))
		print("\nNumber of atoms/cell :: %d"%(int(numatom)))
		print("\nAtomic species")
		for i in range(int(numatom)):
			print ("%s %10.5f %10.5f %10.5f"%(species[i],coordinates[i][0],coordinates[i][1],coordinates[i][2]))
		print("\n------------------------------------------------------------");
		print(" End of input file dump")
		print("------------------------------------------------------------");		
		
		
def usage():
	raise NotImplementedError
	

def Error(string):
	print("\n============================================================");
	print("Fatal error cannot open :: %s"%(string));
	print("============================================================");
	exit();

