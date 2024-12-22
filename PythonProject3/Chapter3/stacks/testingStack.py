import stacks

s = stacks.Stack()
s.push(10)
s.push(20)
s.push(30)

s.pop()
s.pop()
s.pop()
s.pop()
print(s.is_empty())