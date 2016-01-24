# -*- coding: utf-8 -*-

from node import Node
from samples import sample1 as s1

if __name__ == "__main__":
    nd = Node
    lca1 = nd.lca(s1.n7, s1.n6)
    lca2 = nd.lca(s1.n5, s1.n4)
    lca3 = nd.lca(s1.n8, s1.n6)
    lca4 = nd.lca(s1.n9, s1.n4)
    print "LCA between 7 and 6 is %s" % lca1
    print "LCA between 5 and 4 is %s" % lca2
    print "LCA between 8 and 6 is %s" % lca3
    print "LCA between 9 and 4 is %s" % lca4
