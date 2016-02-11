import sys
sys.path = ['/home/mininet/mininet_wifi_forked', '.'] + sys.path
import time
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Docker
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink
from os import system

def topology():
    "Create a network."
    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding docker containers\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.250', cls=Docker, dimage="ubuntu" )
    h2 = net.addHost( 'h2', ip='10.0.0.251', cls=Docker, dimage="ubuntu" )
    h3 = net.addHost( 'h3', ip='10.0.0.252', cls=Docker, dimage="ubuntu" )
    h4 = net.addHost( 'h4', ip='10.0.0.253', cls=Docker, dimage="ubuntu" )
    h5 = net.addHost( 'h5', ip='10.0.0.254', cls=Docker, dimage="ubuntu" )
    h6 = net.addHost( 'h6', ip='10.0.0.249', cls=Docker, dimage="ubuntu" )

    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1')
    s2 = net.addSwitch( 's2')
    s3 = net.addSwitch( 's3')

    info( '*** Creating links\n' )
    net.addLink( h1, s1 )
    net.addLink( s1, h2 )

    net.addLink( h3, s2 )
    net.addLink( h4, s2 )

    net.addLink( h5, s3 )
    net.addLink( h6, s3 )

    net.addLink( s1, s3 )
    net.addLink( s2, s3 )


    info( '*** Starting network\n')
    net.start()

    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
