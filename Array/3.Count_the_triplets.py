"""
Given an array of distinct integers. The task is to count all the
triplets such that sum of two elements equals the third element.

Input:
    4
    1 5 3 2
    3
    3 2 7
Output:
    2
    -1

Steps: [7,2,5,4,3,6,1,9,10,12]
    1. sort the list
    2. maintain 2 pointers at i(0, n-2) and j(i+1, n-1)
    3. sum= arr[i]+arr[j], sum in arr increase the result
"""
arr = [7,2,5,4,3,6,1,9,10,12]
arr.sort()
res=0
n=len(arr)
for i in range(0, n-2):
    for j in range(i+1,n-1):
        s = arr[i] +arr[j]
        if s > arr[-1]:
            break
        elif s in arr:
            res += 1

print((res if res>0 else -1))
