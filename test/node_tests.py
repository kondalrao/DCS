from nose.tools import *
from DCS.node import Node
import subprocess

class TestNode(object):
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_node_exception(self):
        with assert_raises(TypeError):
            node = Node()

    def test_node_creation(self):
        node1 = Node('n1')
        node2 = Node('n2')
        cmd = subprocess.Popen(["ip", "netns", "list"], stdout=subprocess.PIPE)
        netns_list = cmd.stdout.read()
        eq_(netns_list.split(), [b'n2', b'n1'])
