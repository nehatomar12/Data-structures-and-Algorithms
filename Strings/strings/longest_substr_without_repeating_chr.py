"""
input = "GEEKSFORGEEKS"
output = "EKSFORG"
The desired time complexity is O(n) 
"""
import sys
input = "GEEKSFORGEEKS"
input = "qwertqwer"
input = "ashdfkjahdjkfbbnmbuicae"

"""
step1: create a hash table of {"char": index}
    if char not in hash----add it
    else:
        check if index_of_char in >= temp_strt
            if yes: calculate length and get the start and maxlen update
            else: change chr value in hash_table

END return input[start: start+max_len]

"""
start = 0
max_len = 0
temp_start = 0
hash_table = {}
hash_table[input[0]] = 0
#input = "GEEKSFORGEEKS"
for i in range(1,len(input)):
    if input[i] not in hash_table:
        hash_table[input[i]] = i
    elif hash_table[input[i]] >= temp_start:
        # set the current str and maxlen
        curren_len = i - temp_start
        if max_len < curren_len:
            max_len = curren_len
            start = temp_start
        temp_start = hash_table[input[i]] + 1
    hash_table[input[i]] = i

curren_len = len(input[temp_start:])
if curren_len > max_len: 
    max_len = curren_len
    start = temp_start


if max_len == 0:
    print((len(input))) 
else:
    print( max_len)
    print((input[start: start+max_len]))



