import stacks
def balance_checker(string):
    #Create an empty stack
    stack = stacks.Stack()

    #iterate through the string from left to right, if the character is an opening symbol, push it to the stack
    for char in string:
        if char in "([{":
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            else:
                if not matches(stack.pop(), char):
                    return False
    return stack.is_empty()

def matches(a, b):
    opening_bracket = "([{"
    closing_bracket = ")]}"
    return opening_bracket.index(a) == closing_bracket.index(b)

if __name__ == "__main__":
    print(balance_checker("}]"))
