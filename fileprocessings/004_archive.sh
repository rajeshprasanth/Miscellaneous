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
cd $ARCHIVE
mkdir archive
mv * archive
tar zcvf archive.tar.gz archive

