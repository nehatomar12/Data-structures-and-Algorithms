class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

prev = None

def isbst_rec(root):
    global prev
    if root is None:
        return True
    if not isbst_rec(root.left):
        return False
    if prev and prev.data >= root.data:
        return False
    prev = root
    return isbst_rec(root.right)


def isBST(root):
    if isbst_rec(root):
        return True
    return False


if __name__ == '__main__':
    root = Node(3)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.right.left = Node(4)
    #root.right.left.left = Node(40)

    if (isBST(root)):
        print("Is BST --> 1 ")
    else:
        print("Not a BST --> 0")
