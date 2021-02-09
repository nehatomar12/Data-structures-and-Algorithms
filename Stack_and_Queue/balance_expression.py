

exp = "{([])}"
#exp = "{([])}}"
exp = "{}{(}))}"

def check_exp(exp):
    s = []
    for i in exp:
        if i in ("{", "[", "("):
            s.append(i)
        else:
            if not s:
                return False
            curr_char = s.pop()
            if i == "}":
                if curr_char != "{":
                    return False
            if i == "]":
                if curr_char != "[":
                    return False
            if i == ")" :
                if curr_char != "(" :
                    return False
    if s:
        return False
    return True


# num = input()

# for i in range(0, int(num)):
#     exp = input()
#     check_exp(exp)

if check_exp(exp):
    print("balanced")
else:
    print("not balanced")
