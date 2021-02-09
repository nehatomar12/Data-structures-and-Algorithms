
"""
Given a sorted array of positive integers.
Your task is to rearrange the array elements alternatively
i.e first element should be max value,
    second should be min value,
    third should be second max,
    fourth should be second min and so on..

Input:
    6
    1 2 3 4 5 6
Output:
    6 1 5 2 4 3
"""
arr = [1,2,3,4,5,6]

size = len(arr)

# Approach1
def rearrange_extra_space():
    i,j=0,size-1
    temp = []
    flag = True
    while i < j:
        temp.append(arr[j])
        temp.append(arr[i])
        i += 1
        j -= 1
        # if flag:
        #     temp.append(arr[j])
        #     j -= 1
        # else:
        #     temp.append(arr[i])
        #     i += 1
        # flag = not flag
    if i == j:  # Handle the odd case
        temp.append(arr[i])
    print(temp)

#rearrange_extra_space() # Time and Space complexity O(n) and O(n)

# Approach2
# The idea is to use multiplication and modular trick to store two elements at an index.
# If 'i' is even
#        arr[i] += arr[max_index] % max_element * max_element
#        max_index--
#     ELSE // if 'i' is odd
#        arr[i] +=  arr[min_index] % max_element * max_element
#        min_index++

def rearrange_2():
    print(arr)
    min_ ,max_= 0, size-1
    max_e = arr[size-1] + 1 # can be any number greater then the largest number
    for i in range(size):
        if i%2 == 0:
            arr[i] += (arr[max_] % max_e) * max_e
            max_ -= 1
        else:
            arr[i] += (arr[min_] % max_e) * max_e
            min_ += 1
    print(arr)
    for a in arr:
        print(a//max_e,end=" ")
    print()
rearrange_2()
#rearrange_extra_space()