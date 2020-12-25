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


def merge_bst(root1, root2):
    """
    base cases:
        -if root1 empty; print(inorder: root2)
        -if root2 empty; print(inorder: root1)

    follow iterative in_order
    while curr and len(s) >0:
        if curr:
            s.append(curr)
            curr= curr.left
        if len(s) > 0: ----> changed
            node = s.pop()
            print(node.data)
            curr =curr.right

    s1 s2 [] []
    curr1 curr2
    """
    if not root1:
        inorder(root2)
    if not root2:
        inorder(root1)
    s1, s2 = [], []
    curr1, curr2 = root1, root2

    while curr1 or curr2 or s1 or s2:
        if curr1 or curr2:
            if curr1:
                s1.append(curr1)
                curr1 = curr1.left
            if curr2:
                s2.append(curr2)
                curr2 = curr2.left
        else:
            if not s1:
                # inorder for curr2
                if s2:
                    curr2 = s2.pop()
                    curr2.left = None
                    inorder(curr2)
                    return
            if not s2:
                # inorder for curr1
                if s1:
                    curr1 = s1.pop()
                    curr1.left = None
                    inorder(curr1)
                    return
            curr1 = s1.pop()
            curr2 = s2.pop()
            if curr1.data < curr2.data:
                print(curr1.data, end = " ")
                curr1 = curr1.right
                s2.append(curr2)
                curr2 =None
            else:
                print(curr2.data, end = " ")
                curr2 = curr2.right
                s1.append(curr1)
                curr1 =None




if __name__ == "__main__":
    # Let us create the following tree as first tree
    #      3
    #     / \
    #    1   5

    root1 = Node(3)
    root1.left = Node(1)
    root1.right = Node(5)

    # Let us create the following tree as second tree
    #      4
    #     / \
    #    2    6
    #

    root2 = Node(4)
    root2.left = Node(2)
    root2.right = Node(6)

    merge_bst(root1, root2)
