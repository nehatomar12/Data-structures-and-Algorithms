"""
Input:

7 4 0 9  [7 7 7 9] [9 9 9 9] [0+3+7+0]=10
Output:
10

arr = [ 3 0 0 2 0 4] (leftmax,rightmax array)
left = [ 3 3 3 3 3 4]
right = [4 4 4 4 4 4]

water = min(left,right) - arr[i]
    [0+3+3+1+3+0]

Testcase 1:
    Water trapped by block of height 4 is 3 units,
    block of height 0 is 7 units.
    So, total unit of water trapped is 10 units.


"""
def trapping_water(arr):
    water = 0

    left_max = 0
    right_max = 0

    low = 0
    high = len(arr)-1

    while low <= high:
        #  water = min(left_max,right_max) - arr[i]
        if arr[low] < arr[high]:
            if arr[low] > left_max:
                left_max = arr[low]
            else:
                water += (left_max-arr[low])
            low += 1
        else:
            if arr[high] > right_max:
                right_max = arr[high]
            else:
                water += (right_max-arr[high])
            high -= 1

    print(water)


if __name__ == "__main__":
    arr = [7, 4,0,9]
    trapping_water(arr)