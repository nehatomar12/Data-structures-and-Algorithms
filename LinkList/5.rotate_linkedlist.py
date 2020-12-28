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

    def rotate_linklist(self, k):
        trav2 = trav1 = self.head
        cnt = 1
        while trav2.next:
            trav2 = trav2.next
            cnt += 1
            if cnt == k:
                trav1 = trav2
        print(trav1.data, trav2.data)
        trav2.next = self.head
        self.head = trav1.next
        trav1.next = None

list_obj = LL()
l1 = [1,2,3,4,5,6,7,8]

for i in l1:
    list_obj.addLast(i)

list_obj.listprint()
list_obj.rotate_linklist(k=9)
list_obj.listprint()
