#!/bin/bash
#
# Author: Rajesh Prashanth Anandavadivel <rajeshprasanth@rediffmail.com>
# Date:21 23:12:46 IST 2017
#
# Change-log
# Sun Feb  4 19:29:50 IST 2018       Additional feature added to strip extenstion added.
#--------------------------------------------------------------------------------
# Description : Get the filename in the specified path and assign it to a user 
#               specified variable, so that data capture plugin in rundeck can 
#               use it for passing through the job steps.
#--------------------------------------------------------------------------------
# Usage: get_filename.sh </path/to/file> <file_pattern> <rundeck_variable>
#
#--------------------------------------------------------------------------------
# Developer's guide
#--------------------------------------------------------------------------------
# $1 -> path
# $2 -> filename
# $3 -> variable
#--------------------------------------------------------------------------------

cd $1
filename=`ls -1v *$2|head -n1`
for last; do true; done
variable_str=$last
echo "$variable_str=$filename"
FILE_BASENAME=`basename $filename $2`
echo "FILE_BASENAME=$FILE_BASENAME"
