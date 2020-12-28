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

    def size(self):
        cnt = 0
        trav = self.head
        while trav is not None:
            cnt += 1
            trav = trav.next
        return cnt

    def find(self, data):
        trav = self.head
        while trav is not None:
            if trav.data == data:
                return trav
            trav = trav.next
        return None

    def addFirst(self, data):
        newNode = Node(data)
        if self.empty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def addLast(self, data):
        newNode = Node(data)
        if self.empty():
            self.head = newNode
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = newNode

    def specificPos(self, data, pos):
        if pos <= 0:
            print("invalid pos")
        elif pos == 1:
            self.addFirst(data)
        elif pos >= self.size():
            self.addLast(data)
        else:
            newNode = Node(data)
            trav = self.head
            for i in range(pos - 1):
                trav = trav.next
            newNode.next = trav.next
            trav.next = newNode

    def addBefore(self, dataf, adddata):
        res = self.find(dataf)
        if res is None:
            print("Data/Node not found")
            raise
        trav = self.head
        while trav.data != dataf:
            trav = trav.next
        newNode = Node(dataf)
        newNode.next = trav.next
        trav.next = newNode
        trav.data = adddata


list_obj = LL()
l1 = [1, 2, 3, 5, 6]

for i in l1:
    list_obj.addLast(i)
list_obj.listprint(list_obj.head)
list_obj.addBefore(5, 4)
list_obj.listprint(list_obj.head)
