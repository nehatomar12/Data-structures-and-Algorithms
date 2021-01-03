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

    def listprint(self, head):
        trav = head
        while trav is not None:
            print(trav.data, end=" ")
            trav = trav.next
        print()

    def detect_and_removeLoop(self):
        slow_p = fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("loop found")
                return slow_p
        print("loop not found")
        return None

    def remove_loop(self, slow_p):
        trav1 = self.head
        trav2 = slow_p

        while trav1 and trav2:
            if trav1.next == trav2.next:
                trav2.next = None
            trav1 = trav1.next
            trav2 = trav2.next


list_obj = LL()
l1 = [1, 2, 3, 4, 5]

for i in l1:
    list_obj.addLast(i)

# create a loop
list_obj.head.next.next.next.next.next = list_obj.head
loop_node = list_obj.detect_and_removeLoop()
list_obj.remove_loop(loop_node)
loop_node = list_obj.detect_and_removeLoop()
