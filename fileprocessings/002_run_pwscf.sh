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

#--------------------------------------------------------------------
FULLNAME=`ls -v $WORK/*in|head -n1`
FILENAME=`basename $FULLNAME .in`

cd $WORK && timeout 1800s pw.x < $WORK/$FILENAME.in > $WORK/$FILENAME.out

