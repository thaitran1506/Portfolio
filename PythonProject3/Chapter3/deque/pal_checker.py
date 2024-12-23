""""
Palindrome is a string that reads the same forwards and backwards. We want to create an algorithm to
input a string of characters and check whether it is palindrome or not.
We will use a deque to store the characters of the string.
Process the string from left to right and add each character to the rear of the deque
Make use of the dual functionality of the deque.
The front of the deque will hold the first character of the string and the rear of the deque
will hold the last character.
Since we can remove both of the front and rear characters directly, we can compare them and continue
only if they match.
If we can continue matching first and last items, we will eventually run out of characters or be left
with a deque of size 1 depending on the size of the string.
In either case the string must be a palindrome.
"""
import Deque

def pal_checker(string):
    #create an empty deque
    deque = Deque.Deque()
    #process the string from left to right and add character to the rear of the deque
    for char in string:
        deque.add_rear(char)

    while deque.size() > 1:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            return False
    return True

print(pal_checker('abba'))