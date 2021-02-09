"""
Given an array of integers of size ‘n’.
calculate the maximum sum of ‘k’ consecutive elements in the array.

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39

"""
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

def brute_force_approach():
    #Time complexity = O(k*n)
    max_sum = 0
    start = 0
    for i in range(len(arr)-k):
        temp = sum(arr[i: i+k])
        if temp > max_sum:
            max_sum = temp
            start = i
    print(max_sum)
    print((arr[start:start+k]))

def sliding_window_approach():
    # Time Complexity is O(n)
    window_sum = sum(arr[:k])
    start = 0
    # Compute sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # current window.
    for i in range(len(arr)-k):
        current_sum = window_sum - arr[i] + arr[i+k]
        if current_sum > window_sum:
            window_sum = current_sum
            start = i +1
    print(window_sum)
    print((arr[start:start+k]))

if __name__ == "__main__":
    brute_force_approach()
    sliding_window_approach()
