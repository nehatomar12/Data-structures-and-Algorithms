# https://www.programiz.com/dsa/heap-sort

def heapify(arr,size,i):
    # Find largest among root and children
    largest = i
    l = 2*i
    r = 2*i +1
    #print(arr[largest])
    if l < size and arr[l] > arr[largest]:
        largest = l
    if r <size and arr[r] > arr[largest]:
        largest = r
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,size,largest)

def heapSort(arr):
    size=len(arr)
    # make heap
    for i in range((size//2),-1,-1):
        heapify(arr,size,i)

    # swap parent to last element
    for i in range(size-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)


arr = [ 1,3,12, 11, 13, 5, 6, 7]
# heapify(arr,len(arr),arr[1])
# print(arr)
heapSort(arr)
# n = len(arr)
print(("Sorted array is: ", arr))
# for i in range(n):
#     print ("%d" %arr[i],end=" ")