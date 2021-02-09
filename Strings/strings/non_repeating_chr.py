"""
Input : str = geeksforgeeks, k = 3
Output : r
First non-repeating character is f,
second is o and third is r.

Input : str = geeksforgeeks, k = 2
Output : o

Input : str = geeksforgeeks, k = 4
Output : Less than k non-repeating
         characters in input.
"""
str = "geeksforgeeks"
#tr = "geks"
def k_th_non_repeating_chr(k):
    """
    Step1: create 2 array one to store count of variable and other index
    count = []*256
    index = []*256

    Step2: travese given value and increment count, if count==1, mark index value
    if count is greater then 1 the chr is repeated so unmark the index

    Step3: sort index array
    return value for k-1

    """
    index = [len(str)] * 256
    count = [0] * 256

    for i in range(len(str)):
        count[ord(str[i])] += 1

        if count[ord(str[i])] == 1:
            index[ord(str[i])] = i
        else: #count[ord(str[i])] == 2:
            index[ord(str[i])] = len(str)

    index = sorted(index)
    # if k-1 is != to max set value
    # return else -1
    #print(index)
    if index[k-1] != len(str):
        return str[index[k-1]]
    else:
        return -1



def non_rep(k):
    count = [0] * 256
    index = [len(str)] * 256

    for i, s in enumerate(str):
        count[ord(s)] += 1
        if count[ord(s)] == 1:
            index[ord(s)] = i
        else:
            index[ord(s)] = len(str)
    index = sorted(index)
    return str[index[k-1]] if index[k-1] != len(str) else -1


from collections import Counter
#print(Counter(str))
print(k_th_non_repeating_chr(1), non_rep(1))

print(k_th_non_repeating_chr(2), non_rep(2))
print(k_th_non_repeating_chr(4), non_rep(4))
