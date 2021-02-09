"""
Input: arr[] = {5, 9, 14, 6, 10, 77}, K=3
Output: 5
Explanation:
The sub-array of length 3 with maximum distinct prime factors is 6, 10, 77 and prime factors are 2, 3, 5, 7, 11.

"""
# https://www.geeksforgeeks.org/maximum-distinct-prime-factors-of-elements-in-a-k-length-subarray/

arr = [4, 2, 6, 10]
factors = [True] * (max(arr) + 1)

def get_prime_sieve(num):
    p = 2
    while p*p <= num:
        for i in range(p*p, num+1,p):
            factors[i] = False

        p += 1
    print(("{} Prime number".format(num)))
    return factors




def maximumDPF(arr, n, k):
    global factors
    ans = 0

    maps = {}

    # Calculating the total prime factors
    # for first k elements
    for i in range(0, k):

        # Calculating prime factors of
        # every element in O(logn)
        num = arr[i]
        while num != 1:
            maps[factors[num]] = maps.get(
                             factors[num], 0)+1
            num = int(num / factors[num])

    ans = max(len(maps), ans)

    for i in range(k, n):

        # Perform operation for
        # removed element
        num = arr[i - k]
        while num != 1:

            maps[factors[num]] = maps.get(
                             factors[num], 0)-1

            # if value in map become 0,
            # then erase that index from map
            if maps.get(factors[num], 0) == 0:
                maps.pop(factors[num])

            num = int(num / factors[num])

        # Perform operation for
        # added element
        num = arr[i]
        while num != 1:

            maps[factors[num]] = int(maps.get(
                                 factors[num], 0))+1
            num = int(num / factors[num])

        ans = max(len(maps), ans)

    return ans


# Driver Code
if __name__ == '__main__':

    k = 3
    n = len(arr)

    factors = get_prime_sieve(max(arr) + 1)
    print(factors)
    print((maximumDPF(arr, n, k)))
