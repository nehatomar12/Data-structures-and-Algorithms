"""
True:
()[]{}
([{}])
([]{})

False:
([)]
([]
[])
([}))
"""
given = "([]{})"
def balance(given):
    hash = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    s = []
    output = False
    for i in given:
        if i in ("(", "{", "["):
            s.append(i)
        elif len(s) > 0:
            ele = s.pop()
            if ele != hash[i]:
                return output
        else:
            return output
    if len(s) == 0:
        output = True
    return output

print((balance(given)))
