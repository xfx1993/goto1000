def numSubarrayProductLessThanK(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    size = len(nums)
    tail = 0
    front = 0
    count = 0
    cur = 1
    while front < size:
        if cur * nums[front] < k:
            cur = nums[front] * cur
            count += front - tail + 1
            front += 1
        else:
            cur = cur * nums[front]
            while cur >= k:
                cur = cur // nums[tail]
                tail += 1
            count += front - tail + 1
            front += 1
    return count

nums =[10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 19
print(numSubarrayProductLessThanK(nums,k))


