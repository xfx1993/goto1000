def maxSumAfterPartitioning( arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    size = len(arr)
    dp = [0 for i in range(size+1)]
    dp[-2]=arr[-1]
    for i in range(size-2,-1,-1):
        curmax = 0
        for j in range(i,min(i+k,size)):
            curmax = max(curmax,arr[j])
            dp[i] = max(dp[i],curmax*(j-i+1)+dp[j+1])
    return dp[0]


size = len(arr)
memo = dict()


def dfs(index):
    if index >= size:
        return 0
    if index in memo:
        return memo[index]
    curmax = -1
    cur = 0
    for i in range(index, min(index + k, size)):
        curmax = max(curmax, arr[i])
        cur = max(cur, curmax * (i - index + 1) + dfs(i + 1))
    memo[index] = cur
    return cur


return dfs(0)

arr=[1,15,7,9,2,5,10]
K = 3
print(maxSumAfterPartitioning(arr,k=K))