class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def addNode(root, data):
    newNode = Node(data)
    if root is None:
        root = newNode
    else:
        trav = root
        while True:
            if data < trav.data:
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


"""
functions
    - get distance from root to node
    - get distance between nodes (LCA)
"""

def get_distance_from_root(root, key):
    if root.data == key:
        return 0
    if root.data > key:
        return 1 + get_distance_from_root(root.left, key)
    return 1 + get_distance_from_root(root.right, key)


def get_distance(root, a, b):
    if not root:
        return 0
    if root.data > a and root.data > b:
        return get_distance(root.left, a, b)
    elif root.data < a and root.data < b:
        return get_distance(root.right, a, b)
    elif root.data >= a and root.data <= b:
        return get_distance_from_root(root, a) + get_distance_from_root(root, b)


if __name__ == '__main__':

    root = Node(20)
    addNode(root, 10)
    addNode(root, 5)
    addNode(root, 15)
    addNode(root, 30)
    addNode(root, 25)
    addNode(root, 35)
    a, b = 5, 15
    if a > b:
        a, b = b, a
    print((get_distance(root, a, b)))
    #make sure a  < b
