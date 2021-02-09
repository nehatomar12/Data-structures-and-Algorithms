"""
Contiguous sub-array with maximum sum.

local_max: sum of elements visted till i
global_max: sum of elemnets with maximum sum
start, end: to store index of result array

"""
arr = [1,2,3,-2,5]

local_max, global_max = 0,0
start,end , s = 0,0,0

for i in range(len(arr)):
    local_max += arr[i]
    if local_max > global_max:
        global_max=local_max
        start = s
        end=i
    # if local_max has negative value the elements in local_max
    # is not part of max contiguous sub-array
    # update the local_max and s to next index
    if local_max < 0:
        local_max=0
        s=i+1
print((arr[start:end+1]))
print((sum(arr[start:end+1])))
