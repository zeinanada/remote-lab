#!/bin/bash
set -x #-e
LOG=""
if [[ $1 == "" ]]  ; then
        echo "Usage: ./revoke_user_nodes.sh  username"
        exit -1
fi

USER_NAME=$1
user_exists=$(id -u $USER_NAME )
if  [ -z "$user_exists" ]; then
    exit -1
fi
#Hist_Bit_Dir=/home/crc-users/bitstream_history/$USER_NAME
#User_Bit_Dir=/home/crc-users/$USER_NAME/tempbits/
#Bit_Default_Dir=/home/crc-user/tempbits/
#get all processes and kill
pgrep -u $USER_NAME | xargs -n1 kill
#lock user access
passwd -l $USER_NAME

#folder_name="$USER_NAME-`date +%d.%m.%Y-%H.%M.%S`"
#mkdir -p $Hist_Bit_Dir/$folder_name
#cp -f $User_Bit_Dir/* $Hist_Bit_Dir/$folder_name
##copy only the difference in files between crc-user/tempbits and user tempbits directory to tempbits directory
#diff -q $Bit_Default_Dir $User_Bit_Dir | grep "Only in $User_Bit_Dir*" | cut -d " " -f4 | xargs -n1 -I %  echo cp -r -v $User_Bit_Dir% $Hist_Bit_Dir$folder_name/ | bash

