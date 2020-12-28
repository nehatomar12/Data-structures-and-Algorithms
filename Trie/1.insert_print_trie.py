class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False
        self.key = None
        #optional
        self.counter = 0

def make_trie(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children.get(char)
    node.isLeaf = True
    node.key = word
    node.counter += 1

def printTrie(root):
    for _, node in sorted(root.children.items()):
        if node.key:
            print((node.key))
        printTrie(node)

root = TrieNode()
make_trie(root, "This")
make_trie(root, "That")
make_trie(root, "The")
make_trie(root, "Those")

printTrie(root)
