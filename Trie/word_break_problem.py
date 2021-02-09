

#https://leetcode.com/problems/word-break/discuss/490911/Python-Simple-Trie-solution-with-detailed-explanation-and-sketches
from pprint import pprint
from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_done = False


class Trie:
    def __init__(self):
        self.root = Node(None)
        self.memo = {}

    def add(self, word):
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = Node(char)
            root = root.children[char]
        root.is_done = True


    """
        {'': False,
        'akproblem': True,
        'breakproblem': True,
        'eakproblem': True,
        'kproblem': True,
        'lem': True,
        'problem': True,
        'reakproblem': True}
    """
    def find(self, s):
        root = self.root # set to None
        for i, char in enumerate(s):
            if char not in root.children:
                return False

            if root.children[char].is_done:
                # -- (a) if the remaining part hasn't been seen before, then we need to check it -> call the function recursively
                if s[i+1:] not in self.memo:
                    self.memo[s[i+1:]] = self.find(s[i+1:])

                # -- (b) if remaining has been seen - return True (no need to check)
                if self.memo[s[i+1:]]:
                    return True
                    # for example:
                    # A man gotta do what a man gotta do
                    # ex: s = "Amangottadowhatamangottado"
                    # The words "man", "do", "gotta", and "a" repeats twice each
                    # in such scenario, it's wise to use a memoization dict to speed things up - see sketch 3

            root = root.children[char]
        pprint(vars(root))
        return root.is_done


def wordBreak(s, wordDict):
    trie = Trie()
    for word in wordDict:  # ------ O(W) where W = len(words)
        trie.add(word)  # --------------- O(K) where K = len(word)
    # print(trie.root.children)
    # Words have been added. Find if s is made up of words in the trie
    # ---- Overall time : O(W*K) OR O(S*S[i+1:]) Whichever is worst
    val= trie.find(s)
    pprint(trie.memo)
    return val

dict = ["self", "th", "is", "famous",
        "word", "break", "b", "r", "e", "a", "k",
        "br", "bre", "brea", "ak", "prob", "lem"]
str = "wordbreakproblem"

#print((wordBreak(str, dict)))

str = "bedbathandbeyond"
dict = ["teddy", "bath", "bedbath", "and", "beyond"]
print((wordBreak(str, dict)))
