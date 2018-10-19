"""
Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Lab05 Topology"

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        topLeftHost = self.addHost( 'h1' )
        topRightHost = self.addHost( 'h2' )
        bottomLeftHost = self.addHost( 'h3' )
        bottomRightHost = self.addHost( 'h4' )
        leftSwitch = self.addSwitch( 'sw1' )
        rightSwitch = self.addSwitch( 'sw2' )

        # Add links
        self.addLink( topLeftHost, leftSwitch )
        self.addLink( bottomRightHost, leftSwitch)
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( topRightHost, rightSwitch )
        self.addLink( bottomRightHost, rightSwitch )


topos = { 'mytopo': ( lambda: MyTopo() ) }
