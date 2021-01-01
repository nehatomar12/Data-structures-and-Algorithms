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

    def swappair(self):
        trav = self.head
        while trav and trav.next:
            trav.data, trav.next.data = trav.next.data, trav.data
            trav = trav.next.next

list_obj = LL()
l1 = [1,2,3,4,5,6,7]

for i in l1:
    list_obj.addLast(i)

list_obj.listprint()
list_obj.swappair()
list_obj.listprint()
