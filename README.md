# redis_ha_test
Redis Cluster HA Test Scripts. These scripts takes logs includes some sorts of events related with the fail-over.

It's very delicate and difficult to check high availability to test Redis Cluster HA functionalities. 
This test suite includes 6 scripts which log the event and changes of status. 

# Prerequiste

1. Install mysql server and create log table.
Before to use this script, you should have to install mysqld (server) and python mysql.connector.
and then, create 'test' database and create log table 'tb_log' by using below scripts.

<code>

create database test;

CREATE TABLE `tb_log` (
  `seq_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `ts` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `elapsed_time` mediumint(9) DEFAULT NULL,
  `target_ip` varchar(30) DEFAULT NULL,
  `event_type` varchar(30) DEFAULT NULL,
  `event_value` varchar(2000) DEFAULT NULL,
  `start_time` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`seq_id`,`ts`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

</code>

2. Modify Config Endpoint
Update config endpoint entry in redisinfo.py file.

# To test

It's very simple to start script.

<code>

./redis_cluster_info.sh

</code>

and then, you can fail-over your redis cluster to test it.

# Logs in log table (tb_log)

Logs includes the cluster node info on each nodes and route53's config endpoint entry items.
If some exceptions occured during setting/getting the value to the redis cluster, it will be also logged.

