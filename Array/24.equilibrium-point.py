"""
Given an array A of N positive numbers.
The task is to find the first Equilibium Point in the array.
Equilibrium Point in an array is a position such that
the sum of elements before it is equal to the sum of elements after it.

N = 5
A[] = {1,3,5,2,2}
Output: 3

Steps:
    1) Initialize leftsum  as 0
    2) Get the total sum of the array as sum
    3) Iterate through the array and for each index i, do following.
        a)  Update sum to get the right sum.
            sum = sum - arr[i]
        // sum is now right sum
        b) If leftsum is equal to sum, then return current index.
        // update leftsum for next iteration.
        c) leftsum = leftsum + arr[i]
    4) return -1
"""
def equilibium_point(arr):
    result = -1
    left_sum = 0
    total_sum = sum(arr)

    for i, ele in enumerate(arr):
        total_sum -= ele
        if left_sum == total_sum:
            result = i
            break
        left_sum += ele

    return result



if __name__ == "__main__":
    # Time Complexity: O(n)
    arr = [-7, 1, 5, 2, -4, 3, 0]
    res = equilibium_point(arr)
    print(("Equilibium Point in the array is {}".format(res)))
