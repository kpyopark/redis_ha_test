#!/usr/bin/python

from rediscluster import StrictRedisCluster
import LogUtil
import redisinfo
from LogUtil import StopWatch
from time import sleep

startup_nodes = [{"host":redisinfo.getConfigEndpoint(), "port":"6379"}]

rc = StrictRedisCluster(startup_nodes=startup_nodes, skip_full_coverage_check=True)
rc_readonly = StrictRedisCluster(startup_nodes=startup_nodes, skip_full_coverage_check=True, readonly_mode=True)
inx = 0

stopwatch = StopWatch()
target_host = ''
stopwatch5000 = StopWatch()

success = 0
failure = 0

while True:
  inx += 1
  try :
    stopwatch.start()
    target_host = 'foo' + str(inx) + ':set'
    rc.set("foo"+str(inx),"bar"+str(inx))
    target_host = 'foo' + str(inx) + ':get'
    rc_readonly.get("foo"+str(inx))
    success += 1
    if( inx % 5000 == 0 ):
      stopwatch5000.stop()
      LogUtil.writeLog(stopwatch5000.getStartTime(), stopwatch5000.getElapsedTime(), 
        target_host, 'SETGETC', str(success) + ':' + str(failure))
      stopwatch5000.start()
    
    stopwatch.stop()
  except :
    failure += 1
    stopwatch.stop()
    LogUtil.writeLog(stopwatch.getStartTime(), stopwatch.getElapsedTime(), 
      target_host, 'SETGETC', 'Exception Occurred')


