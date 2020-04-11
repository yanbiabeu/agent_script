#!/bin/bash
if [[ ${uid} -ne 0 ]]
then 
echo "you need root acces"
exit 1
fi
lscpu
uname -r
uname -p
uname
free -m
iostat
cat /proc/meminfo
cat /proc/cpuinfo
cat /etc/os-release
sar -u
nproc
