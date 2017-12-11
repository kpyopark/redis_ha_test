#!/bin/sh

var=1

while true
do
  echo ${var}
  ./redis_readwrite.py ${var} &
  sleep 1
  ((++var))
done
  
