
arr = [50,80] #,20,40,70,30,10,60]
arr = [2,5,1,3,4]
#arr = [1,2,3,4]
# print "Bef Array: ", len(arr)

# for i in range(len(arr)-1):
#    print arr[i], " ",

def swap(x,y):
   # t = x
   # x = y
   # y = t
   #y, x = x,y
   return x, y
# a = 1
# b = 2
# print a , " ", b
# a,b = swap(a,b)
# print a , " ", b


def bubbleSort(arr):
   t =0
   for passnum in range(len(arr)-1,0,-1):
      for i in range(passnum):
         if arr[i]>arr[i+1]:
            t += 1
            tmp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=tmp
   print(t)

bubbleSort(arr)
print(("Aft Array: ", arr))

def selectionSort(arr):
   for i in range(0,len(arr)-1):
      for j in range(i+1,len(arr)):
         if arr[i] > arr[j]:
            tmp=arr[i]
            arr[i]=arr[j]
            arr[j]=tmp

#selectionSort(arr)
#print "Aft Array: ", arr

def insertionSort(arr):
   for index in range(1,len(arr)):
      currentvalue = arr[index]
      position = index
      while position>0 and arr[position-1]>currentvalue:
         arr[position]=arr[position-1]
         position = position-1
      arr[position]=currentvalue

# insertionSort(arr)
# print "Aft Array: ", arr