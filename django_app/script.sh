#!/bin/bash

#kill $(ps aux | grep '[m]otion' | awk '{print $2}')

#ps -ef | grep  motion | grep -v grep | awk '{print $2}' | xargs kill

#if pgrep motion; then pkill motion; fi


if pgrep motion
then
echo "motion running "
#kill -9 $(ps | grep "motion" | grep -v grep | awk '{ print $1 }')
killall motion
echo "motion  got killed"
else
echo "motion is not running"
fi

