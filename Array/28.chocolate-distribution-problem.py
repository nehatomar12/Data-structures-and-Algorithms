"""
8
3 4 1 9 56 7 9 12
5

Testcase 1: The minimum difference between maximum chocolates and minimum chocolates is 9-3=6
"""
import sys
def chocolate_diff(arr, students, packets):
    min_diff = sys.maxsize

    if students == 0 and packets == 0:
        return 0

    if packets < students:
        return -1

    arr.sort()
    print(arr)

    i=0
    while(i+students-1 < packets):
        temp = arr[i+students-1] - arr[i]
        if temp < min_diff:
            min_diff=temp
        i += 1


    print(min_diff)


if __name__ == "__main__":
    #Time Complexity: O(n Log n) as we apply sorting before subarray search.
    arr = [3, 4, 1, 9, 56, 7, 9, 12]
    students = 5 # Number of students
    packets = len(arr)
    chocolate_diff(arr, students, packets)