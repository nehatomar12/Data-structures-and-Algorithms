"""
Take two pointers for the heads of both the linked lists.
If one of them reaches the end earlier then use it by moving it to the beginning of the other list.
Once both of them go through reassigning they will be equidistance from the collision point.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def empty(self):
        if self.head is None:
            return True
        return False

    def size(self):
        cnt = 0
        trav = self.head
        while trav is not None:
            cnt += 1
            trav = trav.next
        return cnt

    def addLast(self, data):
        newNode = Node(data)
        if self.empty():
            self.head = newNode
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = newNode

    def listprint(self):
        trav = self.head
        while trav is not None:
            print(trav.data, end=" ")
            trav = trav.next
        print()


def intersection_point_1(l1, l2):
    size1 = l1.size()
    size2 = l2.size()
    print(size1, size2)
    diff = abs(size2 - size1)
    if size1 > size2:
        cnt = 0
        trav1 = l1.head
        while cnt < diff:
            trav1 = trav1.next
            cnt += 1
        trav2 = l2.head
    else:
        cnt = 0
        trav2 = l2.head
        while cnt < diff:
            trav2 = trav2.next
            cnt += 1
        trav1 = l1.head
    while trav1 and trav2:
        if trav1.data == trav2.data:
            print("Intersection point: ", trav1.data)
            return trav1.data
        trav1 = trav1.next
        trav2 = trav2.next

    return None


def intersection_point_2(headA, headB):

    if headA == None or headB == None:
            return None

    A_pointer = headA
    B_pointer = headB

    while A_pointer and B_pointer and A_pointer.data != B_pointer.data:
        A_pointer = headB if A_pointer == None else A_pointer.next
        B_pointer = headA if B_pointer == None else B_pointer.next


    if A_pointer:
        return A_pointer.data
    elif B_pointer:
        return B_pointer.data
    else:
        return None




l2 = [1,2,3,7,8]
l1 = [5,4,6,7,8,9]


l1 = [39, 9, 31, 22, 82, 6,18, 15, 91]
l2=[80, 72,18, 15, 91]
list_obj1 = LL()
for i in l1:
    list_obj1.addLast(i)
list_obj1.listprint()

list_obj2 = LL()
for i in l2:
    list_obj2.addLast(i)
list_obj2.listprint()

print(intersection_point_2(list_obj1.head, list_obj2.head))
