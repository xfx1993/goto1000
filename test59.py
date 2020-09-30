def mincostTickets( days, costs):
    """
    :type days: List[int]
    :type costs: List[int]
    :rtype: int
    """
    size = len(days)
    dp = [0 for i in range(size)]

    for i in range(size):
        if i==0:
            dp[i]=min(costs)
        else:
            curcost = 999999999
            curcost = min(dp[i-1]+costs[0],curcost)
            index = 0
            for j in range(i-1,-1,-1):
                if days[i]-days[j]>=7:
                    index = j
                    curcost = min(costs[1] + dp[index], curcost)
                    break
            else:
                curcost = min(curcost,costs[1])
            index =0
            for k in range(i-1,-1,-1):
                if days[i]-days[k]>=30:
                    index = k
                    curcost = min(costs[2] + dp[index], curcost)
                    break
            else:
                curcost = min(curcost,costs[2])

            dp[i] =curcost

    return dp[-1]

days = [1,4,6,7,8,20]
costs = [2,7,15]
print(mincostTickets(days,costs))