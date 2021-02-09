"""
The problem is to count all the possible paths from top left to bottom right
of a mXn matrix with the constraints that from each cell you can either move only to right or down

Examples :

Input :  m = 2, n = 2;
Output : 2
There are two paths
(0, 0) -> (0, 1) -> (1, 1)
(0, 0) -> (1, 0) -> (1, 1)

Input :  m = 2, n = 3;
Output : 3
There are three paths
(0, 0) -> (0, 1) -> (0, 2) -> (1, 2)
(0, 0) -> (0, 1) -> (1, 1) -> (1, 2)
(0, 0) -> (1, 0) -> (1, 1) -> (1, 2)

DP solution:
    base case cell[0][0--m]==1, cell[0..n][0]==1
    cell[x][y] = cell[x-1]+cell[y-1]
"""

def no_of_paths(m, n):
    counts = [[0 for j in range(n)] for i in range(m)]

    for i in range(0, m):
        for j in range(0, n):
            if i==0 or j==0:
                counts[i][j] = 1
            else:
                counts[i][j] = counts[i-1][j]+counts[i][j-1]

    print(counts)

def optimize_no_of_paths(p,q):
    dp = [1 for i in range(q)]
    #print(dp)
    for i in range(p - 1):
        for j in range(1, q):
            dp[j] += dp[j - 1]
    print(dp)
    return dp[q - 1]


no_of_paths(m=2,n=3)
optimize_no_of_paths(p=2,q=3)