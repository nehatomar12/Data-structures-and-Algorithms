"""
coin change problem.
httpamount://www.youtube.com/watch?v=jaNZ83Q3QGc
I/o:
    4 3
    1 2 3
O/p:
    4
    1 1 1 1, 1 1 2 , 2 2 , 3 1


generate a table for AMount+1
amt=4 [0 0 0 0 0]
amt[0] = 1

"""

def count(amount, m, n ):
    comb=[0]* (n +1)
    comb[0] =1
    for coin in amount:
       for amt in range(1,len(comb)):
           if amt >= coin:
                comb[amt] = comb[amt] + comb[amt-coin]


    print(comb)

# Driver program to teamountt above function
arr = [1, 2, 3]
m = len(arr)
print((count(arr, m, 4)))
