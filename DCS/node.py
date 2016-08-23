from pyroute2 import NetNS, IPDB, IPRoute
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class Node (object):

    def __init__(self, name):
        log.debug('Creating node %s'% name)
        self.name = name
        self.ns = NetNS(name)
        self.ipdb = IPDB(nl=self.ns)
        self.intfs = {}

    def __del__(self):
        # print('Deleting the node: ', self.name)
        try:
            self.ns.close()
            self.ns.remove()
            self.ipdb.release()
        except AttributeError as e:
            pass
        except:
            raise

    def add_intf(self, link, intf_name = None):
        if intf_name is None:
            intf_name = self.name + 'eth' + str(len(self.get_intfs()))

        self.intfs[intf_name] = link
        
        return intf_name

    def get_intf(self, intf_name):
        return self.intfs[intf_name]

    def get_intfs(self):
        return self.intfs


class Host(Node):
    pass


class Switch(Node):
    pass


class Router(Node):
    pass