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

    def reverse_linklist(self):
        current = self.head
        prev = None

        while current:
            nextp = current.next
            current.next = prev
            prev = current
            current = nextp

        self.head = prev

    def reverse_linklist_group(self, head, k):
        current = head
        prev = None
        cnt = 0
        while current and cnt < k:
            nextp = current.next
            current.next = prev
            prev = current
            current = nextp
            cnt += 1
        if nextp:
            head.next = self.reverse_linklist_group(nextp, k)
        return prev

list_obj = LL()
l1 = [1, 2, 3, 4, 5, 6]

for i in l1:
    list_obj.addLast(i)

list_obj.listprint()
list_obj.head = list_obj.reverse_linklist_group(list_obj.head, 2)
list_obj.listprint()
