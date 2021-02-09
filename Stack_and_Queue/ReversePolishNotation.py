"""
https://blog.klipse.tech/python/2016/09/22/python-reverse-polish-evaluator.html
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.
"""


def evalRPN(A):
    s = []
    ops_map = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a // b
    }
    for elem in A:
        if elem in ops_map:
            b = s.pop()
            a = s.pop()
            s.append(ops_map[elem](int(a), int(b)))
        else:
            s.append(elem)
    return int(s[0])


A = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
A = [ "4", "13", "5", "/", "+" ]
print((evalRPN(A)))
