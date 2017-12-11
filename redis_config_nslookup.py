#!/usr/bin/python

import socket
import LogUtil
import redisinfo
from LogUtil import StopWatch
from time import sleep

prev_nodes = ['']
stopwatch = StopWatch()

while True:
  stopwatch.start()
  ais = socket.getaddrinfo(redisinfo.getConfigEndpoint(),0,0,0,0)
  stopwatch.stop()
  nodes = []

  for result in ais:
    if result[-1][0] not in nodes:
      nodes.append(result[-1][0])

  if (prev_nodes[0] != nodes[0] or len(prev_nodes) != len(nodes)) :
    LogUtil.writeLog(stopwatch.getStartTime(), stopwatch.getElapsedTime(), '10.0.0.2', 'ROUTE53', ','.join(nodes))
    prev_nodes = nodes

  sleep(0.05)

