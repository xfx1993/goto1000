def criticalConnections( n, connections):
    """
    :type n: int
    :type connections: List[List[int]]
    :rtype: List[List[int]]
    """
    ##构建图
    graph = dict()
    for i in range(n):
        graph[i]=dict()
    for s,v in connections:
        graph[s][v]=1
        graph[v][s]=1

    ##无向图中找桥

    low=[0 for i in range(n)]
    dfn = [0 for i in range(n)]
    res = []
    def dfs(node,pre,time):
        dfn[node]=time
        low[node]=time
        for nextnode in graph[node]:
            if nextnode!=pre and dfn[nextnode]==0:
                dfs(nextnode,node,time+1)
                if low[node] < low[nextnode]:
                    res.append([node, nextnode])
                low[node]=min(low[node],low[nextnode])
            elif nextnode!=pre and dfn[nextnode]!=0:
                low[node]=min(low[node],low[nextnode])


    dfs(0,-1,1)
    return res

n=10
connections=[[1,0],[2,0],[3,0],[4,1],[5,3],[6,1],[7,2],[8,1],[9,6],[9,3],[3,2],[4,2],[7,4],[6,2],[8,3],[4,0],[8,6],[6,5],[6,3],[7,5],[8,0],[8,5],[5,4],[2,1],[9,5],[9,7],[9,4],[4,3]]
print(criticalConnections( n, connections))






