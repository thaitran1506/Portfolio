"""
The basic building block for the linked list implementation is the node. Each node object must hold
at least 2 pieces of information. First the node must contain the list item itself - the data field.
In addition, each node must hold a reference to the next node.
To construct a node, you need to supply the initial value for the node.
Hidden fields _data and _next of the Node class are turned into properties and can be accessed
as data and next respectively
"""
class Node:
    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        #get node data
        return self._data
    def set_data(self, node_data):
        """set node data"""
        self._data = node_data
    data = property(get_data, set_data)

    def get_next(self):
        """get next node"""
        return self._next

    def set_next(self, node_next):
        """set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String representation of the node"""
        return str(self._data)