"""
An anagram of a string is another string that contains same characters,
only the order of characters can be different
For example, “abcd” and “dabc” are anagram of each other.

"""
def is_anagram(s1, s2):
    hash1 = [0]*256
    for i in s1:
        hash1[ord(i)] += 1
    for i in s2:
        hash1[ord(i)] -= 1
    for i in range(256):
        if hash1[i] != 0:
            return False
    return True

def print_anagrams(arr):
    from collections import defaultdict

    group_anagram = defaultdict(list)

    for a in arr:
        group_anagram["".join(sorted(a))].append(a)

    print(list(group_anagram.values()))


if __name__ == "__main__":
    s1 = "abcd"
    s2 = "adcb"
    print(is_anagram(s1, s2))

    arr =  ["cat", "dog", "tac", "god", "act"]
    # Print all anagram together
    print_anagrams(arr)
