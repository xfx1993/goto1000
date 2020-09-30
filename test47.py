def jobScheduling( startTime, endTime, profit):
    """
    :type startTime: List[int]
    :type endTime: List[int]
    :type profit: List[int]
    :rtype: int
    """
    size = len(startTime)
    sep = [[startTime[i], endTime[i], profit[i]] for i in range(size)]
    sep.sort(key=lambda x: x[0])

    dp = [0 for i in range(size)]

    for i in range(size-1,-1,-1):
        if i==size-1:
            dp[i] = sep[i][2]
            continue
        curend = sep[i][1]
        left = i+1
        right=size-1
        while left < right:
            mid = (left + right) // 2
            if sep[mid][0] < curend:
                left = mid + 1
            else:
                right = mid
        if sep[left][0]>=curend:
            dp[i] = max(sep[i][2]+dp[left],dp[i+1])
        else:
            dp[i] = max(sep[i][2],dp[i+1])

    return dp[0]

startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]
print(jobScheduling(startTime, endTime, profit))