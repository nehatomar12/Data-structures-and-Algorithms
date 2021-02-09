"""
keys = ["code", "coder", "coding", "codable", "codec", "codecs", "coded",
		"codeless", "codec", "codecs", "codependence", "codex", "codify",
		"codependents", "codes", "code", "coder", "codesign", "codec",
		"codeveloper", "codrive", "codec", "codecs", "codiscovered"]

k = 4

 o/p:
    codec occurs 4 times
    codecs occurs 3 times
    coder occurs 2 times
    code occurs 2 times

"""


class TrieNode:
    def __init__(self, data):
        self.children = {}
        self.isleaf = False
        self.key = None
        self.count = 0


def insert(root, data):
    node = root
    for char in data:
        if char not in node.children:
            node.children[char] = TrieNode(data)
        node = node.children.get(char)
    node.isleaf = True
    node.count += 1
    # Fill data in last node
    node.key = data

def printTrie(root):
    global result
    for _, node in sorted(root.children.items()):
        if node.key:
            if result.get(node.count):
                result[node.count].append(node.key)
            else:
                result[node.count] = [node.key]
        printTrie(node)


root = TrieNode("*")
result = {}
given = [
		"code", "coder", "coding", "codable", "codec", "codecs", "coded",
		"codeless", "codec", "codecs", "codependence", "codex", "codify",
		"codependents", "codes", "code", "coder", "codesign", "codec",
		"codeveloper", "codrive", "codec", "codecs", "codiscovered"
    ]
for i in given:
    insert(root, i)

printTrie(root)
print(result)
k = 6
# for key, v in sorted(result.items(), reverse=True):
#     for values in v:
#         if k == 0:
#             break
#         print(values, " occurs ", key, " times ")
#         k -= 1
for k, v in sorted(list(result.items()), reverse=True):
    print((v, " occurs ", k, " times "))
