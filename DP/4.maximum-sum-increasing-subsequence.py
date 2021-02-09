"""
Similar to longest-increasing-subsequence

"""
def get_mis(arr):
    n = len(arr)
    mis = []
    for i in arr:
        mis.append(i)

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and (mis[j]+arr[i]) > mis[i]:
                mis[i] = mis[j]+arr[i]

    print(mis)


arr = [7, 1, 4, 8, 11, 2, 14, 3]
get_mis(arr)