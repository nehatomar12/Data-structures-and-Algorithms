#This is the complexity of the sorting algorithm which we are using
# after first in-order traversal, rest of the opertions take place in linear time.
# space (n)
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


# Function to traverse the binary tree and store its keys in a set
def extractKeys(root, set):
    # base case
    if root is None:
        return
    extractKeys(root.left, set)
    set.add(root.data)
    extractKeys(root.right, set)


# Function to put back keys in set in their correct order in BST
# by doing in-order traversal
def convertToBST(root, it):
    if root is None:
        return
    convertToBST(root.left, it)
    root.data = next(it)
    convertToBST(root.right, it)


if __name__ == '__main__':

    """ Construct below tree
              8
            /   \
           /     \
          3       5
         / \     / \
        /   \   /   \
       10    2 4     6
    """

    root = Node(8)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(10)
    root.left.right = Node(2)
    root.right.left = Node(4)
    root.right.right = Node(6)

    # traverse the binary tree and store its keys in a set
    s = set()
    extractKeys(root, s)

    # put back keys present in set in their correct order in BST
    it = iter(s)
    convertToBST(root, it)

    # print the BST
    inorder(root)
