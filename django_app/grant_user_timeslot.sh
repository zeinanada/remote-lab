#!/bin/bash
set -x #-e



if [[ $1 == "" ]]  || [[ $2 == "" ]] || [[ $3 == "" ]] ; then
        echo "Usage: ./grant_user_nodes_timeslot.sh  username  start_date_time  end_date_time"
        echo "Date format is HH:MM CCYY-MM-DD"
        exit -1
fi


user_name=$1;
start_date_time=$2;
end_date_time=$3;
#echo $user_name  $start_date_time $end_date_time>> /home/crc-portal/userlog

grant_script="sudo /bin/sh ./grant_user_node.sh"
revoke_script="sudo /bin/bash ./revoke_user_all_nodes.sh"

#let diff=(`date +%s -d "$start_date_time"`-`date +%s`); echo $diff
#    if [[ diff -gt "0" ]]; then
#        echo "Start Date is in the future"
#        echo "$grant_script  $user_name"   | at "$start_date_time";
#        #at $start_date_time -f $grant_script;
#    else
#        echo "Start Date is in the past"
#        if [[ diff -lt "-3600" ]]; then
#            echo "Somethig is wrong date is too far in the past"
#        else
#            echo "$grant_script  $user_name"   | at "$start_date_time";
#        fi
#    fi


#echo "$revoke_script  $user_name" | at "$end_date_time";
#at $end_date_time -f $revoke_script;


echo "sudo /bin/sh ./grant_user_node.sh $1" | at $2
echo "sudo /bin/bash ./revoke_user_all_nodes.sh $1" | at $3

