#!/bin/bash
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
FILENAME=`ls -v $INBOUND/*in|head -n1`
mv $FILENAME $WORK
