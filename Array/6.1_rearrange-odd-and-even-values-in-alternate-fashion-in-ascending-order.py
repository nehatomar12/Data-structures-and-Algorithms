"""
Given an array of integers (both odd and even),
the task is to arrange them in such a way that
odd and even values come in alternate fashion in
non-decreasing order(ascending) respectively.

If the smallest value is Even then we have to print Even-Odd pattern.
If the smallest value is Odd then we have to print Odd-Even pattern

Input: arr[] = {1, 3, 2, 5, 4, 7, 10}
Output: 1, 2, 3, 4, 5, 10, 7
Smallest value is 1(Odd) so output will be Odd-Even pattern.

Input: arr[] = {9, 8, 13, 2, 19, 14}
Output: 2, 9, 8, 13, 14, 19
Smallest value is 2(Even) so output will be Even-Odd pattern.


"""

def alternateRearrange(arr, n):
    arr.sort()
    v1, v2 = [], []

    for i in range(n):
        if arr[i]%2 == 0:
            v1.append(arr[i])
        else:
            v2.append(arr[i])

    index = 0 # for main arr
    i = 0 # index for v1
    j = 0 # index for v2

    flag = False
    if arr[0]%2 == 0:
        flag=True

    while index < n:
        if flag:
            arr[index] = v1[i]
            i += 1
        else:
            arr[index] = v2[j]
            j += 1
        flag = not flag
        index += 1

    print(arr)

# Driver code
arr = [ 9, 8, 13, 2, 19, 14]
n = len(arr)

alternateRearrange(arr, n)