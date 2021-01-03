
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
          / \   /
        4    5 6
       /
      7
"""
# to store the height of tree during traversal

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.left = Node(6)
#root.left.left.left.right = Node(12)


if isBalanced(root) > 0:
    print('Tree is balanced')
else:
    print('Tree is not balanced')
