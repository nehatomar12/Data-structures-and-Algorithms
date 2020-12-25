#https://www.techiedelight.com/fix-binary-tree-one-swap-bst/
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def swapData(first, second):
    first.data, second.data = second.data, first.data

# Recursive function to insert a key into BST
def insert(root, key):
    # if the root is None, create a node and return it
    if root is None:
        return Node(key)

    # if given key is less than the root node, recur for left subtree
    if key < root.data:
        root.left = insert(root.left, key)

    # if given key is more than the root node, recur for right subtree
    else:
        root.right = insert(root.right, key)

    return root

def fixBST(node, x ,y, prev):
    if not node:
        return x, y, prev

    x, y, prev = fixBST(node.left, x, y, prev)

    if prev and node.data < prev.data:
        if not x:
            x = prev
        y = node
    prev = node
    return fixBST(node.right, x, y, prev)


if __name__ == "__main__":
    """ Construct below BST
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
    """

    keys = [15, 10, 20, 8, 12, 16, 25]

    root = None
    for key in keys:
        root = insert(root, key)
    inorder(root);print()
    # swap any two nodes values
    swapData(root.left, root.right.right)
    inorder(root);print()
    # fix the BST
    # 2 variable which is swaped x y = None
    # prev to store previous node = None
    x, y, prev =None,None, None
    x, y, prev = fixBST(root,x,y,prev )
    if x:
        swapData(x, y)
    # print the BST after fixing it
    inorder(root);print()