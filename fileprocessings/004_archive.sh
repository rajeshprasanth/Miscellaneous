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
cd $ARCHIVE
mkdir archive
mv * archive
tar zcvf archive.tar.gz archive

