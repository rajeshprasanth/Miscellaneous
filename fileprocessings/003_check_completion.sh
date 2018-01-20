##!/bin/bash
#
#
#--------------------------------------------------------------------
# Path definitions
#--------------------------------------------------------------------
ROOT="/var/lib/rundeck/halides"
INBOUND="$ROOT/inbound"
OUTBOUND="$ROOT/outbound"
WORK="$ROOT/work"
ARCHIVE="$ROOT/archive"
JUNK="$ROOT/junk"
#--------------------------------------------------------------------
OFULLNAME=`ls -v $WORK/*out|head -n1`
OFILENAME=`basename $FULLNAME .out`

IFULLNAME=`ls -v $WORK/*in|head -n1`
IFILENAME=`basename $FULLNAME .in`

grep "This run was terminated on" $OFULLNAME

if [  $? != 0  ] ;then
	mv $IFULLNAME $OFULLNAME $JUNK
else 
	mv $IFULLNAME $ARCHIVE
	mv $OFULLNAME $OUTBOUND
fi
