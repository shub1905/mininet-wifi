#!/usr/bin/python

"""
This example shows how to create a simple network and
how to create docker containers (based on existing images)
to it.
"""

from mininet.net import Dockernet
from mininet.node import Controller, Docker, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Link


def dockerNet():

    "Create a network with some docker containers acting as hosts."

    net = Dockernet(controller=Controller)

    info('*** Adding controller\n')
    net.addController('c0')

    info('*** Adding hosts\n')
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')

    info('*** Adding docker containers\n')
    d1 = net.addDocker('d1', ip='10.0.0.251', dimage="ubuntu")
    d2 = net.addDocker('d2', ip='10.0.0.252', dimage="ubuntu")

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(s1, d1)
    net.addLink(h2, s2)
    net.addLink(d2, s2)
    net.addLink(s1, s2)

    info('*** Starting network\n')
    net.start()

    net.ping([d1, d2])

    net.ping([d1], manualdestip="10.0.0.252")
    net.ping([d2, d3], manualdestip="11.0.0.254")

    info('*** Dynamically add a container at runtime\n')
    d4 = net.addDocker('d4', dimage="ubuntu")
    # we have to specify a manual ip when we add a link at runtime
    net.addLink(d4, s1, params1={"ip": "10.0.0.254/8"})

    net.ping([d1], manualdestip="10.0.0.254")

    info('*** Running CLI\n')
    CLI(net)

    info('*** Stopping network')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    dockerNet()