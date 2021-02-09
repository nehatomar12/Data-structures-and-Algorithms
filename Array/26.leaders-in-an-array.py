"""
Given an array A of positive integers.
Your task is to find the leaders in the array.
An element of array is leader if it is greater than or equal to all the elements to its right side.
The rightmost element is always a leader.

Input:
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17
as it is greater than all the elements
to its right.  Similarly, the next
leader is 5. The right most element
is always a leader so it is also
included.
"""
def approach_1(arr):
    # Time Complexity: O(n*n)
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                break
        if j == len(arr)-1:
            print((arr[i]))


def leaders(arr):
    # Time Complexity: O(n)
    _max=arr[-1]
    leaders = [arr[-1]]
    for i in range(len(arr)-2,-1,-1):
        if arr[i] > _max:
            leaders.append(arr[i])
            _max = arr[i]
    print(leaders)

if __name__ == "__main__":
    arr = [16,17,4,3,5,2]
    leaders(arr)
    #approach_1(arr)