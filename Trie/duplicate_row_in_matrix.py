"""


"""

result = {}
class TrieNode:
    def __init__(self, data):
        self.children = {}
        self.isleaf = False
        self.key = None


def insert(root, data):
    node = root
    for char in data:
        if char not in node.children:
            node.children[char] = TrieNode(data)
        node = node.children.get(char)

    # check for dupicate row
    if node.isleaf:
        return False

    node.isleaf = True
    # Fill data in last node
    node.key = data
    return True

def printTrie(root):
    global result
    for _, node in sorted(root.children.items()):
        if node.key:
            print((node.key))
        printTrie(node)


root = TrieNode("*")
mat = [
		[1, 0, 0, 1, 0],
		[0, 1, 1, 0, 0],
		[1, 0, 0, 1, 0],
		[0, 0, 1, 1, 0],
		[0, 1, 1, 0, 0]
	]

for _, row in enumerate(mat):
    if not insert(root, row):
        print(("Row: ", row, " is Duplicate"))
