#!/bin/bash
#
#
runengine() {
     	echo "+--------------------------------------------------------------------+" > $1".log"
	echo "|                 Quantum Espresso Automation Script                 |" >> $1".log"
	echo "+--------------------------------------------------------------------+" >> $1".log"
	echo "" >> $1".log"
	echo "############" >> $1".log"
	echo "# File I/O #" >> $1".log"
	echo "############" >> $1".log"
	echo "    Input file......................: "$1".in" >> $1".log"
	echo "    Output file.....................: "$1".out" >> $1".log"
	echo "    Error file......................: "$1".err" >> $1".log"
	echo "    Log file........................: "$1".log" >> $1".log"
	echo "" >> $1".log"
	echo "#########################" >> $1".log"
	echo "# Simulation Parameters #" >> $1".log"
	echo "#########################" >> $1".log"
	echo "" >> $1".log"
	echo "    Calculation type................: "$(grep -i calculation $1.in |gawk -F\' {'print $2'}) >> $1".log"
	echo "    Cutoff Energy...................: "$(grep -i ecutwfc $1.in |gawk -F= {'print $2'}) "Ry" >> $1".log"
	echo "    Target Pressure.................: "$(grep -i press $1.in |gawk -F= {'print $2'}) "kbar" >> $1".log"
	echo "    Engine Start time...............: "$(date +"%D %T") >> $1".log"
 	pw.x < $1.in > $1.out 2> $1.err
	echo "    Engine Stop time................: "$(date +"%D %T") >> $1".log"
	grep "This run was terminated on" $1.out 

	if [  $? != 0  ] ;then
		echo "" >> $1".log"
		echo "    FATAL ERROR--Premature termination" >> $1".log"
		echo "" >> $1".log"
		echo "    Track the errors in "$1".err" >> $1".log"
		mail -s ":::Quantum-Espresso job failed on $HOSTNAME:::" rajeshprasanth@rediffmail.com < $1".log"
	fi
	echo "+--------------------------------------------------------------------+" >> $1".log"
	echo "|                        Script Terminated                           |" >> $1".log"
	echo "+--------------------------------------------------------------------+" >> $1".log"
}

PBE_PSEUDO_1="Sb.pbe-mt_fhi.UPF"
PBE_PSEUDO_2="Mg.pbe-mt_fhi.UPF"
PW_PSEUDO_1="Sb.pw-mt_fhi.UPF"
PW_PSEUDO_2="Mg.pw-mt_fhi.UPF"

NETWORK_PSEUDO="http://www.quantum-espresso.org/wp-content/uploads/upf_files/"
LOCAL_PSEUDO="/home/rajeshprashanth/pseudo"

wget $NETWORK_PSEUDO/$PBE_PSEUDO_1 
wget $NETWORK_PSEUDO/$PBE_PSEUDO_2 
wget $NETWORK_PSEUDO/$PW_PSEUDO_1
wget $NETWORK_PSEUDO/$PW_PSEUDO_2 

mv *UPF $LOCAL_PSEUDO

for template in Mg3Sb2; do
	for pressure in $(seq 0 10 200); do
		sed -e "s/PRESSURE/$pressure/" -e "s/PSEUDO_1/$PBE_PSEUDO_1/" -e "s/PSEUDO_2/$PBE_PSEUDO_2/" $template > $template.vcrelax.pbe.$pressure.in
		runengine $template.vcrelax.pbe.$pressure
		sed -e "s/PRESSURE/$pressure/" -e "s/PSEUDO_1/$PW_PSEUDO_1/" -e "s/PSEUDO_2/$PW_PSEUDO_2/" $template > $template.vcrelax.pw.$pressure.in
		runengine $template.vcrelax.pw.$pressure
	done
done



rm -rf input output log error
mkdir input output log error

mv *in input && mv *out output && mv *.err error
mv *log log
mail -s ":::Quantum-Espresso jobs is done on $HOSTNAME:::" rajeshprasanth@rediffmail.com

