
MAXN = 100100
# vector<int> v[MAXN]
# int tim, tin[MAXN], tout[MAXN], pr[MAXN][20]
tim = 0
v = []
def dfs(x, anc):
    tin[x] = tim
    tim += 1
    pr[x][0] = anc
    #for (int i = 1 i < 20 i++)
    for i in range(1,20):
        pr[x][i] = pr[ pr[x][i - 1] ][i - 1]

    #for (int i = 0 i < v[x].size() i++)
    for i in range(v[x].size()):
        dfs(v[x][i], x)

    tout[x] = tim
    tim += 1

def isAnc(x, y):
    return (tin[x] <= tin[y] & tout[y] <= tout[x])

def lca( x,  y):
    if isAnc(x, y):
        return x

    if isAnc(y, x):
        return y


    for i in range(19, -1,-1):
        if ( not isAnc(pr[x][i], y) ):
            x = pr[x][i]

    return pr[x][0]


def main():
    n, q = 5,5


    for i in range(2, n):
        x = eval(input())
        v[x].append(i)

    tin[0] = -1
    tout[0] = 1E9
    dfs(1, 0)

    for i in range(1, q+1):
        k = eval(input())
        cur = eval(input())
        for i in range(1,k):
            x=eval(input())
            cur = lca(cur, x)

        print( cur)

main()
