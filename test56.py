def findCheapestPrice( n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    graph = dict()
    for i in range(n):
        graph[i] = dict()

    for u, v, w in flights:
        graph[u][v] = w

    visited = [[0 for i in range(n)] for j in range(n)]
    fallstation = dict()
    memo = dict()

    def dfs(cursrc, cen, visited):
        if cursrc == dst and cen <= K:
            return 0
        elif cursrc == dst and cen > K:
            return 999999999
        if (cursrc, cen) in fallstation:
            return fallstation[(cursrc, cen)]
        if (cursrc,cen) in memo:
            return memo[(cursrc,cen)]
        cur = 999999999
        if cursrc not in graph:
            return cur
        for nextstation, price in graph[cursrc].items():
            if visited[cursrc][nextstation] == 0 and nextstation not in fallstation:
                visited[cursrc][nextstation] = 1
                cur = min(price + dfs(nextstation, cen + 1, visited), cur)
                visited[cursrc][nextstation]  = 0
        if cur >= 999999999:
            fallstation[(cursrc, cen)] = cur
        memo[(cursrc,cen)]=cur
        return cur

    mincost = dfs(src, -1, visited)
    print(memo)
    if mincost < 999999999:
        return mincost
    else:
        return -1


n = 5
flights = [[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]]
src =0
dst = 4
K=3
print(findCheapestPrice( n, flights, src, dst, K))