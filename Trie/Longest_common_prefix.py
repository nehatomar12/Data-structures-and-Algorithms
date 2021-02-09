"""
given = ["codable", "code", "coder" , "coding"]

o/p: "cod"
"""
class TrieNode:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.isleaf = False


def insert(root, data):
    node = root
    for char in data:
        if char not in node.children:
            node.children[char] = TrieNode(data)
        node = node.children.get(char)
    node.isleaf = True

def printTrie(root, res=""):
    if not root.children:
        print(res)
        return
    for child, node in list(root.children.items()):
        res = res + child
        printTrie(node, res)
        if root.data == "*":
            res = ""

def LCS(root):
    if not root.children:
        return "-1"
    result = ""
    node = root
    while node and len(node.children) == 1:
        for k, v in list(node.children.items()):
            result += k
            node = v
    return result

root = TrieNode("*")
given = ["codable", "code", "coder" , "coding"]
given = [
        "code", "coder", "coding", "codable", "codec", "codecs", "coded",
        "codeless", "codependence", "codependency", "codependent",
        "codependents", "codes", "codesign", "codesigned", "codeveloped",
        "codeveloper", "codex", "codify", "codiscovered", "codrive"
    ]
for i in given:
    insert(root, i)
#printTrie(root, res="")
print((LCS(root)))
