def shortestAlternatingPaths( n, red_edges, blue_edges):
    """
    :type n: int
    :type red_edges: List[List[int]]
    :type blue_edges: List[List[int]]
    :rtype: List[int]
    """
    red_graph = dict()
    blue_graph = dict()

    for i in range(n):
        red_graph[i] = dict()
        blue_graph[i] = dict()

    for s, v in red_edges:
        red_graph[s][v] = 1

    for s, v in blue_edges:
        blue_graph[s][v] = 1

    def bfs(g1, g2):
        distance = [101 for i in range(n)]
        distance[0] = 0
        v1 = [[0 for i in range(n)] for j in range(n)]
        v2 = [[0 for i in range(n)] for j in range(n)]
        nodes = [0]
        cen = 0
        g = None
        visited = None
        while nodes:
            cen += 1
            nextnodes = []
            if cen % 2 == 1:
                g = g1
                visited = v1

            else:
                g = g2
                visited = v2
            for node in nodes:
                for nextnode in g[node].keys():
                    if visited[node][nextnode] == 0:
                        distance[nextnode] = min(distance[nextnode],cen)
                        visited[node][nextnode] = 1
                        nextnodes.append(nextnode)
            nodes = nextnodes
        return distance

    rdis = bfs(red_graph, blue_graph)
    bdis = bfs(blue_graph, red_graph)

    resdistance = [min(rdis[i], bdis[i]) for i in range(n)]
    for i in range(n):
        if resdistance[i] == 101:
            resdistance[i] = -1
    return resdistance


n =5
red_edges = [[0,1],[1,2],[2,3],[3,4]]
blue_edges =[[1,2],[2,3],[3,1]]
print(shortestAlternatingPaths(n,red_edges,blue_edges))