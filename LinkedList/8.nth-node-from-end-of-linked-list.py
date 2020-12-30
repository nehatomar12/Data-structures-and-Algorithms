"""
Find the Nth node from the end of the linked list.

N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output: 8

Method 1: Get length
        print (length -n + 1) node

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

    def listprint(self, head):
        trav = head
        while trav is not None:
            print(trav.data, end=" ")
            trav = trav.next
        print()

    def addLast(self, data):
        newNode = Node(data)
        if self.empty():
            self.head = newNode
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = newNode

    def get_nth_node(self, n):
        left = self.head
        right = self.head

        cnt = 0
        while right and cnt < n:
            right = right.next
            cnt += 1
        if not right:
            # cases:
            # 1. either nth value is greater then length
            # 2. nth value is equal to length
            if cnt == n:
                print(left.data)
                return
            return None
        else:
            while right:
                left = left.next
                right = right.next

            print(left.data)


list_obj = LL()
l1 = [1, 2, 3, 4, 5, 6]
for i in l1:
    list_obj.addLast(i)

list_obj.get_nth_node(6)