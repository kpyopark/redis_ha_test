#!/usr/bin/python
from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector.pooling
import time

dbconfig = {
  'database' : 'test',
  'user' : 'root'
}

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "LogPool", pool_size = 3, **dbconfig)

'''
 CREATE TABLE `tb_log` (
  `seq_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `elapsed_time` mediumint(9) DEFAULT NULL,
  `target_ip` varchar(30) DEFAULT NULL,
  `event_type` varchar(30) DEFAULT NULL,
  `event_value` varchar(2000) DEFAULT NULL,
  `start_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`seq_id`,`ts`)
) ENGINE=InnoDB AUTO_INCREMENT=718 DEFAULT CHARSET=latin1
'''

def writeLog(start_time, elapsed_time, target_ip, event_type, event_value):
  cnx = cnxpool.get_connection()
  cursor = cnx.cursor()
  add_log = ("insert into tb_log (start_time, elapsed_time, target_ip, event_type, event_value) " \
             "VALUES(%s,%s,%s,%s,%s)")
  log_item = (start_time,elapsed_time,target_ip,event_type,event_value)
  cursor.execute(add_log, log_item);
  cnx.commit()
  cursor.close()
  cnx.close()

class StopWatch:
  def __init__(self):
    self.start_time = time.time() * 1000000

  def stop(self):
    self.end_time = time.time() * 1000000

  def getElapsedTime(self):
    return (self.end_time - self.start_time)

  def getStartTime(self):
    return self.start_time

  def start(self):
    self.start_time = time.time() * 1000000

