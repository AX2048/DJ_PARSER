#!/bin/bash
echo "BEGIN"
date +%F::%H-%M-%S
pwd
whoami
echo "---------------"
cat dns.txt | while read line; do echo $line; dig +short $line; echo "---------------"; done
echo "END"