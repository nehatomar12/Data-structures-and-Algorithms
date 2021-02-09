"""
Given an array C of size N-1 and
given that there are numbers from 1 to N with one element missing,
the missing number is to be found.

Input:
    5
    1 2 3 5
    10
    1 2 3 4 5 6 7 8 10

Output:
    4
    9
"""

given_arr = [1,2,3,5]
original_arr = list(range(given_arr[-1]+1))
print((list(set(original_arr) ^ set(given_arr))[-1]))
