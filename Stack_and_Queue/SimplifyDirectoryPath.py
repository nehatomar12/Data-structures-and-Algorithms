A = "/a/./b/../../c/"
A = "/home//foo/"
"""
check for elements  / . .. "" and add to stack
for printing pop each element of stack
"""
def simplifyPath(A):
    s = []
    top = -1
    for i in A.split("/"):
        if i == "..":
            if top != -1:
                s.pop(top)
                top -= 1
        elif i == "." or i == "":
            pass
        else:
            s.append(i)
            top += 1
    res = "/"
    for element in range(len(s)):
        if top == 0:
            return res + s[element]
        res += s[element] + "/"
        top -= 1
    return res

print((simplifyPath(A)))