"""
Queue using LL

push --> addLast()
pop --> removefirst()
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
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

    def removeFirst(self):
        if self.empty():
            res = -1
        elif self.head.next is None:
            res = self.head.data
            self.head = None
        else:
            res = self.head.data
            self.head = self.head.next
        return res

    # Method to add an item to the queue
    def push(self, item):
        self.addLast(item)

    # Method to remove an item from queue
    def pop(self):
        return self.removeFirst()
