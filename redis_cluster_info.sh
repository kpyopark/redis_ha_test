#!/bin/sh

CONFIG_ENDPOINT=`./redisinfo.py`

SERVERS=`nslookup ${CONFIG_ENDPOINT} | grep Address`

for server in ${SERVERS}
do
    if [[ $server == *"Address"* ]]; then
        # do nothing
        echo 'do nothing'
    elif [[ $server == *"10.0.0.2"* ]]; then
        # do nothing
        echo 'do nothing'
    else
        ./redis_node_cluster_info.py ${server} &
        ./redis_socket_info.py ${server} &
    fi
done

./redis_config_nslookup.py &
./redis_readwrite_continous.py &
./redis_readwrite_discrete.sh &


