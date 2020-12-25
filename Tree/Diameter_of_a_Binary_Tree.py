import queue
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printpaths(root,s):
    # do inorder traversal
    # add nodes in stack
    # when we reach any leaf node print full stack
    # after the end remove the node from stack
    if root is None:
        return

    s.append(root.data)
    printpaths(root.left,s)
    if (root.left and root.right) is None:
        print((s, sum(s)))
    printpaths(root.right,s)
    s.pop()
    return

def in_order(root):
    if not root:
        return
    in_order(root.left)
    print((root.data))
    in_order(root.right)

def diameter_of_tree(root):
    global ans
    if (root == None):
        return 0

    left_height = diameter_of_tree(root.left)
    right_height = diameter_of_tree(root.right)

    # update the answer, because diameter
    # of a tree is nothing but maximum
    # value of (left_height + right_height + 1)
    # for each node
    ans = max(ans, 1 + left_height +
                             right_height)

    return 1 + max(left_height,
                   right_height)
#main function
if __name__ == '__main__':

    root = Node(9)
    root.left = Node(8)
    #root.right = Node(6)
    root.left.left = Node(5)
    root.left.right = Node(10)
    #root.left.left.left = Node(2)
    root.left.left.right = Node(5)
    root.left.right.left = Node(6)
    #root.right.right = Node(9)
    root.left.left.right.right= Node(6)
    # root.right.right.right.left = Node(4)
    # root.right.right.right.right = Node(-1)
    # root.right.right.right.right.left = Node(10)
    s = []
    ans = -999999999
    diameter_of_tree(root)
    print(ans)

    #in_order(root)
    #printpaths(root, s)
