import queue
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.data)

'''
hd= horizontal distance
BOTTOM view: 7,5,8,6
This implementation uses level order traversal.
The vertical column right to root node are positive and to left of root node is -ve.
Dictionary(res) is used to keep track of lowest node in a vertical column.
        1
    2       3
        5       6
    7       8


'''
#
#Level order Traversal
#
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
#
# Bottom-view
#
def print_bottom_view_BT(root):
    #base case
    if root is None:
        return
    que = queue.Queue()
    map_hd = {}
    root.level = 0
    que.put(root)
    while not que.empty():
        node = que.get()
        # as the hash is created for hd
        # and we are updating with latest value
        map_hd[node.level] = node.data
        if node.left:
            node.left.level = node.level -1
            que.put(node.left)
        if node.right:
            node.right.level = node.level +1
            que.put(node.right)
    for v in sorted(map_hd):
        print(map_hd[v],end=" ")
#
# Top-view
#
def print_top_view_BT(root):
    #base case
    if root is None:
        return
    que = queue.Queue()
    map_hd = {}
    root.level = 0
    que.put(root)
    while not que.empty():
        node = que.get()
        # as the hash is created for hd
        # and we are updating with first value
        if node.level not in map_hd:
            map_hd[node.level] = node.data
        if node.left:
            node.left.level = node.level -1
            que.put(node.left)
        if node.right:
            node.right.level = node.level +1
            que.put(node.right)
    for v in sorted(map_hd):
        print(map_hd[v],end=" ")

#
# left-view
#
def print_left_view_BT(root):
    if root is None:
        return
    que = []
    que.append(root)
    while len(que) > 0:
        check = True
        nodeCount = len(que)
        while(nodeCount > 0):
            node = que[0]
            que.pop(0)
            if check:
                print(node.data,end=" ")
                check=False
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            nodeCount -= 1

def print_right_view_BT(root):
    if root is None:
        return
    que = []
    que.append(root)
    while len(que) > 0:
        nodeCount = len(que)
        while(nodeCount > 0):
            node = que[0]
            que.pop(0)
            if nodeCount == 1:
                print(node.data,end=" ")

            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            nodeCount -= 1

def print_vertical_view_BT(root):
    if root is None:
        return
    que = queue.Queue()
    map_hd = {}
    root.level = 0
    que.put(root)
    while not que.empty():
        node = que.get()
        if node.level in map_hd:
            map_hd[node.level].append(node.data)
        else:
            map_hd[node.level] = [node.data]
        if node.left:
            node.left.level = node.level -1
            que.put(node.left)
        if node.right:
            node.right.level = node.level +1
            que.put(node.right)

    #print(map_hd)
    # for _, value in enumerate(sorted(map_hd)):
    #     for i in map_hd[value]:
    #         print(i,end=" ")
    #     print()
    for _, i in sorted(map_hd.items(), key= lambda x: x[0]):
        print(i,end=" ")
    print()

def reverse_level_order_BT(root):
    que = []
    st = []
    que.append(root)
    while len(que) > 0:
        node = que[0]
        que.pop(0)
        st.append(node)
        if node.right:
            que.append(node.right)
        if node.left:
            que.append(node.left)
    while len(st) > 0:
        r = st.pop()
        print(r,end=" ")


#main function
if __name__ == '__main__':


    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    #print_bottom_view_BT(root)
    #levelOrder(root)
    #print_top_view_BT(root)
    #print_left_view_BT(root)
    #print_right_view_BT(root)
    #print_vertical_view_BT(root)
    reverse_level_order_BT(root)
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    #levelOrder(root)
    #reverse_level_order_BT(root)
    print_vertical_view_BT(root)
    """