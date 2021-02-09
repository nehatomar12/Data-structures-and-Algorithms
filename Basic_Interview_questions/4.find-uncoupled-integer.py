"""
arr = [1, 2, 3, 4, 5, 99, 1, 2, 3, 4, 5]
output = 99

"""
arr = [1, 2, 3, 4, 5, 99, 1, 2, 3, 4, 5]
r = 0
for i in arr:
    r ^= i
print(r)