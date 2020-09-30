def maxSumOfThreeSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    size =len(nums)
    right1 = [[0,0] for i in range(size)]
    right2 = [[0,0,0] for i in range(size)]
    curmax = 0
    curmax_index=-1
    cur = 0
    index = size-1
    for i in range(size-1,-1,-1):
        if index-i+1<k:
            cur+=nums[i]
        else:
            cur+=nums[i]
            if cur>=curmax:
                curmax = cur
                curmax_index = i
            right1[i]=[curmax,curmax_index]
            cur = cur-nums[index]
            index-=1
    curmax = 0
    curmax_index=-1
    curmax_next_index = -1
    cur = 0
    index = size-k-1
    for i in range(size-k-1,-1,-1):
        if index-i+1<k:
            cur+=nums[i]
        else:
            cur+=nums[i]
            temp = cur+right1[i+k][0]
            if temp>=curmax:
                curmax = temp
                curmax_index = i
                curmax_next_index = right1[i+k][1]
            right2[i]=[curmax,curmax_index,curmax_next_index]
            cur = cur-nums[index]
            index -=1


    curmax = 0
    curmax_index = -1
    curmax_next_index = -1
    curmax_next_next_index = -1
    cur = 0
    index = 0
    for i in range(0,size-2*k):
        if i-index+1<k:
            cur+=nums[i]
        else:
            cur+=nums[i]
            temp = cur + right2[i + 1][0]
            if temp>curmax:
                curmax = temp
                curmax_index = i-k+1
                curmax_next_index = right2[i+1][1]
                curmax_next_next_index = right2[i+1][2]
            cur-=nums[index]
            index+=1
    return [curmax_index,curmax_next_index,curmax_next_next_index]



nums = [1,2,1,2,6,7,5,1]
k = 2

print(maxSumOfThreeSubarrays(nums,k))