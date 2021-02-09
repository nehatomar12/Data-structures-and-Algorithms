"""
The cost of stock on each day is given in an array A[] of size N.
Find all the days on which you buy and sell the stock
so that in between those days your profit is maximum.

N = 7
A[] = {100,180,260,310,40,535,695}
    Output: (0 3) (4 6)
Explanation: We can buy stock on day
0, and sell it on 3rd day, which will
give us maximum profit. Now, we buy
stock on day 4 and sell it on day 6.

N = 5
A[] = {4,2,2,2,4}
Output: (3 4)

steps:
    Find the local minima and store it as starting index. If not exists, return.
    Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
    Update the solution (Increment count of buy sell pairs)
    Repeat the above steps if end is not reached.

{100,180,260,310,40,535,695}
i=0
local_minima = arr[i] >= arr[i+1] {i++} else 100 !> 180 buy=i,i++
local_maxima = arr[i] >= arr[i-1] {i++} else i=4(40) sell = i-1

i=4
local_minima = arr[i] >= arr[i+1] {i++} else 40 !> 535 buy=i,i++
local_maxima = arr[i] >= arr[i-1] {i++} else i=4(40) sell = i-1

"""

def stock_buy_sell(arr, n):
    if n == 0:
        return

    i =0
    while i < n-1:
        #local minima
        while i < n-1 and arr[i] >= arr[i+1]:
            i += 1

        if i == n-1:
            break
        buy = i
        i += 1

        #local maxima
        while i < n and arr[i] >= arr[i-1]:
            i += 1
        sell = i-1

        print((buy, sell))



if __name__ == "__main__":
    arr =[100,180,260,310,40,535,695]
    arr = [4,2,2,2,4]
    stock_buy_sell(arr, len(arr))