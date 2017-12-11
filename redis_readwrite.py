#!/usr/bin/python

from rediscluster import StrictRedisCluster
import LogUtil
from LogUtil import StopWatch
from time import sleep
import sys
import redisinfo

startup_nodes = [{"host":redisinfo.getConfigEndpoint(), "port":"6379"}]

rc = StrictRedisCluster(startup_nodes=startup_nodes, skip_full_coverage_check=True)
rc_readonly = StrictRedisCluster(startup_nodes=startup_nodes, skip_full_coverage_check=True, readonly_mode=True)
inx = int(sys.argv[1])

stopwatch = StopWatch()
target_host = ''

success = 0
failure = 0

if True:
  try :
    stopwatch.start()
    target_host = 'foo' + str(inx) + ':set'
    rc.set("foo"+str(inx),"bar"+str(inx))
    target_host = 'foo' + str(inx) + ':get'
    rc_readonly.get("foo"+str(inx))
    success += 1
    stopwatch.stop()
    if (inx % 10 == 0):
      LogUtil.writeLog(stopwatch.getStartTime(), stopwatch.getElapsedTime(), 
        target_host, 'SETGET', 'INX:' + str(inx))
    
  except :
    failure += 1
    stopwatch.stop()
    LogUtil.writeLog(stopwatch.getStartTime(), stopwatch.getElapsedTime(), 
      target_host, 'SETGET', 'Exception Occurred')


