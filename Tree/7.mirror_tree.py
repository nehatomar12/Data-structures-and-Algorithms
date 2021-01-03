class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

##
## mirror Tree
##
def areMirrors_iterative(root1,root2):
    # inorder of root1 and
    # reverse inorder of root2
    st1 = []
    st2 = []
    while True:
        while root1 and root2:
            if root1.data != root2.data:
                return False
            st1.append(root1)
            st2.append(root2)
            root1 = root1.left
            root2 = root2.right
        # check if any of root1/root2 is None
        if not (root1 is None or root2 is None):
            return False
        if len(st1) == 0 and len(st2) == 0:
            break
        else:
            root1,root2=st1.pop(),st2.pop()
            root1 = root1.right
            root2 = root2.left
    return True


def areMirror_recursive(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data == root2.data:
        return areMirror_recursive(root1.left, root2.right) and areMirror_recursive(root1.right, root2.left)
    return False

if __name__ == '__main__':

    # 1st binary tree formation
    root1 = Node(1)         #          1
    root1.left = Node(3)         #     / \
    root1.right = Node(2)  #        3    2
    root1.right.left = Node(5)#       / \
    root1.right.right = Node(4) #  5      4

    # 2nd binary tree formation
    root2 = Node(1)        #          1
    root2.left = Node(2)         #     / \
    root2.right = Node(3) #        2     3
    root2.left.left = Node(4)#  / \
    root2.left.right = Node(5)# 4  5

    print((areMirrors_iterative(root1, root2)))
    print((areMirror_recursive(root1, root2)))