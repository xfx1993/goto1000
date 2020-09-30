def canCompleteCircuit( gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    size = len(gas)

    def dfs(start, cur, curgas, flag):
        if flag == 1 and cur == start:
            return True

        nextgas = curgas + gas[cur] - cost[cur]

        if nextgas < 0:
            return False
        else:
            if cur + 1 == size:
                cur = 0
                flag = 1
                return dfs(start, 0, nextgas, flag)
            else:
                return dfs(start, cur + 1, nextgas, flag)

    for i in range(size):
        if gas[i] >= cost[i]:
            if dfs(i, i, 0, 0):
                return i


gas = [1,2,3,4,5]
cost =[3,4,5,1,2]
print(canCompleteCircuit(gas,cost))