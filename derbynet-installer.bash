#!/bin/bash

# assumes that we are root

# Update all packages
apt-get update && apt-get -y dist-upgrade && apt-get -y dist-upgrade

apt-get install -y apt-transport-https git

wget -q -O- https://jeffpiazza.org/derbynet/debian/jeffpiazza_derbynet.gpg | \
tee /usr/share/keyrings/derbynet-archive-keyring.gpg

echo "deb [arch=all signed-by=/usr/share/keyrings/derbynet-archive-keyring.gpg] " \
" https://jeffpiazza.org/derbynet/debian stable main" | \
tee /etc/apt/sources.list.d/derbynet.list > /dev/null

apt-get update

# install derbynet server
apt-get install -y derbynet-server

# remove apache if installed since derbynet is dependet on nginx
apt-get remove -y apache2