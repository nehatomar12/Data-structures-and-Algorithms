class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def areIdentical_iterative(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    return (root1.data==root2.data and areIdentical_iterative(root1.left, root2.left) and areIdentical_iterative(root1.right,root2.right))


def areIdentical_recursive(root1, root2):

    #base condition
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    q1, q2 = [], []
    q1.append(root1)
    q2.append(root2)

    while (len(q1) >0 and len(q2) >0):

        n1 = q1.pop()
        n2 = q2.pop()

        if n1.data != n2.data:
            return False

        if n1.left and n2.left:
            q1.append(n1.left)
            q2.append(n2.left)
        elif n1.left or n2.left:
            return False

        if n1.right and n2.right:
            q1.append(n1.right)
            q2.append(n2.right)
        elif n1.right or n2.right:
            return False

    return True

if __name__ == '__main__':

    # 1st binary tree formation
    root1 = Node(1)         #          1
    root1.left = Node(3)         #     / \
    root1.right = Node(2)  #        3    2
    root1.right.left = Node(5)#       / \
    root1.right.right = Node(4) #  5      4

    root2 = Node(1)         #          1
    root2.left = Node(3)         #     / \
    root2.right = Node(2)  #        3    2
    root2.right.left = Node(5)#       / \
    root2.right.right = Node(4) #  5      4



    print((areIdentical_iterative(root1, root2)))
    print(areIdentical_recursive(root1, root2))