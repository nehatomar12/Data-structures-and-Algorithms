"""
Given two sorted arrays Arr1[] and Arr2[] in non-decreasing order with size N and M.
The task is to merge the two sorted array into one sorted array

Input: Arr1[] = {1, 5, 9, 10, 15, 20}; size: m
       Arr2[] = {2, 3, 8, 13}; size: n
Output: Arr1[] = {1, 2, 3, 5, 8, 9}
        Arr2[] = {10, 13, 15, 20}

Tip: use selection sort logic
Logic:
    1. Iterate Arr1 and Arr2 from last as j and i resp
       save last element 'last = Arr1[j]'
    2. Find the smallest element in Arr1 greater than Arr2[i].
       Move all elements one position ahead till the smallest greater
       element is not found
       Found: check if Arr[j+1](element after the smaller element found) is greater then the last element
       array: copy Arr1[j+1] = Arr2[i]
                  Arr2[i] = last
    3. update last and continue same steps
Steps:
    1.  Arr1[] = {1, 5, 9, 10, 15, 20}; --->j=m-2(15)
        Arr2[] = {2, 3, 8, 13}; ---->i=n-1(13)
        last=Arr1[j] (20)
        a. 15 > 13 True
            Arr1[] = {1, 5, 9, 10, 15, 15}; --->j=3(10)
            Arr2[] = {2, 3, 8, 13}; ---->i=n-1(13)
        b. 10 > 13 False
            check 13>last(20) No; copy arr2 13-->Arr1[j+1], Arr2[i] = last
            Arr1[] = {1, 5, 9, 10, 13, 15}; --->j=3(10)
            Arr2[] = {2, 3, 8, 20}; ---->i=n-1(13)

    2.  Arr1[] = {1, 5, 9, 10, 13, 15}; --->j=m-2(13),last=15
        Arr2[] = {2, 3, 8, 20}; ---->i=n-2(8)

"""
Arr1 = [1, 5, 9, 10, 15, 20]
Arr2 = [2, 3, 8, 13]
# For special condition check
Arr2 = [1, 3, 5, 7]   #----- m (j=5)
Arr1 = [0, 2, 6, 8, 9] #------n (i=9)
m, n = len(Arr1), len(Arr2)


def in_place_merge():
    for i in range(n-1, -1, -1):
        last = Arr1[m-1] #7
        j = m-2
        # when arr2 j>=0 consider is all elemets of Arr1 is smaller then Arr2[i]
        while (j >= 0 and Arr1[j] > Arr2[i]):
            Arr1[j+1] = Arr1[j]
            j -= 1
        # if all elements are smaller in Arr1 then check with last value
        #  then swap otherwise decrement i value and continue
        if j != m-2 or last > Arr2[i]:  # j != (m-2) --> don't swap
            Arr1[j+1] = Arr2[i]
            Arr2[i] = last



in_place_merge()
print((Arr1, Arr2))
