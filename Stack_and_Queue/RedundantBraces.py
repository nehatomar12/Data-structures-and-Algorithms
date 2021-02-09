"""
Given a string A denoting an expression. It contains the following operators ’+’, ‘-‘, ‘*’, ‘/’.

Chech whether A has redundant braces or not.

Return 1 if A has redundant braces, else return 0.

Note: A will be always a valid expression.
Input 1:
    A = "((a + b))"
Output 1:
    1
    Explanation 1:
        ((a + b)) has redundant braces so answer will be 1.

Input 2:
    A = "(a + (a + b))"
Output 2:
    0
"""
A = "((a + b))"
A = "(a + (a + b))"
#A = "(a)"
#A = " ((a+b-c)*c)"
def braces():
    res = True
    s = []
    top = -1
    temp = ""
    for i in A:
        if i != " ":
            s.append(i)
            top += 1
        if top != -1 and s[top] == ')':
            s.pop()
            top -= 1
            while top != -1 :
                if s[top] == "(":
                    break
                temp += s.pop()
                top -= 1
            s.pop()
            top -= 1
            if temp and len(temp) > 1:
                temp =""
            else:
                res = False

    if res:
        return 0
    return 1

print((braces()))
