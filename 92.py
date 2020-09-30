def findMinHeightTrees( n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if n==0:
        return []
    if n==1:
        return [0]
    if n==2:
        return [0,1]
    graph = dict()
    for i in range(n):
        graph[i] = dict()
    for s, v in edges:
        graph[s][v] = 1
        graph[v][s] = 1


    minheight = float('inf')
    minlist = []
    visited =dict()
    nodes = []
    for i in range(n):
        if len(graph[i])==1:
            visited[i]=1
            nodes.append(i)

    while nodes:
        curnode =[]
        for node in nodes:
            for nextnode in graph[node].keys():
                if nextnode not in visited:
                    visited[nextnode]=1
                    curnode.append(nextnode)
        if curnode:
            nodes=curnode
        else:
            return nodes





    return minlist

n= 4
edges = [[1,0],[1,2],[1,3]]

print(findMinHeightTrees(n,edges))