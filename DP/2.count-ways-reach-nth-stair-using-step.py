"""

Question1: count all ways

steps:
    Create an array of size n + 1 and initialize the first 3 variables with 1, 1, 2. The base cases.
    Run a loop from 3 to n.
    For each index i, computer value of ith position as dp[i] = dp[i-1] + dp[i-2] + dp[i-3].
    Print the value of dp[n], as the Count of the number of ways to reach n th step

for any index ways will be all 3 levels below it

Question2: count minimum jumps to reach nth stair
    n
    n-1     (1 step more to reach n)
    n-2     (1 step more to reach n)
    n-3     (1 step more to reach n)

    so ans is 1+min(till the step n OR n-1 OR n-2)
    ex: t(5) == t(4),t(3),t(2)
        t(4) == t(3),t(2),t(1)

    base case if n=0, return 0
              if n=1,2,3 return 1(as only one jump is needed)

"""

def countAllWays(n):
    res = [0] * (n + 2)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1) :
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    return res[n]

def min_jumps(n):
    a = 0
    b = 1
    c = 1

    for i in range(3,n+1):
        d = 1 + min(a,b,c)
        a=b
        b=c
        c=d

    return c

# Driver code
n = 4
print((countAllWays(n)))
print((min_jumps(n)))