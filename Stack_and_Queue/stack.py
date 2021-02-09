class Stack:
    def __init__(self):
        self.top = -1
        self.stack_s = list()
        self.size = 5

    def empty(self):
        return (self.top == -1)

    def full(self):
        return (self.top == self.size - 1)

    def push(self, ele):
        if self.full():
            raise Exception("stack_s is full")
        self.stack_s.append(ele)
        self.top += 1
        return True

    def pop(self):
        if self.empty():
            raise Exception("stack_s is empty")
        self.stack_s.pop(self.top)
        self.top -= 1
        return True

    def peek(self):
        if self.empty():
            raise "stack_s is empty"
        return self.stack_s[self.top]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_LL:
    def __init__(self):
        self.head = None
        
    def empty(self):
        return (self.head == None)

    # Add first position
    def push(self, ele):
        if self.empty():
            self.head = Node(ele)
        else:
            newNode = Node(ele)
            newNode.next = self.head
            self.head = newNode
        return True

    # remove last
    def pop(self):
        if self.empty():
            print("Nothing to remove")
        elif self.head.__next__ is None:
            self.head = Node
        else:
            #trav = self.head
            self.head = self.head.__next__
        return True

    def peek(self):
        if self.empty():
            raise "stack_s is empty"
        return self.head.data

myStack = Stack_LL()
print(myStack.push(5)) #prints True
print(myStack.peek())
print((myStack.push(6))) #prints True
print(myStack.peek())
print((myStack.push(9))) #prints True
print(myStack.peek())
myStack.pop()
print(myStack.peek())


# print myStack.pop() #prints True
# print myStack.peek()
# print(myStack.pop()) #prints True
# print myStack.peek()
# print(myStack.pop()) #prints True
# print myStack.peek()


# print(myStack.push(5)) #prints False since 5 is there
# print(myStack.push(3)) #prints True
# #print(myStack.size())  #prints 4 
# print(myStack.pop())   #prints 3
# print(myStack.pop())   #prints 9
# print(myStack.pop())   #prints 6
# print(myStack.pop())   #prints 5
# #print(myStack.size())  #prints 0
# print(myStack.pop())