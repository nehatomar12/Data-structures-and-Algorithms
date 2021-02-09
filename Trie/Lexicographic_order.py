class TrieNode:
    def __init__(self):
        self.children = {}
        self.isleaf = False
        self.key = None


def insert(root, data):
    node = root
    for char in data:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children.get(char)
    node.isleaf = True
    # Fill data in last node
    node.key = data

def printTrie(root):
    for _, node in sorted(root.children.items()):
        if node.key:
            print((node.key))
        printTrie(node)

root = TrieNode()
given = ["lexicographic", "sorting", "of", "a", "set", "of", "keys", "can", "be",
        "accomplished", "with", "a", "simple", "trie", "based", "algorithm",
        "we", "insert", "all", "keys", "in", "a", "trie", "output", "all",
        "keys", "in", "the", "trie", "by", "means", "of", "preorder",
        "traversal", "which", "results", "in", "output", "that", "is", "in",
        "lexicographically", "increasing", "order", "preorder", "traversal",
        "is", "a", "kind", "of", "depth", "first", "traversal"]
for i in given:
    insert(root, i)
printTrie(root)