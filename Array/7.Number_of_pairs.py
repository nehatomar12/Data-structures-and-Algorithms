"""
Given two arrays X and Y of positive integers, find the number of pairs
such that x^y > y^x (raised to power of) where x is an element from X and y is an element from Y.
"""
from itertools import product

M = 3
N = 2
X = [2, 1, 6, 3]
Y = [1, 5, 3]


def simple_approach():
    count = 0
    for i in range(M):
        for j in range(N):
            if pow(X[i], Y[j]) > pow(Y[j], X[i]):
                count += 1
    print(count)


def get_index(arr, size, element):
    low, high = 0, size-1
    ans = -1
    while low <= high:
        mid = (low + high)//2
        #### simple
        if arr[mid] == element:
            ans = mid
            return ans
        ###
        if arr[mid] > element:
            #ans = mid
            high = mid-1
        else:
            low = mid + 1
    return ans


def optimize_approach():
    """
    General case if x < y, then x^y > y^x
    Sort both array's
    Conditions of Y array:(exceptions)
        1. Get count of 0's, 1's, 2's, 3's, 4's
    Conditions of X array:(exceptions)
        1. if x=0; then no-ops (0^1 ? 1^0)
        2. if x=1; count no's of 0's in Y and add them in answers. { 1^0 > 0^1}
        3. if x=2; getcount of all elements > 2 from Y, update answer { 2^5 > 5^2}
            exceptions for y=3,y=4 ex: 2^3 < 3^2 and 2^4 = 4^2. as we have added count in answer
            subtract no. of 3,4 from answer. and add 0's and 1's  2^0 > 0^2 and 2^1 > 1^2
        4. if x=3; get all 2's in Y and add them in answer as 3^2 > 2^3
        5. else getIndex for element. answer += total_elements_of_y - index

    """
    zeros, ones, twos, threes, fours, answer = 0, 0, 0, 0, 0, 0
    X.sort()
    Y.sort()

    for i in range(len(Y)):
        if Y[i] == 0:
            zeros += 1
        elif Y[i] == 1:
            ones += 1
        elif Y[i] == 2:
            twos += 1
        elif Y[i] == 3:
            threes += 1
        elif Y[i] == 4:
            fours += 1

    for j in range(len(X)):
        if X[j] == 0:
            continue
        elif X[j] == 1:
            answer += zeros
        else:
            index = get_index(Y, N, element=X[j])
            if index != -1:
                answer += (N-index)
            answer += (ones + zeros)
            if X[j] == 3:
                answer += twos
            elif X[j] == 2:
                answer -= threes
                answer -= fours

    return answer


simple_approach()
print((optimize_approach()))
