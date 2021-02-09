"""
arr = ["Steven XL",  "Mary XX","Mary XIII","David IX","Steven XVI", "Mary XV"]
arr = ["Steven 40", "Steven 10+5+1", "Mary 15",
    "Mary 20","Mary 13","David 1-10"]

XL == X !> L == abs(X-L)
"""
from collections import defaultdict
from itertools import groupby
arr = ["Steven XL",  "Mary XX", "Mary XIII",
       "David IX", "Steven XVI", "Mary XV"]
map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "XL": 40,
    "L": 50
}

ordered_map = defaultdict()

arr.sort()
for j, i in groupby(arr, lambda a: a.split(' ')[0]):
    ordered_map[j] = [ii.split(" ")[1] for ii in list(i)]

print(ordered_map)
result = []
for k, v in list(ordered_map.items()):
    print((k, v))
    for s in v:
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i] in map:
            num+=s[i]
            i+=1
         else:
            # print(i)
            num+=map[s[i]]
            i+=1
      print(num)
