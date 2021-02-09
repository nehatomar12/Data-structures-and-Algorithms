"""
Given a set of time intervals in any order, merge all overlapping intervals into
one and output the result which should have only mutually exclusive intervals

{{1,3}, {2,4}, {5,7}, {6,8}}. The intervals {1,3} and {2,4} overlap with each other,
so they should be merged and become {1, 4}. Similarly, {5, 7} and {6, 8} should be merged and become {5, 8}

arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
ans = [(1,9)]

method:
    1. sort the given intervals by a[0]
    2. take 2 variable s,max as starting and ending
    3. for every set check the condition and append the set in m=[]
        if a[0] > max:
            # specific case for i!=0
                m.append(s,max)
            update s and max to a[0] a[1]
        else:
            a[1] > max:
                update only max

    4. check s,max not in m

"""
def mergeIntervals(arr):

        # Sorting based on the increasing order
        # of the start intervals
        arr.sort(key = lambda x: x[0])

        # array to hold the merged intervals
        m = []
        a = 0
        s,max = arr[0][0], arr[0][1]
        for i in range(1, len(arr)):
            a = arr[i]
            if a[0] > max:
                m.append([s,max])
                max = a[1]
                s = a[0]
            else:
                if a[1] >= max:
                    max = a[1]

        #'max' value gives the last point of
        # that particular interval
        # 's' gives the starting point of that interval
        # 'm' array contains the list of all merged intervals

        if [s, max] not in m:
            m.append([s, max])
        print("The Merged Intervals are :", end = " ")
        print(m)
        for i in range(len(m)):
            print(m[i], end = " ")


arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
#arr = [[1,3],[2,4],[5,7],[6,8]]
arr = [[5,  24] , [39, 60] , [15, 28] , [27, 40] , [50, 90]]
#Input: arrl[] = {1, 2, 9, 5, 5}
#exit[] = {4, 5, 12, 9, 12}
arr = [[1,4],[2,5],[9,12],[5,9],[5,12]]
mergeIntervals(arr)
print()