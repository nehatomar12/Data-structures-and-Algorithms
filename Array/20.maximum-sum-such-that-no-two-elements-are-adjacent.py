"""
find the maximum sum of a subsequence with the constraint
that no 2 numbers in the sequence should be adjacent in the array

Input : arr[] = {5, 5, 10, 100, 10, 5}
Output : 110

Input : arr[] = {1, 2, 3}
Output : 4

Steps:
    maintain 2 variable which have max value till index i-1 and i-2
    curr is updated as
        1
"""

import unittest

def get_max_subsequence(arr, n):
    if n == 1:
        return arr[0]
    prevOfPrev = arr[0]
    prev = max(arr[0], arr[1])
    for i in range(2, n):
        curr = max(arr[i], max(prev, prevOfPrev+arr[i]))
        prevOfPrev = prev
        prev = curr
    return prev

def get_cheese_block(arr, n):
    # Base condition
    if n == 1:
        return arr[0]

    # incl: maximum sum soo far including the previous and current elements
    # incl = excl + arr[i] // because excl of i-1 has the max value soo far without including the i-1 value
    # excl: maximum sum soo far excluding the current elements(take max of incl and excl of i-1)
    incl = arr[0]
    excl = 0
    for i in range(1, n):
        prev_incl = incl
        incl = excl + arr[i]
        excl = max(prev_incl, excl)
    #print(incl, excl)
    return max(excl, incl)


class Testing(unittest.TestCase):
    def testBlockOfCheese(self):
        self.assertEqual(get_cheese_block([8, 5, 10, 100, 10, 5], 6), 113)
        self.assertEqual(get_cheese_block([1, 2, 3], 3), 4)

if __name__ == "__main__":
    unittest.main()
