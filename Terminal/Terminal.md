# Speration Line

### awk

echo "iowjef owejfioooooooo wiefj fwe" | awk '{print $2}'
从1开始计数， $2 是第二个


awk -f
from file


# internet

## check the port usage

sudo lsof -i -P n | grep LISTEN


# system

## system information

uname

// x86_64
uname -m 

// Linux, Darwin
uname -s






## check the running status

htop


# user
id $USER
id user_name

## add group
newgrp docker

## modified group? 
sudo usermod -aG docker $USER

option:
-G = To add a supplementary groups.
-a = To add anyone of the group to a secondary group.

(what is group, supplementary groups, secondary group