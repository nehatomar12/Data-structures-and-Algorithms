

# List all substrings

#Approach1 
# string comprehension and slicing
str = "geeks"
n = len(str)
all_substr = []
for i in range(0,n):
    for j in range(1,n+1):
        all_substr.append(str[i:j])
#print all_substr

str = "geeks"
from itertools import combinations 
res = [str[x:y] for x, y in combinations( 
            list(range(len(str) + 1)), r = 2)] 
print(res)

# for x, y in combinations(range(len(str) + 1), r=2):

#     print x,y
"""
0 1
0 2
0 3
0 4
0 5
1 2
1 3
1 4
1 5
2 3
2 4
2 5
3 4
3 5
4 5
"""
