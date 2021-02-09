
arr = [10,80,70,30,50,90]

def partition(arr,start,end):
    leader = follower =start
    while leader < end:
        #print((arr[leader],arr[end]))
        if arr[leader] <= arr[end]:
            #print(arr[leader], end=" ")
            arr[follower], arr[leader] = arr[leader], arr[follower]
            follower += 1
        leader += 1
    # to get pivot in it place
    # swap follower and end
    arr[follower], arr[end] = arr[end], arr[follower]
    return follower

def quicksort(arr,start,end):
    if start >= end:
        return
    pivot = partition(arr,start,end)
    quicksort(arr, start, pivot-1)
    quicksort(arr, pivot+1, end)



quicksort(arr,0,len(arr)-1)
print(arr)
