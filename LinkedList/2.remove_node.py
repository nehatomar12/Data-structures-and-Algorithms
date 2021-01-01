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

    def addLast(self, data):
        newNode = Node(data)
        if self.empty():
            self.head = newNode
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = newNode

    def removeFirst(self):
        if self.empty():
            print("Nothing to remove")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

    def removeLast(self):
        if self.empty():
            print("Nothing to remove")
        elif self.head.next is None:
            self.head = None
        else:
            trav = self.head
            while trav.next.next:
                trav = trav.next
            trav.next = None

    def removeSpecificPos(self, pos):
        if pos <= 0:
            print("invalid pos")
        elif pos == 1:
            self.removeFirst()
        elif pos >= self.size():
            self.removeLast()
        else:
            trav = self.head
            for i in range(1, pos - 1):
                trav = trav.next
            trav.next = trav.next.next

    def removeBefore(self, dataf):
        res = self.find(dataf)
        if res is None:
            print("Data/Node not found")
            raise
        trav = self.head
        prev = None
        while trav.next.data != dataf:
            prev = trav
            trav = trav.next
        prev.next = trav.next

    def deleteNode(self, curr_node):
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next


list_obj = LL()
l1 = [1, 2, 3, 5, 4, 5]

for i in l1:
    list_obj.addLast(i)

list_obj.listprint(list_obj.head)
list_obj.removeBefore(4)
list_obj.listprint(list_obj.head)


# Delete without head pointer
list_obj.listprint(list_obj.head)
list_obj.deleteNode(list_obj.head.next.next)
list_obj.listprint(list_obj.head)