class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __lt__(self, other):
        # Override < operator
        # Error while comparing Node objects
        # TypeError: '<' not supported between instances of 'Node' and 'Node'
        return self.data < other.data

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

def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next
    print(None)

def merge_2sorted_linklist(l1, l2):
    # using dummy node
    new_head = None
    a = l1.head
    b = l2.head
    if a.data > b.data:
        new_head = b
        b = b.next
    else:
        new_head = a
        a = a.next
    s = new_head
    while a and b:
        if a.data > b.data:
            s.next = b
            s=b
            b = b.next
        else:
            s.next = a
            s=a
            a = a.next
    if a:
        s.next = a
    if b:
        s.next = b
    printList(new_head)


def mergeLL_recursive(a, b):
    if not a:
        return b
    elif not b:
        return a
    if a.data <= b.data:
        result = a
        result.next = mergeLL_recursive(a.next, b)
    else:
        result = b
        result.next = mergeLL_recursive(a, b.next)
    return result


def merge_k_ll(all_ll):
    import heapq
    from heapq import heappush, heappop

    # create a priority queue with first node of k linkedlist
    p_queue = [x for x in all_ll]

    heapq.heapify(p_queue)

    # maintain new pointer for result LL
    head = tail = None

    while p_queue:
        min_node = heappop(p_queue)
        if not head:
            head = min_node
        else:
            tail.next = min_node
        tail = min_node
        if min_node.next:
            heappush(p_queue, min_node.next)

    printList(head)

L1 = LL()
L2 = LL()
L3 = LL()

l1 = [1,5, 7]
l2 = [2,3,6,9]
l3 = [4,8,10]

for i in l1:
    L1.addLast(i)
for j in l2:
    L2.addLast(j)
for k in l3:
    L3.addLast(k)

printList(L1.head)
printList(L2.head)
printList(L3.head)

#merge_2sorted_linklist(L1, L2)
# h = mergeLL_recursive(L1.head, L2.head)
# printList( h)
merge_k_ll([L1.head, L2.head, L3.head])
