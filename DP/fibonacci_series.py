#
# n= 9 [0, 1, 1, 2, 3, 5, 8,13,21]
#

'''
            fib(5)
    fib(3)           fib(4)
fib(2)  fib(1)    fib(3)    fib(2)
            fib(2)  fib(1)

'''
# Recursive solution
#  n=1 0
#  n=2 1
def fib(n):
    if n == 1 or n == 2:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)
    return res
#print(fib(100))

#DP
saved_res = {}
def dp_fib(n, saved_res):
    #print(saved_res)
    if saved_res.get(n) != None:
        return saved_res[n]
    if n == 0:
        res = 0
    elif n == 1 or n == 2:
        res = 1
    else:
        res = dp_fib(n-1, saved_res) + dp_fib(n-2, saved_res)
    saved_res[n] = res
    return res

saved = [0,1]
def list_dp_fib(n):
    while len(saved) < n+1:
        saved.append(0)
    if n <= 1:
        return n

    if saved[n-1] == 0:
        saved[n-1] = list_dp_fib(n-1)
    if saved[n-2] == 0:
        saved[n-2] = list_dp_fib(n-2)
    
    saved[n] = saved[n-1] + saved[n-2]
    return saved[n]

print((list_dp_fib(5)))