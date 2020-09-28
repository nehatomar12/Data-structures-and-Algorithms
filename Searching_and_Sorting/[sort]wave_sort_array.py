"""
Input:
    1 2 3 4 5
Output:
    2 1 4 3 5

Steps:
    1. Travese only even elements (0,2,4..)
    2. if current even element is less than previous element swap
    3. if current even element is less than next element swap
"""
arr = [1,2,3,4,5]
n=len(arr)
for i in range(0, n, 2):
    # if current even element is less than previous element swap
    if i > 0 and arr[i] < arr[i-1]:
        arr[i], arr[i-1] = arr[i-1], arr[i]

    # if current even element is less than next element swap
    if i < n-1 and arr[i] < arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]

print(arr)