"""
Input : str = "geeks for geeks121"
Output : Vowels: 5
         Consonant: 8
         Digit: 3
         Special Character: 2
"""
s1 = "geeks for geeks121"
v,c,d,sp=0,0,0,0
vowels = ['a','e','i','o','u']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

for s in s1:
    if s in vowels:
        v += 1
    elif s in consonents:
        c += 1
    elif s in numbers:
        d += 1
    else:
        sp += 1

print(("Vowels: ",v))
print(("Consonents ",c))
print(("Special ",sp))
print(("Digits ",d))