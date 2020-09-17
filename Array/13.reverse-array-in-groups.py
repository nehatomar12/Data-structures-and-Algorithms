"""
Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.
Input:
    5 3
    1 2 3 4 5
Output
    3 2 1 5 4
"""

arr = [1,2, 3, 4, 5,6,7,8,9]
k = 3
result = ""

for i in range(0, len(arr), k):
    sub_arr = arr[i:i+k]
    result += " ".join(map(str, sub_arr[::-1]))
    result += " "
print(result.strip())