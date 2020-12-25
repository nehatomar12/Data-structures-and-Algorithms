class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        self.nextRight = None


def in_order(root):
    if not root:
        return
    in_order(root.left)
    print(root.data,end=" ")
    in_order(root.right)

def printLevelByLevel(root):
    # print level by level
    if root:
        node = root
        while node:
            print('{}'.format(node.data), end=' ')
            node = node.nextRight
        print()
        if root.left:
            printLevelByLevel(root.left)
        else:
            printLevelByLevel(root.right)

def connect(root):
    q = [root]
    q.append(None)
    while q:
        node = q.pop(0)
        if node:
            node.nextRight = q[0]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        elif q:
            q.append(None)

root = Node(10)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(1)
root.right.right = Node(2)
connect(root)
in_order(root)
print()
printLevelByLevel(root)