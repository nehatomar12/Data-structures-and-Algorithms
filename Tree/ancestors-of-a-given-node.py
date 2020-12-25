class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right= None

def printAncestors_01(root, key, s):
    #method 1
    if not root:
        return False

    s.append(root.data)
    if root.data == key:
        print((s[:-1]))
    printAncestors_01(root.left,key, s)
    printAncestors_01(root.right,key,  s)
    s.pop()

def printAncestors_02(root, key):
    #method 2 pre-order
    if not root:
        return False

    if root.data == key:
        return True

    if printAncestors_02(root.left,key) or printAncestors_02(root.right,key):
        print((root.data))
        return True




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
printAncestors_01(root, 7, [])
printAncestors_02(root, 7)