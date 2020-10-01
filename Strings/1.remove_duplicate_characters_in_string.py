"""
word = "geeksforgeeks"
output = "geksfor"
"""


def remove_duplicate(word):
    hash = [0] *256
    result = ""
    for letter in word:
        if hash[ord(letter)] == 0:
            result += letter
            hash[ord(letter)] += 1
    print(result)

if __name__ == "__main__":
    word = "geeksforgeeks"
    remove_duplicate(word)
    # A shorter version for this program is as follows
    # import collections
    # print ''.join(collections.OrderedDict.fromkeys(string))
    # >>> collections.OrderedDict.fromkeys(word).keys()
    # odict_keys(['g', 'e', 'k', 's', 'f', 'o', 'r'])
