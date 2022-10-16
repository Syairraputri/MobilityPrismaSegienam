#!/usr/bin/env python

import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology(args):

    net = Mininet_wifi()

    info("* Creating nodes\n")
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8' )
    sta1 = net.addStation( 'sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', range='20' )
    sta2 = net.addStation( 'sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', range='20' )
    sta3 = net.addStation( 'sta3', mac='00:00:00:00:00:04', ip='10.0.0.4/8', range='20' )
    sta4 = net.addStation( 'sta4', mac='00:00:00:00:00:05', ip='10.0.0.5/8', range='20' )

    ap1 = net.addAccessPoint( 'ap1', ssid= 'ap1-ssid', mode= 'g', channel= '1', position='60,20,0', range='30' )
    ap2 = net.addAccessPoint( 'ap2', ssid= 'ap2-ssid', mode= 'g', channel= '1', position='100,20,0', range='30' )
    ap3 = net.addAccessPoint( 'ap3', ssid= 'ap3-ssid', mode= 'g', channel= '1', position='120,40,0', range='30' )
    ap4 = net.addAccessPoint( 'ap4', ssid= 'ap4-ssid', mode= 'g', channel= '1', position='100,60,0', range='30' )
    ap5 = net.addAccessPoint( 'ap5', ssid= 'ap5-ssid', mode= 'g', channel= '1', position='60,60,0', range='30' )
    ap6 = net.addAccessPoint( 'ap6', ssid= 'ap6-ssid', mode= 'g', channel= '1', position='40,40,0', range='30' )
    ap7 = net.addAccessPoint( 'ap7', ssid= 'ap7-ssid', mode= 'g', channel= '1', position='60,120,0', range='30' )
    ap8 = net.addAccessPoint( 'ap8', ssid= 'ap8-ssid', mode= 'g', channel= '1', position='100,120,0', range='30' )
    ap9 = net.addAccessPoint( 'ap9', ssid= 'ap9-ssid', mode= 'g', channel= '1', position='120,140,0', range='30' )
    ap10 = net.addAccessPoint( 'ap10', ssid= 'ap10-ssid', mode= 'g', channel= '1', position='100,160,0', range='30' )
    ap11 = net.addAccessPoint( 'ap11', ssid= 'ap11-ssid', mode= 'g', channel= '1', position='60,160,0', range='30' )
    ap12 = net.addAccessPoint( 'ap12', ssid= 'ap12-ssid', mode= 'g', channel= '1', position='40,140,0', range='30' )
    c1 = net.addController( 'c1' )
	
    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating and Creating links\n")
    net.addLink(ap1, h1)
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, ap5)
    net.addLink(ap5, ap6)
    net.addLink(ap6, ap1)
    net.addLink(ap1, ap7)
    net.addLink(ap2, ap8)
    net.addLink(ap3, ap9)
    net.addLink(ap4, ap10)
    net.addLink(ap5, ap11)
    net.addLink(ap6, ap12)
    net.addLink(ap7, ap8)
    net.addLink(ap8, ap9)
    net.addLink(ap9, ap10)
    net.addLink(ap10, ap11)
    net.addLink(ap11, ap12)
    net.addLink(ap7, ap12)
    
    if '-p' not in args:
        net.plotGraph(max_x=200, max_y=200)
 
    net.startMobility(time=0, ac_method= 'ssf')
    net.mobility(sta1,'start', time=1, position='0,75,0')
    net.mobility(sta1,'stop', time=2, position='80,80,0')
    net.stopMobility(time=5)

    net.startMobility(time=0, ac_method= 'ssf')
    net.mobility(sta2, 'start', time=1, position='80,0,0')
    net.mobility(sta2, 'stop', time=2, position='80,80,0')
    net.stopMobility(time=5)
    
    net.startMobility(time=0, ac_method= 'ssf')
    net.mobility(sta3, 'start', time=1, position='80,160,0')
    net.mobility(sta3, 'stop', time=2, position='80,80,0')
    net.stopMobility(time=5)  
    
    net.startMobility(time=0, ac_method= 'ssf')
    net.mobility(sta4, 'start', time=1, position='160,80,0')
    net.mobility(sta4, 'stop', time=2, position='80,80,0')
    net.stopMobility(time=5)
    
    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])
    ap5.start([c1])
    ap6.start([c1])
    ap7.start([c1])
    ap8.start([c1])
    ap9.start([c1])
    ap10.start([c1])
    ap11.start([c1])
    ap12.start([c1])


    info("*** Running CLI\n")
    CLI( net )

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology(sys.argv)
