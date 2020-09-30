def minReorder( n, connections):
    """
    :type n: int
    :type connections: List[List[int]]
    :rtype: int
    """
    graph = dict()

    for i in range(n):
        graph[i] = dict()

    for s, v in connections:
        graph[s][v] = 1
        graph[v][s] = -1

    count = [0]
    used = dict()
    used[0] = 1

    def change_route(node, used):
        for nextnode in graph[node].keys():
            if nextnode not in used and graph[nextnode][node] == -1:
                count[0] += 1
                used[nextnode] = 1
                change_route(nextnode, used)
            elif nextnode not in used and  graph[nextnode][node] == 1:
                used[nextnode] = 1
                change_route(nextnode, used)

    change_route(0, used)
    return count[0]

n=5
connection = [[1,0],[1,2],[3,2],[3,4]]

print(minReorder(n,connection))