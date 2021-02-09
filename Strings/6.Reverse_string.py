
def reverse_words(string):
    res = ""
    for s in string.split("."):
        res =  s + "."+ res
    print((res[:-1]))


s1 = "ReverseMe"

def reverse(s1):
    if len(s1) == 0:
        return s1
    return reverse(s1[1:]) + s1[0]
print((reverse(s1)))

reverse_words(string="i.like.this.program.very.much")
