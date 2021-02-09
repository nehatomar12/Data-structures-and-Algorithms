"""
Given a list of non negative integers, arrange them in such a manner that they form
the largest number possible.

Input:
    N = 5
    Arr[] = {3, 30, 34, 5, 9}
Output: 9534330

"""

def rearrange(arr, size):
    result = ""
    max_e = max(arr)
    max_ele_dig = len(str(max_e))+1
    new_array = []
    for i in arr:
        temp = str(i)*max_ele_dig
        new_array.append((temp[:max_ele_dig], i))
    print(new_array)
    for i in sorted(new_array, reverse=True):
        result += str(i[1])
    print(result)

if __name__ == "__main__":
    arr = [3, 30, 34, 5, 9]
    size = len(arr)
    rearrange(arr, size)