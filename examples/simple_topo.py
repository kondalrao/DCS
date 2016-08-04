if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import IPython
from DCS.DCS import DCS
dcs = DCS()

dcs.add_node('n1')
dcs.add_node('n2')
dcs.add_link('n1', 'n2')


# drop into python shell
IPython.embed()