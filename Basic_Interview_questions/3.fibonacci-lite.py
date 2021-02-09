
"""
0 1 1 2 3 5 8 13
"""
num = 12
def fib_dp(num):
    if num in (0, 1):
        return num
    fib = [0] * (num+1)
    fib[0] = 0
    fib[1] = 1

    i = 2
    while i < num+1:
        fib[i] = fib[i-1] + fib[i-2]
        i += 1
    return fib[-1]

def fib_recursion(num):
    if num in (0,1):
        return num
    return fib_recursion(num-1) + fib_recursion(num-2)

print((fib_dp(num)))
print((fib_recursion(num)))