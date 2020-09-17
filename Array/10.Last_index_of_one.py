"""
Given a string S consisting only '0's and '1's,  print the last index of the '1' present in it.

"""

input_str = "00001000"
ans = -1
for i in range(len(input_str)-1, -1,-1):
    if input_str[i] == "1":
        ans = i
        break
print(ans)