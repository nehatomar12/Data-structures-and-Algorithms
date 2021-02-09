"""

Given n non-negative integers representing an elevation map where
the width of each bar is 1, compute how much water it is able to trap after raining.

Return the total water it is able to trap after raining..
For Example

Input 1:
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
Output 1:
    6
    In this case, 6 units of rain water (blue section) are being trapped.
"""
A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def trap():
    s = []
    sol = 0
    for i in range(len(A)):
        if 0 < len(s) and A[s[-1]] <= A[i]:
            currht = A[s.pop()]
            while 0 < len(s) and A[s[-1]] < A[i]:
                sol += (i-s[-1]-1)*(A[s[-1]]-currht)
                currht = A[s.pop()]
            if 0 < len(s):
                sol += (i-s[-1]-1)*(A[i]-currht)
        s.append(i)
    return sol


print((trap()))
