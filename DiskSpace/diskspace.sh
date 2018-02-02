#!/bin/bash
#
# Author : Rajesh Prashanth Anandavadivel <rajeshprasanth@rediffmail.com>
# Date : Sun Jan 21 09:00:45 IST 2018
#-----------------------------------------------------------------------------
# Monitor disk space on this the specified directory which is passed as an 
# argument
# 
# Usage: Diskspace.sh </filesystem/to/be/monitored> <option> <size/percent>
#        Option: s -> size in Gigabytes, Megabytes, Kilobytes
#		      9.5G or 4513M or 1045K 
#                p -> percent of usage
#-----------------------------------------------------------------------------
# EXperimental version have only per centage as option
#-----------------------------------------------------------------------------
usage=`df | grep -w "$1" | gawk '{print $5}'| gawk -F"%" '{print $1}'`
available=`df -H | grep -w "$1" | gawk '{print $4}'`
used=`df -H | grep -w "$1" | gawk '{print $3}'`
total=`df -H | grep -w "$1" | gawk '{print $2}'`

if [ $usage -ge $2 ]; then
	echo "+------------------------------------------------+"
	echo "|               Disk Space utility               |"
	echo "+------------------------------------------------+"
	echo "|"
	echo "|Warning ::: Disk space on $1" 
	echo "|            exceeded $2 % currently $usage %"
	echo "|"
	echo "|Disk space information for $1"
	echo "|"
	echo "|     Disk Available.........: $available"
	echo "|     Disk Used..............: $used"
	echo "|     Disk Allocated.........: $total"
	echo "+------------------------------------------------+"
	return 1
	exit 1
else
	echo "+------------------------------------------------+"
	echo "|               Disk Space utility               |"
	echo "+------------------------------------------------+"
	echo "|"
	echo "|Information ::: Disk space on $1" 
	echo "|           is under $2 % currently $usage %"
	echo "|"
	echo "|Disk space information for $1"
	echo "|"
	echo "|     Disk Available.........: $available"
	echo "|     Disk Used..............: $used"
	echo "|     Disk Allocated.........: $total"
	echo "+------------------------------------------------+"
fi
	
