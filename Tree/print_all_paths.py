import queue
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.data)

def levelOrder(root):
    #Write your code here
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        # for n in list(q.queue):
        #     print("queue: ", n, end=" ")
        # print("\n")
        node = q.get()
        print(node.data,end=" ")
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)

def printpaths(root,s):
    # add nodes in stack
    # do inorder traversal
    # when we reach any leaf node print full stack
    # after the end remove the node from stack
    if root is None:
        return
    s.append(root.data)
    printpaths(root.left,s)
    if (root.left and root.right) is None:
        print(s)
    printpaths(root.right,s)
    s.pop()
#main function
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
    s = []
    #levelOrder(root)
    printpaths(root,s)
