"""
Input : str = "aabb"
Output : Yes

Input : str = "abab"
Output : No

"""

def validate(s):
    for i in range(0, len(s)):
        if s[i] != "a":
            break
    if i*2 != len(s):
        print(("{}: No".format(s)))
        return
    for j in range(i, len(s)):
        if s[j] != "b":
            print(("{}: No".format(s)))
            return
    print(("{}: Yes".format(s)))



if __name__ == "__main__":
    input_strs = ["aabb", "abab", "aabbb"]
    for s in input_strs:
        validate(s)