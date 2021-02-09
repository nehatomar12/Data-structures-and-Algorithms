"""
geeksforgeek
acaaabbbacdddd

Output:
gksforgk
acac

"""


def removeAdjDup(str):
    chars = list(str)
    prev_index = 0     # prev index
    prev_value = chars[0]  # value
    i = 1
    while i < len(str):
        if prev_value != str[i]:
            prev_index += 1
            chars[prev_index] = chars[i]
            i += 1
            prev_value = chars[prev_index]
        else:
            while i < len(str) and prev_value == str[i]:
                i += 1
            prev_index -= 1  # update prev index
            prev_value = chars[prev_index]
    print("------>", str)
    return "".join(chars[:prev_index+1])


def removedup(str):
    res = str[0]
    pindex = 0
    pval = str[0]
    i = 1
    while i < len(str):
        if str[i] == pval:
            while i < len(str) and str[i] == pval:
                i += 1
        if i < len(str):
            pval = str[i]
            pindex += 1
            res += pval
            i += 1
    print("*****" ,res)

if __name__ == '__main__':

    str = "ABDAADBDAABB"
    str = "geeksforgeeks"
    str = removeAdjDup(str)
    print(str)
    removedup("geeksforgeeks")
