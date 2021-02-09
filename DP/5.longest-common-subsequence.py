"""
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


3 cases:
1. if i or j ==0
    lcs = 0
2. if same, move diagonally
3. if not, move parallel to i, j
"""

def lcs(a, b):
    m=len(a)
    n=len(b)
    lcs = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                lcs[i][j] = 0
            elif a[i-1]==b[j-1]:
                lcs[i][j]=1+lcs[i-1][j-1]
            else:
                lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])

    print(lcs[-1][-1])
    print_sequence(lcs,m,n,a,b)

def print_sequence(L,rows,cols,A,B):
    # Print the subsequence
    res = [""]*(L[rows][cols] +1)

    res_index = len(res)
    # Traverse both string from right side
    # compare values from L table
    i = len(A)
    j = len(B)
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            res[res_index-1] = A[i-1]
            i -= 1
            j -= 1
            res_index -= 1
        # compare value in tables
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    print(("".join(res)))


lcs(a="bd", b="abcd")
