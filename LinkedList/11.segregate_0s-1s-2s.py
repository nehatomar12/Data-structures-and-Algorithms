
'''
	Function to segregate the list of
	0s,1s and 2s.

	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
class Node:
    def __init__(self, data=None):
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

    def sortLL(self):
        trav = self.head

        #Dummy Nodes to avoid too many None Checks at the end.
        zeroL = Node(0)
        oneL = Node(1)
        twoL = Node(2)

        zero = zeroL
        one = oneL
        two = twoL

        while trav:
            if trav.data == 0:
                zero.next = trav
                zero = zero.next
            elif trav.data == 1:
                one.next = trav
                one = one.next
            elif trav.data == 2:
                two.next = trav
                two = two.next
            trav = trav.next

        #joining to 3 lists with head at zeroL, to form one single list
        if oneL.next :
            zero.next = oneL.next
        else:
            zero.next = twoL.next
        one.next = twoL.next
        two.next = None

        #return the heaL of the new list formeL.
        return zeroL.next


list_obj = LL()
l1 = [0,0,1,2,1,2]

for i in l1:
    list_obj.addLast(i)

list_obj.listprint(list_obj.head)
head = list_obj.sortLL()
list_obj.listprint(head)
