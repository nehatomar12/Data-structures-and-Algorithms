
# coin change problem.
# https://www.youtube.com/watch?v=jaNZ83Q3QGc
def count(S, m, n ):
    comb=[0]* (n +1)
    comb[0] =1
    for coin in S:
       for amt in range(1,len(comb)):
           if amt >= coin:
                comb[amt] = comb[amt] + comb[amt-coin]


    print(comb)
    print(comb[4])

# Driver program to test above function
arr = [1, 2, 5]
m = len(arr)
count(arr, m, 12)
