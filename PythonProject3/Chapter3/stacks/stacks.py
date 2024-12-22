'''
Stacks are ordered from top to bottom. Items are added and removed at the top of the stack. Stacks are ordered last
in first out.
Stacks operations are as follows:
- Stack() creates a new empty stack. If no given parameter, a new empty stack will be created.
- push(item) adds item to the top of the stack.
- pop() removes item from the top of the stack and returns it. It needs no parameter. Stack is modified in-place.
- peek() returns the item at the top of the stack. Does not modify the stack itself. If stack is empty, returns None.
- is_empty() returns True if stack is empty, False otherwise.
- size() returns the number of items in the stack. Needs no parameter and return an integer.
'''
class Stack:
    """Stack implementation as a list of items."""
    def __init__(self):
        """Create a new empty stack."""
        self.items = []

    def push(self, item):
        """Add item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack. If stack is empty, returns None."""

        if self.is_empty():
            return None

        return self.items.pop()

    def peek(self):
        """Return the item at the top of the stack."""
        return self.items[-1]

    def is_empty(self):
        """Return True if stack is empty, False otherwise."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """Return a string representation of the stack."""
        return str(self.items)

    def __repr__(self):
        """Return a string representation of the stack."""
        return str(self.items)



