arr = [50,80,20,40,70,30,10,60]
#arr = [1,2,3,4]
print(("Bef Array: ", arr, "length: ", len(arr)))


def bubble_sort():
    for passnum in range(len(arr)-1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                arr[i+1],arr[i] = arr[i],arr[i+1]
    print(("After Swap: ", arr))

#bubble_sort()

def selection_sort():
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]
    print(("After swap :", arr))

#selection_sort()

def insertion_sort():
    # traverse full array from 1 to len(arr)
    for i in range(1, len(arr)):
        # copy value of i in key and get pos to traverse
        # if value is greater than key shift the values of j and last copy key to j
        key = arr[i]
        pos = i-1
        while pos >= 0 and key < arr[pos]:
            arr[pos+1] = arr[pos]
            pos -= 1
        arr[pos+1] = key
    print(("After swap :", arr))

insertion_sort()

def merge(left, right):
    result = []
    i ,j = 0 , 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # if one list is full added and other has elemnets
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)/2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

#print("After sort: ", merge_sort(arr)

def linear_serch_rec(arry, size, index ,data):
    if index == size:
        print("Not found")
        return

    if arry[index] == data:
        print(("found element: ", arry[index]))
        return
    else:
        linear_serch_rec(arry,size,index+1,data)

#linear_serch_rec(arr, len(arr), 0 , 60)

def linear_serach(data):
    for i in range(len(arr)):
        if arr[i] == data:
            print(("Found: ", arr[i]))
            return
    print("Not found")

#linear_serach(10)

def binary_serach(data):
    arrq = arr.sort()
    print(("Arr after sort: ",arr))
    left = 0
    right = len(arrq)-1

    while left <= right:
        mid = (left+right)/2
        if arr[mid] == data:
            print(("found: ", arr[mid]))
            return
        if arr[mid] < data:
            left = arr[mid+1]
        else:
            right = arr[mid-1]

#binary_serach(20)
