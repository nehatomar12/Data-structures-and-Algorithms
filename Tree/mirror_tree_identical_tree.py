class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

##
## mirror Tree
##
def areMirrors(root1,root2):
    # inorder of root1 and
    # reverse inorder of root2
    st1 = []
    st2 = []
    while True:
        while root1 and root2:
            
            if root1.data != root2.data:
                return False
            st1.append(root1)
            st2.append(root2)
            root1 = root1.left
            root2 = root2.right
            
        # check if any of root1/root2 is None
        if not (root1 is None or root2 is None):
            return False

        if len(st1) == 0 and len(st2) == 0:
            break
        else:
            root1,root2=st1.pop(),st2.pop()
            root1 = root1.right
            root2 = root2.left
            
    return True


def areidentical(root1, root2):

    #base condition
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    q1, q2 = [], []
    q1.append(root1)
    q2.append(root2)

    while (len(q1) >0 and len(q2) >0):

        n1 = q1.pop()
        n2 = q2.pop()

        if n1.data != n2.data:
            return False

        if n1.left and n2.left:
            q1.append(n1.left)
            q2.append(n2.left)
        elif n1.left or n2.left:
            return False

        if n1.right and n2.right:
            q1.append(n1.right)
            q2.append(n2.right)
        elif n1.right or n2.right:
            return False

    return True

if __name__ == '__main__':

    # 1st binary tree formation
    root1 = newNode(1)         #          1
    root1.left = newNode(3)         #     / \
    root1.right = newNode(2)  #        3    2
    root1.right.left = newNode(5)#       / \
    root1.right.right = newNode(4) #  5      4

    # root2 = newNode(1)         #          1
    # root2.left = newNode(3)         #     / \
    # root2.right = newNode(2)  #        3    2
    # root2.right.left = newNode(5)#       / \
    # root2.right.right = newNode(4) #  5      4

    # 2nd binary tree formation
    root2 = newNode(1)        #          1
    root2.left = newNode(2)         #     / \
    root2.right = newNode(3) #        2     3
    root2.left.left = newNode(4)#  / \
    root2.left.right = newNode(5)# 4  5

    print((areMirrors(root1, root2)))
    #print(areidentical(root1, root2))