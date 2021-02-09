"""
Write a program to find the the peak element of the array. Expected running time O(logn)

Eg :
Input Format:
10
1 2 3 4 5 6 8 7 5 3

Output : 8
"""

arr = [1,2,3,4,5,6,8,7,5,3]

i,j = 0,len(arr)-1

global_max = 0
local_max = 0
while i <= j:
    if arr[i] > arr[j]:
        local_max = arr[i]
    else:
        local_max = arr[j]

    if local_max > global_max:
        global_max = local_max

    i += 1
    j -= 1

print(global_max)