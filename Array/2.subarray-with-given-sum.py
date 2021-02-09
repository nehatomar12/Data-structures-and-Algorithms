"""
Problem: Given an unsorted array A of size N of non-negative integers,
         find a continuous sub-array which adds to a given number S.

Input:
        5 12 (size sum)
        1 2 3 7 5
        10 15
        1 2 3 4 5 6 7 8 9 10
Output:
        2 4
        1 5

Steps:
    - Modified version of Kadane's algorithm
    - case1: when local_max becomes equals to required_sum
    - case2: when local_max becomes > then required_sum.
        (try to remove elements from the beginning until the condition is false)
"""
required_sum = 26
arr = [1,2,3,4,5,6,7,8,9,10]
local_max = 0
start,end=0,0
for i in range(len(arr)):
    local_max += arr[i]
    while local_max > required_sum:
        local_max -= arr[start]
        start += 1
    if local_max == required_sum:
        end = i
        break

print((arr[start:end+1]))
print(local_max)
