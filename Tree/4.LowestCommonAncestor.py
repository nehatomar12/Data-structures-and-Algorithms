
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find(root, k):
    # Base Case
    if root is None:
        return False
    # If data is present at root, or if left subtree or right
    # subtree , return true
    if (root.data == k or find(root.left, k) or
        find(root.right, k)):
        return True
    # Else return false
    return False

def LCA(root, v1, v2):
    if root is None:
        return None

    if root.data == v1 or root.data == v2:
        return root

    ls = LCA(root.left, v1, v2)
    rs = LCA(root.right, v1, v2)

    if ls and rs:
        return root
    return ls if ls else rs


if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    if find(root, 4) and find(root, 2):
        print((LCA(root, 4, 8).data))
    else:
        print("data not found")
