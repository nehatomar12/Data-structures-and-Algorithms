
############ MERGE SORT ##############
def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def merge_sort(arr):
    # Just break the array to single elements
    # Send to merge()
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

############ MERGE SORT ##############





if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]
    print((merge_sort(arr)))