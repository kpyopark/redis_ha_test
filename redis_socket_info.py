#!/usr/bin/python

import socket
import threading
import LogUtil
from LogUtil import StopWatch
import sys
from time import sleep

target_host = sys.argv[1]

def connect_test(host):
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_address = (host, 6379)
  stopwatch = StopWatch()
  message = 'success'
  try :
    sock.connect(server_address)
  except socket.error as e:
    message = str(e)
  finally :
    stopwatch.stop()
    try :
      sock.close()
    except :
      pass
  if( message != 'success') :
    LogUtil.writeLog(stopwatch.getStartTime(), stopwatch.getElapsedTime(), host, 'SOCKET', message)

while True:
#if True:
  t = threading.Thread(target=connect_test, args=(target_host,))
  t.start()

  sleep(1)
  
