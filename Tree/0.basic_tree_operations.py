from queue import Queue
class Node:
    def __init__(self, data):
        self.key = data
        self.left = self.right= None

class Btree:
    def __init__(self):
        self.root = None

    def getRoot(self,data):
        return self.root

    def addNode(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            trav = self.root
            while True:
                if data < trav.key:
                    # move in left
                    if trav.left is None:
                        trav.left = newNode
                        break
                    trav = trav.left
                else:
                    # move in right
                    if trav.right is None:
                        trav.right = newNode
                        break
                    trav = trav.right

    def height_of_tree(self):
        # longest path from root to any leaf node
        # Base Case
        if self.root is None:
            return 0
        q = []
        q.append(self.root)
        height = 0
        while len(q) > 0:
            nodeCount = len(q)
            height += 1
            # pop all the nodes at this level
            # and add child of nodes
            while(nodeCount > 0):
                node = q[0]
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                nodeCount -= 1
        return height


    def search_node(self, data):
        if self.root is None:
            return False
        q = Queue.Queue()
        q.put(self.root)
        while q.empty() == False:
            node = q.queue[0]
            if node.key == data:
                return True
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
            q.get()
        return False


    def findnode(self, data):
        parentNode = None
        trav = self.root
        while trav is not None:
            if trav.key == data:
                return parentNode, trav
            parentNode = trav
            if data < trav.key:
                trav = trav.left
            else:
                trav = trav.right
        #parentNode = None
        return None , None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print((str(node.key) + ' '))
            self._printTree(node.right)

    def morris_inorder(self):
        current = self.root
        while current is not None:
            if current.left is None:
                print((current.key,))
                current = current.right
            else:
                pre = current.left
                # Find the inorder predecessor of current
                while pre.right is not None and pre.right != current:
                    pre=pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    print((current.key))
                    # left subtree is processed
                    current = current.right

    def morris_preorder(self, r):
        current = r
        while current:
            if current.left is None:
                print((current.key,))
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right != current:
                    pre = pre.right

                if pre.right is current:
                    pre.right = None
                    current = current.right
                else:
                    print((current.key,))
                    pre.right = current
                    current = current.left

    def isLeaf(self, node1):
        if node1 is None:
            return 0
        if node1.left and node1.right is None:
            return 1
        return 0




tree = Btree()
#tree.addNode(26)
tree.root = 5
tree.root.left = 5

#tree.morris_inorder()

#print "Sum: ", tree.sum_of_tree(tree.root)
#tree.printTree()

print(("Height: ", tree.height_of_tree()))
# par, trav = tree.findnode(4)
# print "Serach: ", par.key, "  ", trav.key