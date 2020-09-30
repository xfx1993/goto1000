def jobScheduling(self, startTime, endTime, profit):
    """
    :type startTime: List[int]
    :type endTime: List[int]
    :type profit: List[int]
    :rtype: int
    """
    size = len(startTime)
    sep = [[startTime[i], endTime[i], profit[i]] for i in range(size)]
    sep.sort(key=lambda x: x[0])

    memo = dict()

    def findjob(index, pre_chose_end):
        if index == size:
            return 0
        if pre_chose_end in memo:
            return memo[pre_chose_end]
        curprofit = 0

        left = index
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if sep[mid][0] < pre_chose_end:
                left = mid + 1
            else:
                right = mid
        for i in range(left, size):
            if sep[i][0]>sep[left][1]:
                break
            if sep[i][0] >= pre_chose_end:
                curprofit = max(sep[i][2] + findjob(index + 1, sep[i][1]), curprofit)
        memo[pre_chose_end] = curprofit
        return curprofit

    return findjob(0, 0)