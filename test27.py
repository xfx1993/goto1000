def busRapidTransit( target, inc, dec, jump, cost):
    """
    :type target: int
    :type inc: int
    :type dec: int
    :type jump: List[int]
    :type cost: List[int]
    :rtype: int
    """
    def findroute(cur_target):
        if cur_target==0:
            return 0

        mincost = cur_target*inc
        for i,val in enumerate(jump):
            if cur_target>1:
                if cur_target%val==0:
                    mincost =min(mincost,cost[i]+findroute(cur_target//val))
                else:
                    bias = cur_target%val
                    if cur_target-bias>=0:
                        mincost=min(mincost,bias*inc+cost[i]+findroute(cur_target//val))
                    mincost = min(mincost,(val-bias)*dec+cost[i]+findroute(cur_target//val+1))
        return mincost

    return findroute(target)

target = 612
inc = 4
dec = 5
jump = [3,6,8,11,5,10,4]
cost = [4,7,6,3,7,6,4]


print(busRapidTransit( target, inc, dec, jump, cost))