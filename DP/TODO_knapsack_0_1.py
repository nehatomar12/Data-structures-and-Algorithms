"""
# https://www.youtube.com/watch?v=nLmhmB6NzcM
# https://www.youtube.com/watch?v=zRza99HPvkQ

"""
def knapSack(W, wt, val, n):

    k = [[None]* (W +1) for r in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                k[i][w] = 0
            elif wt[i-1] <= w:
                k[i][w] = max(val[i-1] + k[i-1][w-wt[i-1]],  k[i-1][w]) 
            else: 
                k[i][w] = k[i-1][w] 
    
    i = n
    j = W
    # i=4,3 , j=8-5, 3
    while i > 0 and j >= 0:
        # if  k[i][j] == k[i-1][j] dont include the element
        if k[i][j] != k[i-1][j]:
            print(wt[i-1] , "Included")
            j = j-wt[i-1]
        i -= 1
        
    return k[n][W] 


# Driver program to test above function 
p = [1,2,5,6] #[60, 100, 120] 
wt = [2,3,4,5] #[10, 20, 30] 
W = 8 #50
n = len(p) 
print((knapSack(W, wt, p, n)))