#!/bin/bash
set -x

if [[ $1 == "" ]] | [[ $2 == "" ]]; then
    echo "Usage: ./user_add.sh username password"
    exit
fi

ret=false
getent passwd $1 >/dev/null 2>&1 && ret=true

if $ret; then
    echo "User Exists" >/dev/null 2>&1
else
     
    useradd -m -s /bin/bash -d /home/$1  $1 
    echo "$1:$2" | chpasswd   
    mkdir -p /home/$1
    chown -R $1 /home/$1    
fi
