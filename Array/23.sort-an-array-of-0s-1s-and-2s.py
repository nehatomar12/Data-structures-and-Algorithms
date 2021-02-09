"""
Given an array A[] consisting 0s, 1s and 2s.
The task is to write a function that sorts the given array.
The functions should put all 0s first, then all 1s and all 2s in last.

Examples:

Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

If (a[mid] ==0),
    then swap the element with the element low and shrink the unknown range by doing low++ and mid++.
If (a[mid] ==1),
    then simply increment mid (mid++), thus further shrinking unknown range.
If (a[mid] ==2),
    then swap it with an element in high range and decrement high (high--).
"""

def segregate0and1and2(arr):
    low = 0
    mid = 0
    high = len(arr) -1

    while mid <= high:
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid],arr[high] = arr[low],arr[high]
            high -= 1
    print(arr)

def segregate0and1(arr):

    left = 0
    right = len(arr) -1

    while left <= right:
        while left <= right and arr[left] == 0:
            left += 1
        while left <= right and arr[right] == 1:
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    print(arr)

if __name__ == "__main__":
    arr = [0, 1, 2, 0, 1, 2]
    segregate0and1and2(arr)
    arr = [0, 1, 0, 1, 1, 1]
    segregate0and1(arr)
