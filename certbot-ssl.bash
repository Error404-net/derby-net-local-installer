#!/bin/bash

# install snapd
apt-get update
apt-get install -y snapd

snap install core
snap refresh core

# install certbot
apt remove -y certbot
snap install --classic certbot
ln -s /snap/bin/certbot /usr/bin/certbot

## request a tls/ssl certifiacte using certbot
# request a certificate and automatically configure it on nginx
certbot --nginx -d derbynet.pack1177.tk

# request a certificate without configuring nginx
# certbot certonly --nginx

