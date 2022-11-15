from mininet.topo import Topo


class BinaryTreeTopo(Topo):

    def __init__(self):
        #Initialize topology
        Topo.__init__(self)
        # Add hosts
        host = []
        for i in range(1, 9):
            host.append(self.addHost("h" + str(i)))

        # Add switches
        switch = []
        for j in range(1, 8):
            switch.append(self.addSwitch('s' + str(j)))
        # add links
        self.addLink(switch[1], switch[2])
        self.addLink(switch[1], switch[5])
        self.addLink(switch[2], switch[3])
        self.addLink(switch[2], switch[4])
        self.addLink(switch[5], switch[6])
        self.addLink(switch[5], switch[7])
        self.addLink(switch[3], host[1])
        self.addLink(switch[3], host[2])
        self.addLink(switch[4], host[3])
        self.addLink(switch[4], host[4])
        self.addLink(switch[6], host[5])
        self.addLink(switch[6], host[6])
        self.addLink(switch[7], host[7])
        self.addLink(switch[7], host[8])


topos = {'binary_tree': (lambda: BinaryTreeTopo())}
