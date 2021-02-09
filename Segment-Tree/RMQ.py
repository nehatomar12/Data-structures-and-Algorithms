
#https://www.hackerearth.com/submission/19441498/
from sys import stdin, stdout


n,m=5,5
t = [0 for i in range(2 * n)]

def build():  # build the tree
    for i in range(n - 1, 0, -1):
        print((i << 1, i << 1 | 1)) # 8-9 6-7 5-4 3-2
        t[i] = min(t[i << 1], t[i << 1 | 1])

def update(p, value):  # set value at position p
    p += n
    t[p] = value
    while p > 1:
        t[p >> 1] = min(t[p], t[p ^ 1])
        p >>= 1


def query(l, r):  # min on interval [l, r)
    res = 10**6+1
    l += n
    r += n
    while l < r:
        if (l & 1):
            res = min(res, t[l])
            l += 1
        if (r & 1):
            res = min(res, t[r-1])
            r -= 1
        l >>= 1
        r >>= 1
    return res

#n, m = map(int, input().split())  # array size, no. of queries

ans = ""

#[0, 0, 0, 0, 0, 1, 5, 2, 4, 3]] Segment tree for internal nodes
t[n: 2 * n] = [1,5,2,4,3] #list(map(int, input().split()))

build()
out = []
for i in range(m):
    a, b, c = input().split()
    b, c = int(b), int(c)
    if a == 'q':
        ans += (str(query(b - 1, c)) + "\n")
    else:
        update(b - 1, c)
stdout.write(ans)

"""
5 5
1 5 2 4 3
q 1 5
q 1 3
q 3 5
u 3 6
q 1 5
"""