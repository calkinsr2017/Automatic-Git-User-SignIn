#!/bin/bash

read -e -p "Enter email address: " emailAddress
read -e -p "Enter your name (all caps): " name
echo "NOTE: Remember, file saved as id_rsa_YOURNAME"
cd ~/.ssh
ssh-keygen -t rsa -N "" -f "id_rsa_$name"

if [ ! -d ~/.ssh/ ]
then
    echo "SSH path does not exist! Creating .ssh folder"
    cd ~
    mkdir .ssh
fi

if [ ! -e ~/.ssh/config ]
then
    echo "You do not have a config file! making one."
    cd ~/.ssh
    touch config
	
    configFile=~/.ssh/config
    /bin/cat << EOM >$configFile

Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa
EOM
fi

configFile=~/.ssh/config
/bin/cat << PEOM >>$configFile
Host github-$name
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_$name
PEOM
   
   
eval `ssh-agent -s`

echo "After you run this script, call the quick-set-user.sh script to your own information!"
