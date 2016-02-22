###About Mininet-WiFi
Mininet-WiFi is a fork of [Mininet-WiFi](https://github.com/intrig-unicamp/mininet-wifi) which allows the emulation of differnet network topologies using both WiFi Stations and Access Points and virtual ethernet. This project augments original [Mininet](https://github.com/mininet/mininet) with functionality to create different network configurations using [Docker](https://www.docker.com/) Containers as their hosts.  

##Installation  
To setup a basic installation of this project follow these steps:  
1: $ sudo apt-get install git  
2: $ git clone https://github.com/shub1905/mininet-wifi  
3: $ cd mininet-wifi  
4: $ sudo util/install.sh -Wnfv  
5: $ pip install docker-py  

###Example  
To run a sample example spawning a simple wifi authenticated network with multiple host and am access point.  
1. $ cd examples  
2. $ sudo python wifiAuthentication.py  

###Author
Shubham Bansal (shubham.bansal@columbia.edu)  