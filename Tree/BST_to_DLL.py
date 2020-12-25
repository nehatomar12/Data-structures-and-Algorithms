
"""
The left and right pointers in nodes are to be used as previous and
next pointers respectively in converted DLL. The order of nodes in DLL
must be same as Inorder of the given Binary Tree.
The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

"""
class Node(object):

    """Binary tree Node class has
    data, left and right child"""

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        # Represent the root of binary tree
        self.root = None
        # Represent the self.head and self.tail of the doubly linked list
        self.head = None
        self.tail = None

    def BSTtoDLL(self, node):
        # break condition for recursion
        if node is None:
            return

        self.BSTtoDLL(node.left)

        if self.head is None:
            self.head = node
        else:
            # for both nodes get 2 pointers ready for DLL
            self.tail.right = node
            node.left = self.tail
        self.tail = node

        self.BSTtoDLL(node.right)
        # print("R:",root.data)
        # print(self.head.data)


    def print_list(self):
        """Function to print the given
        doubly linked list"""
        if self.head is None:
            return
        while self.head:
            print(self.head.data, end=" ")
            self.head = self.head.right


# Driver Code
if __name__ == '__main__':
    bt = BST()
    bt.root = Node(10)
    bt.root.left = Node(12)
    bt.root.right = Node(15)
    bt.root.left.left = Node(25)
    bt.root.left.right = Node(30)
    bt.root.right.left = Node(36)


    bt.BSTtoDLL(bt.root)
    bt.print_list()
