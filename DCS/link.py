from pyroute2 import IPRoute
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class Link(object):
    def __init__(self, node_pair1=None, node_pair2=None):
        self.node_pair1 = node_pair1
        self.node_pair2 = node_pair2

    def add_node_pairs(self, node_pair1, node_pair2):
        self.node_pair1 = node_pair1
        self.node_pair2 = node_pair2

    def __del__(self):
        log.debug("TODO: Deleting the link pair!!")
        # ipr = IPRoute()
        # for link_id in ipr.link_lookup(ifname=self.node_pair1[1]):
        #     ipr.link('del', index=link_id)
        # for link_id in ipr.link_lookup(ifname=self.node_pair2[1]):
        #     ipr.link('del', index=link_id)
        # ipr.close()


class LinkDB(dict):
    def __init__(self, ipdb, *args, **kwargs):
        self.ipdb = ipdb
        dict.__init__(self,*args,**kwargs)
        self.update(*args, **kwargs)

    def __getitem__(self, key):
        n1, n2 = key
        
        if((n1, n2) in self.keys()):
            val = dict.__getitem__(self, (n1, n2))
        elif((n2, n1) in self.keys()):
            val = dict.__getitem__(self, (n2, n1))
        else:
            raise KeyError

        return val

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return ('%s(%s, %s)' % (type(self).__name__, self.ipdb, dictrepr))

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    def add_link(self, node1, node2):
        link = Link()

        node1_intf_name = node1.add_intf(link)
        node2_intf_name = node2.add_intf(link)

        self.ipdb.create(ifname=node1_intf_name,
                         kind='veth',
                         peer=node2_intf_name).commit()

        with self.ipdb.interfaces[node1_intf_name] as veth:
            veth.net_ns_fd = node1.name
        with self.ipdb.interfaces[node2_intf_name] as veth:
            veth.net_ns_fd = node2.name

        link.add_node_pairs((node1, node1_intf_name), 
                            (node2, node2_intf_name))
        self[(node1.name, node2.name)] = link
