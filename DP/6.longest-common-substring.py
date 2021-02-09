"""

"""

X = "ABCDGH"
Y = "ACDGHR"
m = len(X)
n = len(Y)

def common_substr():
    lcs = [[0 for j in range(n+1)] for i in range(m+1)]
    res = 0
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                lcs[i][j] = 0
            elif X[i-1] == Y[j-1]:
                lcs[i][j] = lcs[i-1][j-1] +1
                res = max(res, lcs[i][j])
            else:
                lcs[i][j] = 0

    print(res)

common_substr()