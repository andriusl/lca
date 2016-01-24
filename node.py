# -*- coding: utf-8 -*-


class Node(object):
    """Node Class."""
    instances = {}

    def __init__(self, value, parent=None):
        instances = Node.instances
        if parent:
            self._check_parent(parent)
            # Get root node
            root = parent._get_root()
            # We check value if it is unique in given tree
            Node._check_value(value, root)
            instances[root].append(value)
        else:
            instances[self] = [value]
        self.value = value
        self.parent = parent

    def _check_parent(self, parent):
        if not isinstance(parent, type(self)):
            raise Warning("Parent must be an instance of Node class")

    @classmethod
    def _check_value(cls, value, root):
        if value in cls.instances[root]:
            raise Warning("Value must be unique per nodes tree")

    def _get_parent(self):
        """Return parent node. Should be called only if parent exists."""
        return self.parent

    def _get_root(self):
        parent = self
        while parent.parent:
            parent = parent._get_parent()
        return parent

    def find_ancestors(self):
        """Return a list of ancestors values from lowest to root."""
        # self is also an ancestor
        ancestors = [self.value]
        parent = self.parent
        while parent:  # If no parent, it means we reached root
            ancestors.append(parent.value)
            parent = parent._get_parent()
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
