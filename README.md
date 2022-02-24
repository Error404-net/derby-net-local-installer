# Derbynet Local Installer

This is an install script to setup and install all of the componects for the derbynet server. I run this on a 1 core, 1 g of ram linode server and it seems to have enough power to support the cub scout pack. You will need other computers to set up the timmer and login to register the kids cars with the photo of the kids and the cars.


# Domain Registration
1. Register a free domain
   1. I used freenom to get a free domain
2. In Freenom add the 5 ns[1-5].linode.com nameservers with the management tool in freenom
3. Create a domain in Linode by clicking on domains on the left panel and create a new domain. A subdomain can be used here like example.example.com
   1. This will take up to 24 hours for the domain name to propagate to enough dns servers.

# SSL Certificate
1. Run `./certbot-ssl.bash`
   1. you will need to enter your domain once prompted. 