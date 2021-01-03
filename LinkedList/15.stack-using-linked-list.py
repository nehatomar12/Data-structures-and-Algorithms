"""
Stack using LL

push --> addLast()
pop --> removeLast()
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

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

    def removeLast(self):
        if self.empty():
            res = -1
        elif self.head.next is None:
            res = self.head.data
            self.head = None
        else:
            trav = self.head
            while trav.next.next:
                trav = trav.next
            res = trav.next.data
            trav.next = None
        return res

    def push(self, data):
        self.addLast(data)

    def pop(self):
        return self.removeLast()
