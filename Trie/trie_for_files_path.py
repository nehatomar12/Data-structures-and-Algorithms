class TrieNode:
    def __init__(self):
        self.key = None
        self.children = {}
        self.isLeaf = False
        self.count = 0


def make_trie(root, path):
    node = root
    for _file in path.split("/"):
        if _file not in node.children:
            node.children[_file] = TrieNode()
            node.count += 1
        node = node.children[_file]

    node.isLeaf = True
    #node.count += 1
    node.key = path


def printTrie(root):
    for _, node in sorted(root.children.items()):
        if node.key:
            print((node.key))
        printTrie(node)

def find_prefix(root, prefix):
    if not root:
        return False, 0
    node = root
    for p in prefix.split("/"):
        if p not in node.children:
            return False, 0
        node = node.children[p]
    return True, node.count

root = TrieNode()
make_trie(root, 'geeks/for/geeks')
make_trie(root, "hack/athon/works/for/me")
make_trie(root, "hack/athon/like/me")

printTrie(root)
print((find_prefix(root, "hack/athon")))