#!/usr/bin/python

"""
This example shows how to work with authentication.
"""
import sys
sys.path = ['/home/mininet/mininet_wifi_forked', '.'] + sys.path
import pydevd
import time
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, Docker
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
from os import system


def topology():
    "Create a network."
    net = Mininet( controller=Controller )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    image = 'shub1905/chaos:noNet'
    # image2 = 'shub1905/ubuntu:updated_wpa'
    image2 = 'ubuntu'
    # cmd = '/bin/ash'
    cmd2 = '/bin/bash'

    print "*** Creating nodes"
    h1 = net.addHost('h1', ip='10.0.0.1', cls=Docker, dimage=image2, dcmd=cmd2)
    h2 = net.addHost('h2', ip='11.0.0.2', cls=Docker, dimage=image2, dcmd=cmd2)
    d1 = net.addHost('d1', ip='10.0.0.3', cls=Docker, dimage=image, dcmd=cmd)

    h3 = net.addHost('h3', ip='9.0.0.1', cls=Docker, dimage=image2, dcmd=cmd2)
    h4 = net.addHost('h4', ip='12.0.0.2', cls=Docker, dimage=image2, dcmd=cmd2)
    d2 = net.addHost('d2', ip='9.0.0.3', cls=Docker, dimage=image, dcmd=cmd)

    d3 = net.addHost('d3', ip='9.0.0.1', cls=Docker, dimage=image, dcmd=cmd)

    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633)

    print "*** Associating Stations"
    net.addLink(h1, d1)
    net.addLink(d1, h2)

    net.addLink(h3, d2)
    net.addLink(h4, d2)

    net.addLink(d1, d3)
    net.addLink(d2, d3)

    print "*** Starting network"
    net.build()
    c0.start()

    d1.cmd('ifconfig d1-eth1 11.0.0.4 netmask 255.0.0.0')
    d1.cmd('iptables -I OUTPUT -j ACCEPT')
    d1.cmd('iptables -I INPUT -j ACCEPT')
    d1.cmd('iptables -I FORWARD -j ACCEPT')
    
    h1.cmd('route add default gw 10.0.0.1')
    h1.cmd('route add -net 11.0.0.0 netmask 255.0.0.0 gw 11.0.0.4')
    h1.cmd('route add -net 7.0.0.0 netmask 255.0.0.0 gw 7.0.0.1')
    h1.cmd('route add -net 8.0.0.0 netmask 255.0.0.0 gw 7.0.0.1')
    
    h2.cmd('route add default gw 11.0.0.2')
    h2.cmd('route add -net 10.0.0.0 netmask 255.0.0.0 gw 10.0.0.3')
    h2.cmd('route add -net 7.0.0.0 netmask 255.0.0.0 gw 7.0.0.1')
    h2.cmd('route add -net 8.0.0.0 netmask 255.0.0.0 gw 7.0.0.1')

    d2.cmd('ifconfig d2-eth1 12.0.0.4 netmask 255.0.0.0')
    d2.cmd('iptables -I OUTPUT -j ACCEPT')
    d2.cmd('iptables -I INPUT -j ACCEPT')
    d2.cmd('iptables -I FORWARD -j ACCEPT')

    h3.cmd('route add default gw 9.0.0.1')
    h3.cmd('route add -net 12.0.0.0 netmask 255.0.0.0 gw 12.0.0.4')
    h3.cmd('route add -net 8.0.0.0 netmask 255.0.0.0 gw 8.0.0.1')
    h3.cmd('route add -net 7.0.0.0 netmask 255.0.0.0 gw 8.0.0.1')

    h4.cmd('route add default gw 12.0.0.2')
    h4.cmd('route add -net 9.0.0.0 netmask 255.0.0.0 gw 9.0.0.3')
    h4.cmd('route add -net 8.0.0.0 netmask 255.0.0.0 gw 8.0.0.1')
    h4.cmd('route add -net 7.0.0.0 netmask 255.0.0.0 gw 8.0.0.1')

    d1.cmd('ifconfig d1-eth2 7.0.0.1 netmask 255.0.0.0')
    d1.cmd('route add default gw 7.0.0.1')
    # d1.cmd('route add -net 8.0.0.0 netmask 255.0.0.0 gw 7.0.0.2')
    d2.cmd('ifconfig d2-eth2 8.0.0.1 netmask 255.0.0.0')
    d2.cmd('route add default gw 8.0.0.1')
    # d2.cmd('route add -net 7.0.0.0 netmask 255.0.0.0 gw 8.0.0.2')

    d3.cmd('ifconfig d3-eth0 7.0.0.2 netmask 255.0.0.0')
    d3.cmd('ifconfig d3-eth1 8.0.0.2 netmask 255.0.0.0')
    
    d3.cmd('route add -net 10.0.0.0 netmask 255.0.0.0 gw 7.0.0.1')
    d3.cmd('route add -net 11.0.0.0 netmask 255.0.0.0 gw 7.0.0.1')
    d3.cmd('route add -net 7.0.0.0 netmask 255.0.0.0 gw 7.0.0.1')
    d3.cmd('route add -net 9.0.0.0 netmask 255.0.0.0 gw 8.0.0.1')
    d3.cmd('route add -net 12.0.0.0 netmask 255.0.0.0 gw 8.0.0.1')
    d3.cmd('route add -net 8.0.0.0 netmask 255.0.0.0 gw 8.0.0.1')

    print "*** Running CLI"
    CLI(net)

    print "*** Stopping network"
    net.stop()
    system('sudo mn -c')

if __name__ == '__main__':
    setLogLevel('info')
    # pydevd.settrace('160.39.170.221', port=21000, stdoutToServer=True, stderrToServer=True)
    topology()
