def numDistinctIslands(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row = len(grid)
    col = len(grid[0])
    bias= [[1,0],[-1,0],[0,1],[0,-1]]

    def issameland(land1,land2):
        if len(land1)!=len(land2):
            return False
        size = len(land1)
        bias_x = land1[0][0]-land2[0][0]
        bias_y = land1[0][1]-land2[0][1]

        for i in range(1,size):
            if land2[i][0]+bias_x!=land1[i][0] or land2[i][1]+bias_y!=land1[i][1]:
                return False
        return True

    visited = [[0 for i in range(col)] for j in range(row)]
    islands=[]
    for i0 in range(row):
        for j0 in range(col):
            curisland = []
            if grid[i0][j0]==1 and visited[i0][j0]==0:
                curisland.append([i0,j0])
                nodes = [[i0,j0]]
                visited[i0][j0]=1
                while nodes:
                    curnodes = []
                    for i,j in nodes:
                        for i_,j_ in bias:
                            if 0<=i+i_<row and 0<=j+j_<col and grid[i+i_][j+j_]==1 and visited[i+i_][j+j_]==0:
                                curnodes.append([i+i_,j+j_])
                                visited[i+i_][j+j_]=1
                                x=i+i_
                                y=j+j_
                                if not (1<=x<row-1 and 1<=y<col-1 and grid[x+1][y]==1 and grid[x-1][y]==1 and grid[x][y+1]==1 and grid[x][y-1]==1):
                                    curisland.append([x,y])
                    nodes =curnodes
                curisland.sort(key=lambda x:(x[0],x[1]))
                if not islands:
                    islands.append(curisland)
                else:
                    for land in islands:
                        if issameland(land,curisland):
                            continue
                    else:
                        islands.append(curisland)

    return len(islands)

grid = [[1,0,1],[1,0,0]]
print(numDistinctIslands(grid))