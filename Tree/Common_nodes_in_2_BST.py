"""
Method1: search every node of first tree in second tree. Time complexity of this solution is O(m * h)
         where m is number of nodes in first tree and h is height of second tree.

Method2:
    inorder() arr1
    inorder() arr2
    find intersection of 2 sorted array (pointers)

Method3:
    https://www.geeksforgeeks.org/print-common-nodes-in-two-binary-search-trees/
"""

class Node:
    def __init__(self, data):
        self.key = data
        self.left = self.right= None

class Btree:
    def __init__(self):
        self.root = None

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

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.left)
            print (str(node.key) , end=' ')
            self._printTree(node.right)

def common_node(root1, root2):
    s1, s2 = [], []
    while True:
        if root1:
            # move root1 to left till None
            s1.append(root1)
            root1 = root1.left
        elif root2:
            # move root1 to left till None
            s2.append(root2)
            root2 = root2.left

        elif len(s1) != 0 and len(s2) != 0:
            root1 = s1[-1]
            root2 = s2[-1]
            if root1.key < root2.key:
                s1.pop(-1)
                root1 = root1.right
                root2 = None
            elif root1.key > root2.key:
                s2.pop(-1)
                root2 = root2.right
                root1 = None
            else:
                print(root1.key, " ")
                s1.pop(-1)
                s2.pop(-1)
                root1 = root1.right
                root2 = root2.right
        else:
            break

if __name__ == "__main__":
    tree1 = Btree()
    tree1.addNode(5)
    tree1.addNode(1)
    tree1.addNode(10)
    tree1.addNode(0)
    tree1.addNode(4)
    tree1.addNode(7)
    tree1.addNode(9)

    #tree1._printTree(tree1.root)
    #print()
    tree2 = Btree()
    tree2.addNode(10)
    tree2.addNode(7)
    tree2.addNode(10)
    tree2.addNode(4)
    tree2.addNode(9)

    # tree2._printTree(tree2.root)
    # print()

    common_node(tree1.root, tree2.root)
    # print(tree1.root.key)
    # print(tree2.root.key)
