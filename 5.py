def rangeSum(nums, n, left, right):
    """
    :type nums: List[int]
    :type n: int
    :type left: int
    :type right: int
    :rtype: int
    """
    import heapq
    leftlist = []
    sizeleft = 0
    rightlist = []
    sizeright =0
    left = left-1

    size = len(nums)
    dp = [0 for i in range(size)]

    for i in range(size):
        if i == 0:
            dp[0] = nums[0]
        else:
            dp[i] = dp[i - 1] + nums[i]

    for k in range(1,size+1):
        flagleft =True
        flagright = True
        for f in range(k-1,size):
            if f-k+1==0:
                if sizeleft<left:
                    heapq.heappush(leftlist,-dp[f])
                    sizeleft+=1
                    flagleft=False
                else:
                    if leftlist and -dp[f]>leftlist[0]:
                        heapq.heappop(leftlist)
                        heapq.heappush(leftlist,-dp[f])
                        flagleft = False
                if sizeright<right:
                    heapq.heappush(rightlist,-dp[f])
                    sizeright+=1
                    flagright=False
                else:
                    if -dp[f]>rightlist[0]:
                        heapq.heappop(rightlist)
                        heapq.heappush(rightlist,-dp[f])
                        flagright = False
            else:
                if sizeleft<left:
                    heapq.heappush(leftlist,-dp[f]+dp[f-k])
                    sizeleft+=1
                    flagleft = False
                else:
                    if leftlist and -dp[f]+dp[f-k]>leftlist[0]:
                        heapq.heappop(leftlist)
                        heapq.heappush(leftlist,-dp[f]+dp[f-k])
                        flagleft = False
                if sizeright<right:
                    heapq.heappush(rightlist,-dp[f]+dp[f-k])
                    sizeright+=1
                    flagright = False
                else:
                    if -dp[f]+dp[f-k]>rightlist[0]:
                        heapq.heappop(rightlist)
                        heapq.heappush(rightlist,-dp[f]+dp[f-k])
                        flagright = False
        if  (flagleft and flagright):
            break

    return -sum(rightlist)+sum(leftlist) if leftlist else -sum(rightlist)



nums = [1,2,3,4]
n = 4
left = 1
right = 10
print(rangeSum(nums,n,left,right))