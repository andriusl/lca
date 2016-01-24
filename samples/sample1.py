# -*- coding: utf-8 -*-

from node import Node as nd

# Create sample nodes tree

root = nd(1)
# Left
n2 = nd(2, root)
n5 = nd(5, n2)
n4 = nd(4, n2)
n9 = nd(9, n4)
n8 = nd(8, n4)
# Right
n3 = nd(3, root)
n6 = nd(6, n3)
n7 = nd(7, n3)

# Second nodes tree

nn1 = nd(1)
nn2 = nd(2, nn1)
