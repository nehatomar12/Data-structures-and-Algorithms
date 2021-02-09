name = "geeksforgeeks"
name = "nneha"

def duplicate_with_variable():
    res = ""
    for i in name:
        if i not in res:
            res = res + i
    print(res)

print()

def duplicate_using_map():
    hash = [0]*256
    for i in name:
        hash[ord(i)] += 1
    for i in range(256):
        if hash[i] > 1:
            print(chr(i), end=' ')



duplicate_with_variable()
duplicate_using_map()
