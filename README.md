# redis_ha_test
Redis Cluster HA Test Scripts. These scripts takes logs includes some sorts of events related with the fail-over.

It's very delicate and difficult to check high availability to test Redis Cluster HA functionalities. 
This test suite includes 6 scripts which log the event and changes of status. 

# Prerequiste

1. Install mysql server and create log table.
Before to use this script, you should have to install mysqld (server) and python mysql.connector.
and then, create 'test' database and create log table 'tb_log' by using below scripts.
<code>
(on amazon linux2)
(https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.html)
# sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2
# sudo yum install mariadb-server
# sudo yum install python3
# curl -O https://bootstrap.pypa.io/get-pip.py
# python3 ./get-pip.py --user
# pip install mysql-connector --user
# pip install 
</code>


<pre>
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
</pre>

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

There are some event types.

* CLNODE
 - means results of 'CLUSTER NODES' on each redis nodes. 
 - If previous result is equal to the current status, it will not be logged.
 - Only when the status of nodes was changed, It would be logged.
 
* ROUTE53
 - means results of 'nslookup' to the route53 with config endpoint.
 - when previous dns entry is changed, it will be logged.
 
* SETGETC
 - means recurring processes - get/set to all nodes with one RedisCluster connection
 - After each 5000 get/set ops, it will be logged.
 - Or some exception occured, it will also be logged.
 
* SETGET
 - means recurring processes - get/set to all nodes with new RedisCluster connection
 - After each 10 get/set ops, it will be logged.
 - Or some exception occured, it will also be logged.

* SOCKET
 - means TCP socket connection on each Redis Node.
 - When some error occurred, it will be logged.


