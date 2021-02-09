"""
the length of LIS for
{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and
LIS is {10, 22, 33, 50, 60, 80}.

Steps:
    arr = [7 1 4 8 11 2 14 3]
    lis = [1 1 1 1 1  1 1  1] ->initaial all the single element form the lis


1. arr: [7 1] if 1 > 7: not(dont update)
2. arr: [7 1 11] if 11 > 7: yes update lis(for 11 to +1)
                 if 11 > 1: yes but as we have already update for squence [7,11] if we directly add +1 for 11
                     sequence wont be right
                     add condition if lis(1)+1 > lis(11) if yes update else don't
cond:
    arr[i] > arr[j] and lis(j)+1 > lis(i)
    i => 1--n
    j => 0--i
Time Complexity: O(n2).
Auxiliary Space: O(n).

"""
# TC O(n2) time
def get_lis(arr):
    n = len(arr)
    lis = [1]*n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and (lis[j]+1) > lis[i]:
                lis[i] = lis[j]+1

    maxi = max(lis)
    i = n-1
    while i > 0:
        if lis[i] == maxi:
            print((arr[i]))
            maxi -= 1
        i-=1


# TC O(n Log n) time
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
def CeilIndex(A, l, r, key):
    while (r - l > 1):
        m = l + (r - l)//2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r

def LongestIncreasingSubsequenceLength(A, size):
    tailTable = [0] * (size+1)
    tailTable[0] = A[0]
    len = 1

    # Add check for 3 cases
    # Case 1. There are no active lists, create one.
    # Case 2. Clone and extend.
    # Case 3. Clone, extend and discard.

    for i in range(1, size):

        if (A[i] < tailTable[0]):
            tailTable[0] = A[i]

        elif (A[i] > tailTable[len-1]):
            tailTable[len] = A[i]
            len+= 1

        else:
            tailTable[CeilIndex(tailTable, -1, len-1, A[i])] = A[i]
    return len


# Driver program to
# test above function

A = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
#A = [1, 8, 4] #, 12, 0]
n = len(A)

print("Length of Longest Increasing Subsequence is ",
       LongestIncreasingSubsequenceLength(A, n))
