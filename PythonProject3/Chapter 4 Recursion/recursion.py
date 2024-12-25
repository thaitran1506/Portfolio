"""
The three laws of recursion
    1. a recursive algorithm must have a base case
    2. a recursive algorithm must change its state and move toward the base case
    3. a recursive algorithm must call itself
"""
"""
Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
"""
def reverse_string(string):
    if len(string) == 0:
        return string
    return string[-1] + reverse_string(string[:len(string)-1])

import turtle
def draw_spiral(my_turtle, length):

    if length <= 0:
        return
    my_turtle.forward(length)
    my_turtle.right(90)
    draw_spiral(my_turtle, length - 10)

def draw_tree(my_turtle, branch, angle):
    if branch == 0:
        return
    my_turtle.forward(branch)
    my_turtle.right(angle)
    draw_tree(my_turtle, branch - 10, angle)
    my_turtle.left(angle*2)
    draw_tree(my_turtle, branch - 10, angle)
    my_turtle.right(angle)
    my_turtle.backward(branch)

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_turtle.left(90)
my_turtle.penup()
my_turtle.backward(100)
my_turtle.pendown()
my_turtle.color('red')
draw_tree(my_turtle, 100, 30)
my_win.exitonclick()
