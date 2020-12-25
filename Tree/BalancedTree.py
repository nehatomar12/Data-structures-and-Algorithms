"""
Best explained: https://algorithms.tutorialhorizon.com/find-whether-if-a-given-binary-tree-is-balanced/
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def isBalanced(root):
    # Do post-order treaversal
    # Get Lh and Rh
    # get diff if not 1 return False
    # return height i.e max(lh,rh)+1
    if root is None:
        return 0
    lh = isBalanced(root.left)
    rh = isBalanced(root.right)

    if (rh or lh ) == -1:
        return -1

    diff = abs(lh-rh)

    if diff > 1:
        return -1
    return max(lh,rh) + 1

# Driver function to test the above function
"""
Constructed binary tree is
            1
        / \
        2     3
    / \ /
    4 5 6
/
7
"""
# to store the height of tree during traversal

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right.left = Node(7)
# root.right.right = Node(7)
# root.right.right.right = Node(12)


root = Node(9)
root.left = Node(7)
root.left.left = Node(8)
root.left.right = Node(10)
root.left.left.right = Node(6)
root.left.right.left = Node(4)
root.left.left.right.left = Node(6)
root.left.left.right.right = Node(10)
root.left.right.left.right = Node(8)

if isBalanced(root) > 0:
    print('Tree is balanced')
else:
    print('Tree is not balanced')
