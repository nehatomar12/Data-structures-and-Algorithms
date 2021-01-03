class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def isMirror(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data == root2.data:
        return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
    return False

def isSymmetric(root):
    return isMirror(root, root)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print(("1" if isSymmetric(root) == True else "0" ))
