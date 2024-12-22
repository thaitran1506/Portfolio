"""
Using stack to solve real computer science problems.
Parentheses must appear in balanced fashion. Each opening symbol has a corresponding closing symbol, and the pairs are
properly nested.
The challenge then is write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced.
As you process symbols from left to right, the most recent opening parenthesis must match the next closing symbol.
First opening may have to wait until the very last symbol for it to match.
Closing symbols match opening symbols in the reverse order of their appearance, they match from inside out. this is a clue that stacks can be used to solve the problem.

starting with an empty stack. Process the parentheses from left to right. If the symbol is opening parenthesis, push it to the stack.
If on the other hand, the symbol is closing parenthesis, pop the stack.
If the string of parentheses is balanced, the final stack should be empty. If there is any item left in the stack, the string is not balanced.
"""
import stacks
def par_checker(string):
    """create an empty stack"""
    stack = stacks.Stack()
    """iterate through the string, if the symbol is opening parenthesis, push it to the stack. Otherwise, if the stack is empty, return false. Otherwise pop the stack"""
    for char in string:
        if char == '(':
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()


    if stack.is_empty():
        return True
    else:
        return False


print(par_checker('('))