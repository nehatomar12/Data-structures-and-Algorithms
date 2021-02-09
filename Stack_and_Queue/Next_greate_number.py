
# 1 2 3 4
#

"""
Algo:
  take 2 variable
  next:  it will iterate over array
  element: it will have stack values
  cond: 
    element < next:
        print(next)
        if not empty stack, get new element
    element > next:
        add  element to stack
   add next to stack

"""
def getNGN(array):
    res = {} 
    s = []
    s.append(array[0])
    next = 0
    element = 0

    for i in range(1, len(array)):
        next = array[i]
        if len(s) != 0:
            element = s.pop()
            while element < next:
                res[element] = next
                if len(s) == 0:
                    break
                element = s.pop()
            if element > next:
                s.append(element)
        s.append(next)

    while len(s) != 0:
        res[s.pop()] = -1
    return res
array=[1,5, 2, 7, 11, 3, 0]
res = getNGN(array)
for i in array:
    print(res.get(i), end = " ")
