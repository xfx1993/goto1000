def mincostTickets(days, costs):
    """
    :type days: List[int]
    :type costs: List[int]
    :rtype: int
    """
    size =len(days)
    memo = dict()

    def getmincost(index):
        if index>=size:
            return 0
        if index in memo:
            return memo[index]
        mincost = 99999999
        for i,cost in enumerate(costs):
            if i==0:
                mincost = min(cost+getmincost(index+1),mincost)
            elif i==1:
                curindex = size
                for j in range(index,size):
                    if days[j]>days[index]+6:
                        curindex=j
                        break
                mincost = min(cost+getmincost(curindex),mincost)
            elif i==2:
                curindex = size
                for j in range(index, size):
                    if days[j] > days[index] +29:
                        curindex = j
                        break
                mincost = min(cost + getmincost(curindex), mincost)
        memo[index]=mincost
        return mincost
    return getmincost(0)



days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
print(mincostTickets(days,costs))


