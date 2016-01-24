# -*- coding: utf-8 -*-


class Node(object):
    """Node Class."""

    def __init__(self, value, parent=None):
        self._check_parent(parent)
        self.value = value
        self.parent = parent

    def _check_parent(self, parent):
        if parent and not isinstance(parent, type(self)):
            raise Warning("Parent must be an instance of Node class")

    def find_ancestors(self):
        """Return a list of ancestors values from lowest to root."""
        # self is also an ancestor
        ancestors = [self.value]
        parent = self.parent
        while parent:  # If no parent, it means we reached root
            ancestors.append(parent.value)
            parent = parent.parent
        return ancestors

    @staticmethod
    def lca(node1, node2):
        """Return value of Lowest Common Ancestor between two nodes"""
        ancestors1 = node1.find_ancestors()
        ancestors2 = node2.find_ancestors()
        # Determine shorter list to use for iteration
        if ancestors1 < ancestors2:
            anc_short = ancestors1
            anc_long = ancestors2
        else:
            anc_short = ancestors2
            anc_long = ancestors1
        for value in anc_short:
            if value in anc_long:
                return value
