#!/bin/bash
cat temp.txt >> tcpdumplog.txt
rm temp.txt
touch temp.txt
tcpdump 'icmp[icmptype] = icmp-echo' -n -c 1 -A >> temp.txt 2>&1 &
# TASK_PID1=$!
# sleep 10
# kill $TASK_PID1
# echo 'dead' >> temp.txt
