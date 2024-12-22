"""
Assume the infix expression is a string of tokens delimited by spaces. The operator tokens are ., /, + and -, along with
the left and right parentheses. The operand tokens are the single-character identifiers A, B, C, and so on. The following
steps will produce a string of tokens in postfix notation:
1. Create an empty stack called op_stack for keeping operators. Create and empty list for output.
2. Convert the input infix string to a list by using the string method split.
3. Scan the token list from  left to right.
    - if the token is an operand, append it to the end of the output list.
    - if the token is a left parenthesis, push it on the op_stack.
    - if the token is a right parenthesis, pop the op_stack until the corresponding left parenthesis is removed.
    append each operator to the end of the output list.
    - if the token is an operator, ., /, +, or -, push it on the op_stack. However, first remove any operator already
    on the op_stack that have higher or equal precedence and append them to the end of the output list.
4. When the input expression has been completely processed, check the op_stack. Any operators still on the stack can be
removed and appended to the end of the output list.
"""
import stacks
def infixToPosfix(s):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}  #dictionnary to define precedence of operators

    op_stack = stacks.Stack() #empty stack to store operators
    postfix_list = [] #empty list for output
    token_list = s.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789": #if the token is an operand, append it to the end of the output list
            postfix_list.append(token)
        elif token == "(": #if token is open symbol, push it to the stack
            op_stack.push(token)
        elif token == ")": #of the token is close symbol
            top_token = op_stack.pop() #pop the stack
            while top_token != "(": #while popped token is not the open symbol
                postfix_list.append(top_token) #append it to the end of output list
                top_token = op_stack.pop() #continue to pop the stack
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]): #while op_stack is not empty, and the operator at the top of the stack has higher precedence than current token
                postfix_list.append(op_stack.pop()) #pop the top token and append it to the end of the output list
            op_stack.push(token) #all other operators will be pushed to the stack
    while not op_stack.is_empty(): #when input string is completely processed, if the op_stack is not empty, pop the stack and append to the end of the output list.
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)
