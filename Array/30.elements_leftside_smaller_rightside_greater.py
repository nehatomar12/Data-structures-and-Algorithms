"""
Given an array, find an element before which all elements are smaller than it,
and after which all are greater than it. Return the index of the element
if there is such an element, otherwise, return -1.
Examples:

Input: arr[] = {5, 1, 4, 3, 6, 8, 10, 7, 9};
Output: 4
Explanation: All elements on left of arr[4] are smaller than it
and all elements on right are greater.

Input: arr[] = {5, 1, 4, 4};
Output: -1
Explanation : No such index exits.

Approach1:
    https://www.geeksforgeeks.org/find-the-element-before-which-all-the-elements-are-smaller-than-it-and-after-which-all-are-greater-than-it/
    (Time Complexity: O(n) ,Auxiliary Space: O(n))
        {5, 1, 4, 3, 6, 8, 10, 7, 9} cond: LM[i]= max(LM[i-1], arr[i-1]) max(5,-inf)
        LM: {-inf,5,5,5,5,6,8,10,10 }
    1. Create array leftMax[]
    2. Now get rightMin = -inf
        traverse from last and compare Lm and arr[i]
        LM[i] < arr[i] < rightMin
            return i
        rightMin = min(rightMin, arr[i])

Approach2:

"""

def findElement (a, n):

    # Base case
    if (n in (0,1,2)):
        return -1
    element, maxx = a[0], a[0]
    idx = -1
    # ignore both the leftmost and rightmost
    i = 1
    while (i < (n - 1)):
        # First get the max value from the leftside
        if (a[i] < maxx and i < (n - 1)):
            i += 1
        else:
            element = a[i]
            idx = i
            maxx = a[i]
            # Now check all the right value from elements are greater
            while (a[i] >= element and i < (n - 1)):
                if (a[i] > maxx):
                    maxx = a[i]
                i += 1
    print((a[idx]))
    return idx

def findElement2 (a, n):

    # Base case
    if (n == 1 or n == 2):
        return -1

    # 1. element is the possible candidate
    # for the solution of the problem
    # 2. idx is the index of the
    # possible candidate
    # 3. maxx is the value which is maximum
    # on the left side of the array
    # 4. bit tell whether the loop is
    # terminated from the if condition or
    # from the else condition when loop do
    # not satisfied the condition.
    # 5. check is the variable which tell
    # whether the element is updated or not
    element, maxx, bit = a[0], a[0], -1
    check = 0
    idx = -1

    # The extreme of the array can't be
    # the solution Therefore iterate
    # the loop from i = 1 to < n-1
    i = 1
    while (i < (n - 1)):

        # Here we find the possible candidate
        # where element with left side smaller
        # and right side greater. when the if
        # condition fail we check and update
        # in else condition
        if (a[i] < maxx and i < (n - 1)):
            i += 1
            bit = 0

        # Here we update the possible element
        # if the element is greater than the
        # maxx (maximum element so far). In
        # while loop we sur-pass the value
        # which is greater than the element
        else:
            if (a[i] >= maxx):
                element = a[i]
                idx = i
                check = 1
                maxx = a[i]

            if (check == 1):
                i += 1

            bit = 1
            while (a[i] >= element and i < (n - 1)):
                if (a[i] > maxx):
                    maxx = a[i]

                i += 1

            check = 0

    # Checking for the last value and whether
    # the loop is terminated from else or
    # if block
    if (element <= a[n - 1] and bit == 1):
        return idx
    else:
        return -1

# Driver Code
if __name__ == '__main__':

    arr = [ 5, 1, 4, 3, 6, 8, 2, 10, 17, 19 ]
    #arr = [5, 1, 4, 4]
    #arr = []
    n = len(arr)

    # Function call
    print(("Index of the element is",
           findElement2(arr, n)))