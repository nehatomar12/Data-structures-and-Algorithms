"""
Given an array of positive integers. The task is to find inversion count of array.

Inversion Count : For an array, inversion count indicates how far (or close) the array is from being sorted.
If array is already sorted then inversion count is 0.
If array is sorted in reverse order that inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Input:
    5
    2 4 1 3 5

Output:
    3


Steps:
    Merge sort:
        1. Break array into single elemets >> same
        2. compare and combine the elements
            while comapring if a[i] < a[j] no inversion
            if not, add it to inversion count


"""


def simple_approach(arr):
    # O(n^2)
    swaps = 0
    for i in range(0, len(arr)-1):
        temp = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < temp:
                swaps += 1
    print("simple_approach:   ", swaps)

def merge(arr, temp_arr, left, mid, right):
    inversion_count = 0
    i , j= left , mid+1
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            # No inversion
            temp_arr.append(arr[i])
            i += 1
        else:
            # inversion required
            temp_arr.append(arr[j])
            inversion_count += mid-i +1 # [1 6 7 20] [3 5 8 1] for 6, Inv_count = 3-1+1=2
            j += 1

    #copy remaining elements
    temp_arr += arr[i:]
    temp_arr += arr[j:]

    arr = temp_arr

    return inversion_count

def inversion_with_merge_sort(arr, temp_arr, left, right):
    # O(nlogn)
    inversion_count = 0
    if left < right:
        mid = (left + right)//2
        inversion_count += inversion_with_merge_sort(arr, temp_arr, left, mid)
        inversion_count += inversion_with_merge_sort(arr, temp_arr, mid+1, right)
        inversion_count += merge(arr, temp_arr, left, mid, right)
    return inversion_count

if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    simple_approach(arr)
    temp_arr = []
    print(inversion_with_merge_sort(arr, temp_arr, 0, len(arr)-1))
