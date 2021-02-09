"""
https://www.geeksforgeeks.org/sum-of-all-substrings-of-a-string-representing-a-number/

Example : num = "1234"
sumofdigit[0] = 1 = 1
sumofdigit[1] = 2 + 12  = 14
sumofdigit[2] = 3 + 23  + 123 = 149
sumofdigit[3] = 4 + 34  + 234 + 1234  = 1506
Result = 1670

sumofdigit[3] = 4 + 34 + 234 + 1234
           = 4 + 30 + 4 + 230 + 4 + 1230 + 4
           = 4*4 + 10*(3 + 23 +123)
           = 4*4 + 10*(sumofdigit[2])
In general,
sumofdigit[i]  =  (i+1)*num[i] + 10*sumofdigit[i-1]
"""

def sumOfSubstrings(num) :
    n = len(num)
    prev = int(num[0])
    res = prev
    current = 0
    for i in range(1, n) :
        numi = int(num[i])
        current = (i + 1) * numi + 10 * prev
        res += current
        prev = current # update previous

    return res

num = "1234"
print(sumOfSubstrings(num))
