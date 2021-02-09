
################### Heap Sort ####################
# building a max heap
from heapq import heapify, heappush, heappop

#example https://www.geeksforgeeks.org/building-heap-from-array/
def heapify(arr, size, i):
    largest = i
    lc = 2*i + 1
    rc = 2*i + 2

    if lc < size and arr[lc] > arr[largest]:
        largest = lc
    if rc < size and arr[rc] > arr[largest]:
        largest = rc
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, size, largest)


def heapsort(arr, size):
    # Build max heap
    for i in range((size//2-1), -1, -1):
        heapify(arr, size, i)

    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

################### Find median in a stream  ####################


"""
5 2 1 3 4 6
==>  1 2 3 4 5 6
construct maxheap(1st half) minHeap(2nd half)
upperMin = maxHeap(top)
lowerMax = minHeap(first)


"""
upperMin = 0
lowerMax = 0
lowerHeap = []
upperHeap = []

def addNum(num):
    global upperMin, lowerMax

    if num > upperMin or (lowerMax<=num<=upperMin and len(lowerHeap) == len(upperHeap)):
        heappush(upperHeap, num)
        lowerMax = upperHeap[0]
    else:
        heappush(lowerHeap, -num)
        upperMin = lowerHeap[0]

    # maintain the invariant that their lens are equal, or upper has 1 more than lower
    if len(upperHeap)-len(lowerHeap) > 1:
        heappush(lowerHeap, -heappop(upperHeap))
        upperMin = lowerHeap[0]
    elif len(lowerHeap) - len(upperHeap) >1 :
        heappush(upperHeap, -heappop(lowerHeap))
        lowerMax = upperHeap[0]


def findMedian():
    """
    Returns the median of current data stream
    :rtype: float~
    """
    if len(upperHeap) == len(lowerHeap):
        upperMin = + upperHeap[0]
        lowerMax = - lowerHeap[0]
        return (int(upperMin) + int(lowerMax)) // 2
    else:
        assert len(upperHeap) == len(lowerHeap) + 1
        return int(upperHeap[0])

################### Find median in a stream  ####################

########## Kth largest element ##################

#code




def kth_largest():
    import heapq  # minheap
    size, k = 6,4
    arr = [1,2,3,4,5,6]
    res = [-1] * (k-1)
    heap = []
    for i in range(k):
        heappush(heap, arr[i])
    res.append(heap[0])

    for i in range(k, size):
        if heap[0] < arr[i]:
            heap[0] = arr[i]
            heapq.heapify(heap)
            res.append(heap[0])
    print(res)

########## Kth largest element ##################






arr = [1, 3, 12, 11, 13, 5, 6, 7]
size = len(arr)

heapsort(arr, size)
print(arr)
# for i in [5, 15, 1, 3 ]:
#     addNum(i)
#     print(int(findMedian()))
#kth_largest()