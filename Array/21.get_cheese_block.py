"""
Problem statement:
There are blocks of cheese of different weight placed in a line. A mouse would like to eat the cheese, but with some rules.
The mouse can’t eat two consecutive cheese blocks. The mouse would like to eat maximum cheese from the line of cheese blocks.
Weight of each cheese block in Kg is given as a[i] in an integer array.
Input:
The first line of input contains an integer T denoting the number of test cases.
Each test case contains an integer n which denotes the number of elements in the array a[].
Next line contains space separated n elements in the array a[].
Output:
Print an integer which denotes the maximum amount of cheese that the mouse can have.
Constraints:
1<=T<=200
1<=n<=1000
1<=a[i]<=10000
Example:
Input:
2
6
8 5 10 100 10 5
3
1 2 3
Output:
113
4

Solution:
    Maintain 2 variable for storing below values for every ith index
        - include: maximum sum so far including the all previous and current elements
          (value = exclude_value of previous element + current_value)
          as we don't want to take the adjecent cheese block in result
        - exclude: maximum sum so far excluding the current element
          (value = maximum of include and exclude of previous element)
          as we don't want to include current element

    Result will be the maximum of include and exclude

Output:
    python 21.get_cheese_block.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK
"""

import unittest

def get_cheese_block(arr, n):
    # Base condition
    if n == 1:
        return arr[0]
    # Initialize incl and excl
    incl = arr[0]
    excl = 0
    # Iterate over the remaining elements of array
    for i in range(1, n):
        prev_incl = incl
        incl = excl + arr[i]
        excl = max(prev_incl, excl)
    return max(excl, incl)


class Testing(unittest.TestCase):
    def testBlockOfCheese(self):
        self.assertEqual(get_cheese_block([8, 5, 10, 100, 10, 5], 6), 113)
        self.assertEqual(get_cheese_block([1, 2, 3], 3), 4)

if __name__ == "__main__":
    unittest.main()
