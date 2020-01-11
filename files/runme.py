#!/usr/bin/python
#
import sys
import os

percent_sign=['p','p','p','p','p','p','p','p','p','p','0','m','m','m','m','m','m','m','m','m','m']
percent_value=[1,2,3,4,5,6,7,8,9,10,0,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]

uniaxial_qe=['yz','xz','xy']
uniaxial_cell=['x','y','z']
biaxial_qe=['z','x','y']
biaxial_cell=['xy','yz','xz']
system=['Li3Sb','Li3Bi']

filename = str(system[0])
initial=0
def straincalc(initial,strain_per):
	final = initial + ((strain_per*inital)/100)
	return final
      
def uniaxial_cell_gen(in_cell,in_strain,sign,sysname):
  strained_cell_uniaxial_along_x=in_cell
 # strained_cell_uniaxial_along_x[0][0]=straincalc(in_cell[0][0],in_strain)
  
  strained_cell_uniaxial_along_y=in_cell
 # strained_cell_uniaxial_along_y[1][1]=straincalc(in_cell[1][1],in_strain)
  
  strained_cell_uniaxial_along_z=in_cell
 # strained_cell_uniaxial_along_z[2][2]=straincalc(in_cell[2][2],in_strain)
  
  fnamex=str(sysname) + "_uni_x_" + str(sign) + "_" + str(abs(in_strain))+".cell"
  #Li3Sb_uni_x_p_5.cell
  print fnamex


initial_cell_Li3Sb = [[4.01823700000000,0.00000000000000,2.31993000000000],[1.33941200000000,3.78843000000000,2.31993000000000],[0.00000000000000,0.00000000000000,4.63986000000000]]

initial_cell_Li3Bi = [[4.12549800000000,0.00000000000000,2.38185700000000],[1.37516600000000,3.88955700000000,2.38185700000000],[0.00000000000000,0.00000000000000,4.76371500000000]]
i=0
uniaxial_cell_gen(initial_cell_Li3Sb,percent_value[i],percent_sign[i],system[0])