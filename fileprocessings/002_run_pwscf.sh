##!/bin/bash
#
#
#--------------------------------------------------------------------
# Path definitions
#--------------------------------------------------------------------
ROOT="/home/aanand/Desktop/CuI/halides/cif/batch"
INBOUND="$ROOT/inbound"
OUTBOUND="$ROOT/outbound"
WORK="$ROOT/work"
ARCHIVE="$ROOT/archive"

#--------------------------------------------------------------------
FULLNAME=`ls -v $WORK/*in|head -n1`
FILENAME=`basename $FULLNAME .in`

cd $WORK && timeout 1800s pw.x < $WORK/$FILENAME.in > $WORK/$FILENAME.out

