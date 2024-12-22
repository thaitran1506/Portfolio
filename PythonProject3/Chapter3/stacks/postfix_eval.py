"""
Assume the postfix expression is a string of tokens delimited by spaces. The operators are ., /, +, and - and the
operands are assumed to be single-digit integer values. The output will be an integer result.
1. create an empty stack called operand_stack
2. convert the string to a list by the string method split
3. scan the token list from left to right
    - if the token is an operand, convert it from a string to an integer and push the value onto the operand_stack
    - if the token is an operator, ., /, +, or -, it will need two operands. Pop the operand_stack twice. The first pop
    is the second operand and the second pop is the first operand. Perform the arithmetic operation. Push the result back
    on the operand_stack.
4. When the input expression is completely processed, the result is on the stack. Pop the operand_stack and return the value
"""
import stacks
def postfix_eval(expression):
    operand_stack = stacks.Stack() #empty stack to hold operand
    token_list = expression.split() #convert postfix expression to a list

    for token in token_list: #scan the list of tokens
        if token.isdigit(): #if token is a digit
            operand_stack.push(int(token)) # push the token to the operand_stack
        else: #if tokens are operators, each operator needs 2 operands, pop the operand_stack twice
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2) #do math with the two operands and the corresponding operator
            operand_stack.push(result) #push the value back to the stack
    return operand_stack.pop() #the final stack should only have one value, return it

def do_math(token, operand1, operand2):
    if token == "+":
        return operand1 + operand2
    elif token == "-":
        return operand1 - operand2
    elif token == "/":
        return operand1 / operand2
    elif token == "*":
        return operand1 * operand2


print(postfix_eval("1 2 +"))
