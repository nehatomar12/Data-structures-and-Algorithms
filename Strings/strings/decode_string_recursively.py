"""
Input : str[] = "1[b]"
Output : b

Input : str[] = "2[ab]"
Output : abab

Input : str[] = "2[a2[b]]"
Output : abbabb

Input : str[] = "3[b2[ca]]"
Output : bcacabcacabcaca
"""

inp="2[ab]"
stack1=[] #-----> add no
stack2=[] #------> add char

for i in inp:
    if i in ["1","2","3","4","5","6","7","8","9"]:
        stack1.append(i)
    elif i in "["
