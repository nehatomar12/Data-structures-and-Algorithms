"""
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA
ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS BGSA BSAG BSGA
GABS GASB GBAS GBSA GSAB GSBA SABG SAGB SBAG SBGA SGAB SGBA

use backtracking
                        ABSG  --> swap A with all other letters and first letter will be fixed
        ABSG    BASG    SBAG    GBSA ---> now BSG,ASG,BAG,BSA is to follow the same

    ABSG        BASG    SBAG    ...  -> here 2 letters are fixed
    ASBG        BSAG    SABG
    AGSB        BGSA    SGAB

continue till only one letter is left

    (A swap         A is fixed
    with others)    B and C swap   results
    ABC                 ABC         ABC,ACB
    BAC                 BAC         BAC, BCA
    CBA                 CBA         CBA, CAB


Steps:
    1. swap A with all other letters and first letter will be fixed
    2. continue till one letter remains
"""

def permutation_of_str(given, l, r):
    if l == r:
        print(("".join(given)))
    else:
        for i in range(l,r):
            given[i], given[l] = given[l],given[i]
            permutation_of_str(given, l+1, r)
            given[i], given[l] = given[l],given[i]

given="ABC"
permutation_of_str(list(given), 0, len(given))
