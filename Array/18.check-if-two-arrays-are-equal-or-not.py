"""
Given two arrays A and B of equal size, the task is to find if given arrays are equal or not.

output: 1 == equal, 0 == not equal
Steps:
    create hash for array1
    traverse array2 and check the values of hash calculated

"""
from collections import defaultdict

arr1 = [1, 2, 5, 4, 0]
arr2 = [2, 4, 5, 0, 1]
ans = 1
hash1 = defaultdict(int)
for i in arr1:
    hash1[i] += 1
for i in arr2:
    if not hash1[i]:
        ans = 0
        break
    hash1[i] -= 1

print(ans)