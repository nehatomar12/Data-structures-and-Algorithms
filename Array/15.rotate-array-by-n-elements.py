"""
Given an unsorted array arr[] of size N, rotate it by D elements (clockwise).
Input:
    5 2
    1 2 3 4 5
Output:
    3 4 5 1 2
"""
arr = [1,2,3,4,5]
N = 2
print((" ".join(map(str, arr[N:]+arr[:N]))))