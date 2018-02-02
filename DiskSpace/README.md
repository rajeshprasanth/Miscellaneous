				Diskspace monitoring script for rundeck.
				
Usage: diskspace.sh <partition> <percentage of used space>

Example: 

When disk space is greater than specified, the script fails with the output shown as below.

aanand@ubuntu:~/misc/diskspace$ ./diskspace.sh /dev/loop0 70
+------------------------------------------------+
|               Disk Space utility               |
+------------------------------------------------+

Warning ::: Disk space on /dev/loop0
            exceeded 70 % currently 96 %

Disk space information for /dev/loop0

     Disk Available.........: 481M
     Disk Used..............: 9.2G
     Disk Allocated.........: 11G
+------------------------------------------------+
diskspace.sh: line 35: return: can only `return' from a function or sourced script

When disk space is lesser than specified, the script runs with the output shown as below.

aanand@ubuntu:~/misc/diskspace$ diskspace.sh /dev/loop0 98
+------------------------------------------------+
|               Disk Space utility               |
+------------------------------------------------+

Information ::: Disk space on /dev/loop0
           is under 98 % currently 96 %

Disk space information for /dev/loop0

     Disk Available.........: 481M
     Disk Used..............: 9.2G
     Disk Allocated.........: 11G
+------------------------------------------------+
