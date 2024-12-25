"""implementation of stack using linked list"""

import node
import unorderedList

class StackLinkedList:

    def __init__(self):
        self.list = unorderedList.UnorderedList()

    def is_empty(self):
        return self.list.is_empty()

    def push(self, item):
        self.list.add(item)

    def pop(self):
        return self.list.remove(self.list.size() - 1)

    def peek(self):
        return self.list.head.data

    def size(self):
        return self.list.size()