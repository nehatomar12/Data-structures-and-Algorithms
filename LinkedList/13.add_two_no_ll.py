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

    def listprint(self):
        trav = self.head
        while trav is not None:
            print(trav.data,end=" ")
            trav = trav.next
        print()

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

    def size(self):
        cnt = 0
        trav = self.head
        while trav is not None:
            cnt += 1
            trav = trav.next
        return cnt

    def reverseLL(self):
        prev = None
        current = self.head
        while current is not None:
            nextp = current.next
            current.next = prev
            prev = current
            current = nextp
        self.head = prev
        return prev


def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print(None)


"""
Method 1:
    1. Reverse the LL
    2. Add 0's to make the size equal
    3. Do the addition
"""
def add_numbers(l1, l2):
    l1.head =  l1.reverseLL()
    l2.head =  l2.reverseLL()

    l1_size = l1.size()
    l2_size = l2.size()

    diff = abs(l1_size-l2_size)

    if l1_size > l2_size:
        for i in range(diff):
            l2.addLast(0)
    else:
        for i in range(diff):
            l1.addLast(0)

    new_head = None
    trav1 = l1.head
    trav2 = l2.head
    carry = 0
    while trav1:
        total = trav1.data + trav2.data + carry
        carry = total // 10
        rem = total % 10
        newNode = Node(rem)
        if not new_head:
            new_head = newNode
        else:
            newNode.next = new_head
            new_head = newNode
        trav1 = trav1.next
        trav2 = trav2.next

    if carry != 0:
        newNode = Node(carry)
        newNode.next = new_head
        new_head = newNode

    l1.listprint()
    l2.listprint()
    printList(new_head)


# Better solution
"""
maintain 2 stack
l1 = [4,5]
l2 = [3,4,5]

s1 = [5,4] s2 = [5,4,3]
perform basic addtion with carry
"""
def addTwoLists(first, second):

    new_head = None

    carry = 0
    stack1 = []
    stack2 = []
    while first:
        stack1.insert(0, first.data)
        first = first.next

    while second:
        stack2.insert(0, second.data)
        second = second.next

    while(stack1 or stack2):
        fdata = 0 if not stack1 else stack1.pop(0)
        sdata = 0 if not stack2 else stack2.pop(0)

        tot = carry + fdata + sdata

        carry = tot // 10
        rem = tot % 10
        temp = Node(rem)

        # Add at first position
        if new_head:
            temp.next = new_head
        new_head = temp


    if carry > 0:
        temp = Node(carry)
        temp.next = new_head
        new_head = temp

    printList(new_head)

list_obj = LL()
l1 = [4,5]
list_obj2 = LL()
l2 = [3,4,5]

for i in l1:
    list_obj.addLast(i)
list_obj.listprint()
for i in l2:
    list_obj2.addLast(i)
list_obj.listprint()

#add_numbers(list_obj, list_obj2)
printList(list_obj.head)
printList(list_obj2.head)
addTwoLists(list_obj.head, list_obj2.head)