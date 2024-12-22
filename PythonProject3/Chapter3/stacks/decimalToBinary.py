"""
Converts a decimal number to a binary number. Use floor division to divide a decimal number by 2 until the result is equal to 0.
Use stack to keep track of the remainder of the division.
return the result by popping the stack from top to bottom
"""
import stacks
def decimalToBinary(decimal_num):
    stack_remainder = stacks.Stack()

    while decimal_num > 0:
        stack_remainder.push(decimal_num % 2)
        decimal_num = decimal_num // 2
    binary_string = ""
    while not stack_remainder.is_empty():
        binary_string += str(stack_remainder.pop())

    return binary_string
print(decimalToBinary(9))


