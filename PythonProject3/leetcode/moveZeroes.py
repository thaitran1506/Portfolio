"""
Move Zeroes

Problem: Move all zeroes in an array to the end while maintaining the relative order of non-zero elements.
Hint: Use two pointers to swap non-zero and zero elements.
Source: LeetCode 283
"""

def move_zeroes(a):
    if len(a) == 0:
        return []
    i = 0
    for j in range(1, len(a)):
        if a[j] != 0:
            a[i], a[j] = a[j], a[i]
            i += 1

a = [0, 1, 0, 3, 12]
print(a)
move_zeroes(a)
print(a)