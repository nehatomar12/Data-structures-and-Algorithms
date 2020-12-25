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

def getleafnode(root):
    #Write your code here
    q = []
    q.append(root)
    leafnodecount = 0
    while len(q):
        
        node = q.pop(0)
        if node.left is None and node.right is None:
            leafnodecount += 1
        
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    print(leafnodecount)

#main function
if __name__ == '__main__':
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    #levelOrder(root)
    getleafnode(root)

    