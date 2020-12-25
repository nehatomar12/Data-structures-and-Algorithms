

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = 0

def isleafSameLevel(node, nodeLevel ):
    global level
    if not node:
        return True

    if node.left is None and node.right is None:
        if level == -1:
            level = nodeLevel
        else:
            return level == nodeLevel

    return isleafSameLevel(node.left, (nodeLevel +1)) and isleafSameLevel(node.right, (nodeLevel +1))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
# root.right.left.right = Node(55)
root.right.right = Node(6)

level = -1
root.level = 0
print((isleafSameLevel(root, root.level)))


# Method1 use print all paths function, check len of paths is same or not
# Method2 try to replace path [] with level value for every node