import math
#https://github.com/rocket-ron/Python-stuff/blob/master/scramble.py
# https://gist.github.com/skyful/8203629
# https://github.com/joric/interviewbit/blob/master/programming/dynamic-programming/scramble-string.md

# interleave two equal length strings, or at most a length of 1 difference in lengths
# interleaving is defined as taking 1 character from each string, starting from the beginning
# of the string to the end, alternating from string1 to string2.
def interleave(s1, s2):
    if (len(s1) + len(s2)) <= 2:
        return s1 + s2
    else:
        result = ""
        for i in range(0, min(len(s1), len(s2))):
            result += s1[i] + s2[i]

        # take care of the case that one sring is longer than the other by 1 character
        if len(s1) > len(s2):
            result += s1[len(s1)-1]
        elif len(s2) > len(s1):
            result += s2[len(s2)-1]
        return result


# scramble a string by splitting it into two halves and interleaving the halves
def scramble(x):
    if len(x) <= 2:
        return x
    else:
        ss = split(x)
        return interleave(scramble(ss[0]), scramble(ss[1]))


# split a string into two parts. If the string is odd length, the first "half" wil
# be 1 larger than the second "half"
def split(x):
    if len(x) > 2:
        if len(x) % 2 == 0:
            return x[:len(x) // 2], x[len(x) // 2:]
        else:
            return x[:len(x) // 2 + 1], x[len(x) // 2 + 1:]
    elif len(x) == 2:
        return x[0], x[1]
    else:
        return x,


# determine the next power of 2 equal or larger to the length of the string
# and pad the string to that length.
def pad_to_power_of_2(x):
    i = 0
    size = len(x)
    while math.pow(2, i) < size:
        i += 1
    return x + ' ' * (pow(2, i) - size)


# s = str(input('Enter a string: '))
# print(scramble(s))
# print(scramble(pad_to_power_of_2(s)))
print((scramble("great")))
