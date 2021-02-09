"""
Input  :  str = 'wwwwaaadexxxxxx'
Output : 'w4a3d1e1x6'
"""
str = 'wwwwaaadexxxxxx'
from collections import OrderedDict
hash = OrderedDict({})

for i in str:
   hash[i] = hash.get(i,0) + 1

for k,v in hash.items():
    print("%s%s" % (k,v),end="")