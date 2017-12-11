#!/usr/bin/python

import subprocess
import sys
import LogUtil
from LogUtil import StopWatch
from time import sleep

target_node = sys.argv[1]
prev_nodes = []
stopwatch = StopWatch()


while True:
#if True:
  stopwatch.start()
  result = subprocess.check_output('./redis-cli -h ' + target_node + ' -p 6379 cluster nodes', shell=True)
  stopwatch.stop()
  nodes = []
  for node in result.splitlines() :
    node_split = node.split()
    node_info = {
      'node_id' : node_split[0], 
      'node_ip_port' : node_split[1], 
      'flags' : node_split[2], 
      'master_id' : node_split[3], 
      'connected' :node_split[6]
    }
    # print(node_info)
    nodes.append(node_info)
    
  if (prev_nodes != nodes) :
    LogUtil.writeLog(stopwatch.getStartTime(), stopwatch.getElapsedTime(), target_node, 'CLNODE', result)
    prev_nodes = nodes

  sleep(0.05)
  
