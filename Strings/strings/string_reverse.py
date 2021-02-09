
# Reverse a string in-place
given = "Neha Tomar"
given = "ABC"

def reverse(given):
    res = ""
    for i in range(len(given)-1,-1,-1):
        res = res + given[i]
    print("Reversed string: ", res)

result = ""
def reverse_using_recurrsion(given):
    if len(given) == 0:
        return
    reverse_using_recurrsion(given[1:])
    print(given[0], end=' ')

def all_words_without_using_lib_fun(given="geeks for geeks"):
    res = ""
    tmp = ""
    for i in range(0, len(given)):
        if i == len(given)-1:
            res = res + tmp + given[i] + " "
            print(res)
            return
        if given[i] == " ":
            res = res + tmp + " "
            tmp = ""
        else:
            tmp = given[i] + tmp


def rev(test):
    if len(test) == 0:
        return test
    return rev(test[1:]) + test[0]


# reverse(given)
# print given[::-1] # ramoT aheN
#reverse_using_recurrsion(given)
all_words_without_using_lib_fun()
print(rev("geeks for geeks"))