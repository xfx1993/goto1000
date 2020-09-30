def numSubarrayProductLessThanK( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    size = len(nums)
    dp = [0 for i in range(size)]

    for i in range(size):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = nums[i] * dp[i - 1]
    count = 0
    for i in range(size):
        if nums[i] >= k:
            count += 0
            continue
        if dp[i] < k:
            count += i+1
        else:
            left = 0
            right = i-1
            while left < right:
                mid = (left + right) // 2
                cur = dp[i]/dp[mid]
                if cur >= k:
                    left = mid + 1
                else:
                    right = mid
            n = i - left
            count += n
    return count

nums =[10,9,10,4,3,8,3,3,6,2,10,10,9,3]
k = 19
print(numSubarrayProductLessThanK(nums,k))