# given a BT and any value
# find the value in BT

"""
            10
    12              20
11      7       2       3


key: 2

in-order: 11 12 7 10 2 20 3

"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def pre_order(root, key):
    # Base cond
    if not root:
        return False
    if root.data == key:
        return True
    if pre_order(root.left, key):
        return True
    return pre_order(root.right, key)

def in_order(root, key):
    # L P R
    # Base cond
    if not root:
        return False
    if in_order(root.left, key):
        return True
    if root.data == key:
        return True
    return in_order(root.right, key)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(12)
    root.left.left = Node(11)
    root.right = Node(20)
    root.right.left = Node(2)
    root.right.right = Node(3)

    print((pre_order(root, 200)))
    print((in_order(root, 200)))
    # print(pre_order(root, 21))
    # print(pre_order(root, 3))
