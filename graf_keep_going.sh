#!/bin/sh
if ps -ef | grep -v grep | grep influx_pox_loader.py ; then
        exit 0
else
        /home/pi/influx_pox_loader.py &
        exit 0
fi
