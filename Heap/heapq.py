import heapq

# initializing list
li = [5, 7, 9, 1, 3, 2]

# using heapify to convert list into heap (min-heap)
heapq.heapify(li)

# printing created heap
print ("The created heap is : ",end="")
print (list(li))

# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)

# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li))

# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))

print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li, 2))
print (list(li))
# using heapreplace() to push and pop items simultaneously
# pops 3
print ("The popped item using heapreplace() is : ",end="")
print (heapq.heapreplace(li, 22))
print (list(li))

print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li))