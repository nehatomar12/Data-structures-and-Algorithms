"""
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)


"""
s1 = "ABCD"
s2 = "CDAB"
s2 = "CDBA"

temp = s1+s1
if s2 in temp:
    print(True)
else:
    print(False)
