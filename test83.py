def minDistance(height, width, tree, squirrel, nuts):
    """
    :type height: int
    :type width: int
    :type tree: List[int]
    :type squirrel: List[int]
    :type nuts: List[List[int]]
    :rtype: int
    """
    row = height
    col = width
    bias = [[1,0],[-1,0],[0,1],[0,-1]]
    nutscount = len(nuts)

    def bfs(start):
        """
        :param start:
        :return:distance,松鼠到所有坚果的距离
        """
        nodes = [start]
        visited = [[0 for i in range(col)] for j in range(row)]
        visited[start[0]][start[1]]=1
        dis =0
        distance = dict()
        count = 0
        while nodes:
            dis+=1
            nextnodes=[]
            for x,y in nodes:
                for x_,y_ in bias:
                    if 0<=x+x_<row and 0<=y+y_<col and visited[x+x_][y+y_]==0:
                        if [x+x_,y+y_] in nuts:
                            distance[(x+x_,y+y_)] = dis
                            count+=1
                            if count==nutscount:
                                return distance
                        visited[x+x_][y+y_]=1
                        nextnodes.append([x+x_,y+y_])
            nodes = nextnodes
        return distance
    squirrel2nuts_distance = bfs(squirrel)
    tree2nuts_distance= bfs(tree)
    alldis = 0
    for key,value in tree2nuts_distance.items():
        alldis+=value*2
    mindis = float('inf')
    for key,dis in squirrel2nuts_distance.items():
        if dis+alldis-tree2nuts_distance[key]<mindis:
            mindis =dis+alldis-tree2nuts_distance[key]
    return mindis



h=5
w=7
t=[2,2]
s=[4,4]
n =[[3,0], [2,5]]
print(minDistance(h,w,t,s,n))










