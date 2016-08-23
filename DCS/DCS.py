
from pyroute2 import IPDB
from .node import Node, Host, Switch, Router
from .link import LinkDB
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class DCS(object):
    def __init__(self):
        self._ipdb = IPDB()
        self.linkdb = LinkDB(self._ipdb) 
        self.nodes = {}

    def get_ipdb(self):
        return self._ipdb

    def add_node(self, name):
        node = Node(name)
        self.nodes[name] = node
        return node

    def del_node(self, name):
        node = self.nodes.pop(name)
        del node

    def get_node(self, name):
        return self.nodes[name]
    
    def get_nodes(self):
        return self.nodes.keys()

    def add_host(self, name):
        host = Host(name)
        self.nodes[name] = host
        return host
        
    def add_link(self, node1, node2):
        self.linkdb.add_link(self.get_node(node1), self.get_node(node2))

    def del_link(self, node1, node2):
        pass

    def get_link(self, node1, node2):
        pass

    def get_links(self):
        return self.linkdb.keys()
