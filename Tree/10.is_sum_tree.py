class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right= None

def sum_of_tree( trav):
    if not trav:
        return 0
    return (trav.data + sum_of_tree(trav.left) + sum_of_tree(trav.right))


def isSumTree( node_t):
    #ls , rs = 0,0
    #check for empty tree and leaf node
    if node_t is None or (node_t.left is None and node_t.right is None):
        return 1

    # cal sum of left and right
    ls = sum_of_tree(node_t.left)
    rs = sum_of_tree(node_t.right)

    # recursively check for sumtree
    if node_t.data == (ls+rs) and isSumTree(node_t.left) and isSumTree(node_t.right):
        return 1
    return 0

if __name__ == "__main__":
    root = Node(26)
    root.left= Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)

    if(isSumTree(root)):
        print("The given tree is a SumTree ")
    else:
        print("The given tree is not a SumTree ")