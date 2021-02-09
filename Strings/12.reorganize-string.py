from collections import Counter
"""
Input:
"ogccckcwmbmxtsbmozli"
Output:
"cgcickclmsmtmwbxbzoo"
Expected:
"cocgcickmlmsmtbwbxoz"
"""

def reorganizeString(S):
    """
    mid of the positions,
    half of the length.
    """
    smaller_mid = (len(S) - 1) // 2
    # larger_mid = len(S) // 2
    # smaller_half = len(S) // 2
    larger_half = (len(S) + 1) // 2

    counter = Counter(S)

    if max(counter.values()) >= larger_half + 1:
        return ""

    sorted_string = ""

    for key, value in sorted(counter.items(), key=lambda item: -item[1]):
        sorted_string += key * value

    res = ""
    lo, hi = 0, smaller_mid + 1


    while True:
        if lo == smaller_mid + 1:
            break
        # res += sorted_string[lo] + \
        #     sorted_string[hi] if hi <= len(S) - 1 else sorted_string[lo]
        if hi <= len(S) - 1:
            res += sorted_string[lo] + sorted_string[hi]
        else:
            res += sorted_string[lo]
        lo += 1
        hi += 1

    print(res)
    return res

reorganizeString(S="aaabbaeee")
reorganizeString(S="aaab")
reorganizeString(S="aab")
