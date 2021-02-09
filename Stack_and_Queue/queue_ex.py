class Queue_ex:
    def __init__(self):
        self.rear = -1
        self.front = -1
        self.size = 5
        self.que = [None]*self.size

    def empty(self):
        if (self.rear == -1 or self.front > self.rear):
            print("Queue_ex is empty")
            return True
        return False

    def full(self):
        if (self.rear == (self.size -1)):
            print("Queue_ex is full")
            return True
        return False

    def peek(self):
        if self.empty():
            print("Empty Queue_ex")
        else:
            print((self.que[self.front]))

    def enque(self, data):
        if self.full():
            print("Queue_ex is full")
        elif self.rear == -1:
            self.front = 0
            self.rear += 1
            self.que[self.rear]= data
            print("Done")

    def deque(self):
        if self.empty():
            print("empty Queue_ex")




q = Queue_ex()
q.enque(10)
q.peek()