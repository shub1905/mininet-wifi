#!/usr/bin/python

"""
This example shows how to work with authentication.
"""
import sys
sys.path = ['/home/mininet/forked_mininet', '.'] + sys.path
import pydevd, time
from mininet.net import Mininet
from mininet.node import  Controller, OVSKernelSwitch, Docker
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )

    # image = 'shub1905/chaos:hostapd_latest'
    # image2 = 'shub1905/ubuntu:updated_wpa'
    # cmd = '/bin/ash'
    # cmd2 = '/bin/bash'

    print "*** Creating nodes"
    sta1 = net.addStation( 'sta1', ip='10.0.0.1', passwd='123456789a', encrypt='wpa2', cls=Docker, dimage=image2, dcmd=cmd2 )
    sta2 = net.addStation( 'sta2', ip='10.0.0.2', passwd='12346789a', encrypt='wpa2', cls=Docker, dimage=image2, dcmd=cmd2 )
    sta3 = net.addStation( 'sta3', ip='10.0.0.3', passwd='123456789a', encrypt='wpa2', cls=Docker, dimage=image2, dcmd=cmd2 )

    # sta1 = net.addStation( 'sta1', passwd='123456789a', encrypt='wpa2' ) #encrypt=(wpa,wpa2,wep)
    # sta2 = net.addStation( 'sta2', passwd='123456789a', encrypt='wpa2' ) #encrypt=(wpa,wpa2,wep)
    ap1 = net.addBaseStation( 'ap1', ssid="simplewifi", mode="g", channel="5", passwd='123456789a', encrypt='wpa2' ) #encrypt=(wpa,wpa2,wep)

    c0 = net.addController('c0', controller=Controller, ip='127.0.0.1', port=6633 )

    print "*** Associating Stations"
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)
    net.addLink(sta3, ap1)

    print "*** Starting network"
    net.build()
    c0.start()
    ap1.start( [c0] )

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    # pydevd.settrace('160.39.171.55', port=21000, stdoutToServer=True, stderrToServer=True)
    topology()


