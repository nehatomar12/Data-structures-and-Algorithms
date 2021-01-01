"""
Method:
    1. Divide LL in 2 parts
    2. Reverse the 2nd half
    3. check first and second half is equal
        if LL is odd skip the middle element


    splits the tasks
    1. function to get middle of LL
        - LL is odd or even
        - pointers to both parts

    2. compare the LL
        - recursively compare the LL elements

    3. Reverse the LL
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

    def addFirst(self, data):
        newNode = Node(data)
        if self.empty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

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

def listprint(head):
    trav = head
    while trav is not None:
        print(trav.data,end=" ")
        trav = trav.next
    print()

def reverseLL(head):
    prev = None
    current = head
    while current is not None:
        nextp = current.next
        current.next = prev
        prev = current
        current = nextp
    return prev


def findMiddle(head, is_odd):
    prev = None
    slow = fast = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    if fast:
        is_odd = True

    if prev:
        # divide in 2 parts
        prev.next = None
    return is_odd, slow

def compareLL(a, b):
    if not a and not b:
        return True
    return a and b and a.data == b.data and compareLL(a.next, b.next)


def check_palindrome(head):

    if not head or not head.next:
        return True

    is_odd = False

    is_odd, slow = findMiddle(head, is_odd)

    if is_odd:
        slow = slow.next

    slow = reverseLL(slow)

    return compareLL(head, slow)



list_obj = LL()
l1 = [1,2,3,2,1]
l1 = [1,2]


for i in l1:
    list_obj.addLast(i)
listprint(list_obj.head)

if check_palindrome(list_obj.head):
    print("LL is Palindrome")
else:
    print("LL is not Palindrome")