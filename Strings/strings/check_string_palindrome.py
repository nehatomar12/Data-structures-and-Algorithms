"""
Input : malayalam
Output : Yes

Input : geeks
Output : No
"""

input = "malayalam"
input = "geeks"
n = len(input)
i = 0
j = n-1

is_palindrome = True
while i < j:
    if input[i] == input[j]:
        i += 1
        j -= 1
    else:
        is_palindrome = False
        break

print("String palindrome: ", is_palindrome)

if input == input[::-1]:
    print("Yes palindrome")
else:
    print("Not palindrome")
    