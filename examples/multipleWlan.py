#!/usr/bin/python

"""
   Topology:  ap1<---->sta1<---->sta2
"""

from mininet.net import Mininet
from mininet.node import  OVSKernelSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink


def topology():
    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    sta1 = net.addStation( 'sta1', wlans=3 ) # 3 wlan added
    sta2 = net.addStation( 'sta2' ) # 1 wlan added
    ap1 = net.addBaseStation( 'ap1', ssid="ssid_1", mode="g", channel="5" ) # 1 wlan added
    c0 = net.addController('c0', controller=Controller)

    print "*** Associating..."
    net.addLink(ap1, sta1)

    net.addHoc(sta1, ssid='adhoc1', mode='g')
    net.addHoc(sta2, ssid='adhoc1', mode='g')

    print "*** Starting network"
    net.build()
    c0.start()
    ap1.start( [c0] )

    print "***Addressing..."
    sta1.cmd('ifconfig sta1-wlan1 192.168.10.1')
    sta2.cmd('ifconfig sta2-wlan0 192.168.10.2')

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

