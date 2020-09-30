def maxNonOverlapping( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    size = len(nums)
    cursum = 0
    count =0
    used = dict()
    for i in range(len(nums)):
        cursum = cursum+nums[i]
        if cursum==target:
            cursum=0
            count+=1
            used.clear()
        elif cursum-target in used:
            cursum =0
            count+=1
            used.clear()
        used[cursum]=1
    return count

nums =[-1,3,5,1,4,2,-9,5,6,7,4,5,4,3,4,5,-5,-4,-6,-3,-5,-2,-4,-5,-3,-4,-3,-4,-2,-1]
target= 9

print(maxNonOverlapping(nums,target))