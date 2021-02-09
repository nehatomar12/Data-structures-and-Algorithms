"""
Given a dictionary of words where each word follows a CamelCase notation,
find all words in the dictionary which match with the given
pattern consisting of all uppercase characters.

dict = [Hi, HiTech, HiTechCity, Hello, HelloWorld, HiTechLab]
 
* If the pattern is HT, the output is { HiTech, HiTechCity, HiTechLab }
* If the pattern is HTC, the output is { HiTechCity }
* If the pattern is H, the output is the same as the input

Algo:

"""

from pprint import pprint
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False
        self.key = []
        #optional
        self.counter = 1


def make_trie(root, word):
    node = root
    for char in word:
        if char.isupper():
            node.children[char] = TrieNode()
            node = node.children.get(char)
    node.isLeaf = True
    node.key.append(word)
    print(node.key)


def onlyprintTrie(root):
    if not root:
        return
    if root.isLeaf:
        print(root.key)
    for node in root.children.values():
        onlyprintTrie(node)

def printTrie(root, pattern):
    node = root
    #pprint( node.children)
    for i in pattern:
        if i not in node.children:
            return
        pprint(vars(node))
        node = node.children[i]



given = ["Hi", "HiTech", "HiTechCity", "Techie", "TechieDelight",
		"Hello", "HelloWorld", "HiTechLab"]
pattern = "HT"
root = TrieNode()
for w in given:
    make_trie(root, w)

onlyprintTrie(root)