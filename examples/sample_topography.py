#!/usr/bin/python

"""
This example shows how to work with authentication.
"""
import sys
sys.path = ['/home/mininet/mininet_wifi_forked', '.'] + sys.path
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

    images = ['ubuntu','fedora']
    cmd = '/bin/bash'

    print "*** Creating nodes"
    ap1 = net.addBaseStation( 'ap1', ssid="simplewifi", mode="g", channel="5" )

    sta1 = net.addStation('sta1', ip='10.0.0.1/24' )
    sta2 = net.addStation('sta2', ip='10.0.0.2/24' )
    sta3 = net.addStation('sta3', ip='10.0.0.3/24' )

    h1 = net.addHost('h1', ip='10.0.0.4', cls=Docker, dimage=image[0], dcmd=cmd)
    h2 = net.addHost('h2', ip='10.0.0.5', cls=Docker, dimage=image[0], dcmd=cmd)
    h3 = net.addHost('h3', ip='10.0.0.6')

    h4 = net.addHost('h4', ip='10.0.0.7', cls=Docker, dimage=image[1], dcmd=cmd)

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
    net.addLink(s2, s1)

    net.addLink(s2, h4)

    print "*** Starting network"
    net.build()
    c0.start()

    print "*** Running CLI"
    CLI(net)

    print "*** Stopping network"
    net.stop()
    system('sudo mn -c')

if __name__ == '__main__':
    setLogLevel('info')
    # pydevd.settrace('160.39.170.221', port=21000, stdoutToServer=True, stderrToServer=True)
    topology()
