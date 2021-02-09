def min_heapify(arr,size,i):
    # Find largest among root and children
    l = 2*i
    r = 2*i +1
    #check if i is non-leaf node
    if l < size and r < size:
        if arr[i] > arr[l] or arr[i] > arr[r]:
            if arr[l] < arr[r]:
                arr[l],arr[i]=arr[i],arr[l]
                min_heapify(arr,size,l)
            else:
                arr[r],arr[i]=arr[i],arr[r]
                min_heapify(arr,size,r)

def heapSort(arr):
    size=len(arr)
    # make heap
    for i in range((size//2),-1,-1):
        min_heapify(arr,size,i)

    print(arr)
    #swap parent to last element
    for i in range(size-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        min_heapify(arr,i,0)


arr = [ 1,3,12, 11, 13, 5, 6, 7]

#minheap: [1, 3, 5, 6, 13, 12, 11, 7]
# min_heapify(arr,len(arr),arr[1])
# print(arr)
heapSort(arr)
# n = len(arr)
print(("Sorted array is: ", arr))
# for i in range(n):
#     print ("%d" %arr[i],end=" ")