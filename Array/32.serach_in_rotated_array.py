def _search( nums, low, high, key):
    if low > high:
        return -1

    mid = (low + high)//2
    if nums[mid] == key:
        return mid

    # if low-mid sorted
    # normal Binary search
    if nums[low] <= nums[mid]:
        if nums[low] <= key <= nums[mid]:
            return _search(nums, low, mid-1, key)
        return _search(nums, mid+1, high, key)

    elif nums[mid] <= key <= nums[high]:
        return _search(nums, mid+1, high, key)
    return _search(nums, low, mid-1, key)

def search( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    res = _search(nums, low=0, high=len(nums)-1, key=target)

    if res != -1:
        return res
    return -1


nums = [4,5,6,7,0,1,2]
target= 0
print(search(nums, target))