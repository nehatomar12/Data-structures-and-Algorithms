



def binary_search(arr, size, element):
    low, high = 0, size-1
    while low <= high:
        mid = (low + high)/2
        if arr[mid] == element:
            return mid+1
        elif arr[mid] < element:
            low = mid+1
        else:
            high = mid-1
    return -1




if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    size = len(arr)
    print((binary_search(arr, size, element=1)))