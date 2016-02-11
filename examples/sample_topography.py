#!/usr/bin/python

"""
This example shows how to create a simple real-world like network
using docker containers (based on existing images) and authentication.
"""
import sys
sys.path = ['/home/mininet/mininet_wifi_forked', '.'] + sys.path
import time
from mininet.net import Mininet, info
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

    image = 'ubuntu'
    cmd = '/bin/bash'

    print "*** Creating nodes"
    ap1 = net.addBaseStation( 'ap1', ssid="simplewifi", mode="g", channel="5", passwd='123456789a', encrypt='wpa2')

    sta1 = net.addStation( 'sta1', passwd='123456789a', encrypt='wpa2')
    sta2 = net.addStation( 'sta2', passwd='123456789ab', encrypt='wpa2')
    sta3 = net.addStation( 'sta3', passwd='123456789a', encrypt='wpa2')

    h1 = net.addHost('h1', cls=Docker, dimage=image, dcmd=cmd)
    h2 = net.addHost('h2', cls=Docker, dimage=image, dcmd=cmd)
    h3 = net.addHost('h3')

    h4 = net.addHost('h4', cls=Docker, dimage=image, dcmd=cmd)

    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633)

    s1 = net.addSwitch( 's1')
    s2 = net.addSwitch( 's2')

    print "*** Associating Stations"
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)

    net.addLink(h1, ap1)
    net.addLink(h2, ap1)
    net.addLink(h3, ap1)

    net.addLink(ap1, s1)
    net.addLink(s1, s2)

    net.addLink(s2, h4)

    print "*** Starting network"
    net.build()
    c0.start()
    ap1.start( [c0] )
    s1.start( [c0] )
    s2.start( [c0] )

    print "*** Running CLI"
    CLI(net)

    print "*** Stopping network"
    net.stop()
    system('sudo mn -c')
    system('docker stop $(docker ps -aq);docker rm $(docker ps -aq)')

if __name__ == '__main__':
    setLogLevel('info')
    topology()
