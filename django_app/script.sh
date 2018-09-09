#!/bin/bash


if pgrep motion
then
echo "motion running "
killall motion
echo "motion  got killed"
else
echo "motion is not running"
fi

