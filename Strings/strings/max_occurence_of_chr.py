
str = "geeksggggghhhhhhhh"

chr_set = [0]*256

for i in str:
    chr_set[ord(i)] += 1

max = -1
for i in str: 
    if max < chr_set[ord(i)]: 
        max = chr_set[ord(i)] 
        c = i 

print(c)