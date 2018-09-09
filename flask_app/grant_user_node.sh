#!/bin/bash
#unlock user account with ssh access
passwd -u $1
runuser -l $1 -c 'xpra start --start=terminator --html=on --bind-tcp=localhost:8088 --daemon=yes --pulseaudio=no --mdns=no --clipboard=yes --clipboard-direction=both --encoding=jpeg --printing=no;  motion -c /home/zeinanada/Desktop/Cairo University/Django examples/loggingsite/conf2 '
if [[ $1 == "" ]]  ; then
        echo "Usage: ./grant_user_nodes.sh  username "
        exit -1
fi

echo you are in grant_user_nodes > grantllog2

echo hello $1 > hello.txt
USER_NAME=$1
user_exists=$(id -u $USER_NAME )
if  [ -z "$user_exists" ]; then
    exit -1
fi



#
