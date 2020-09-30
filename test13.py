def shortestDistance( maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: int
    """
    row = len(maze)
    col = len(maze[0])
    visited = [[0 for i in range(col)] for j in range(row)]

    bias = [[-1, 0], [1, 0], [0, 1], [0, -1]]


    pathsize = []
    visited[start[0]][start[1]]=1
    def roll_ball(curpos,cursize):
        if curpos==destination:
            pathsize.append(cursize)
            return
        for b_i,b_j in bias:
            i,j= curpos
            curlen = 0
            back=[]
            if 0<=i+b_i<row and 0<=j+b_j<col and visited[i+b_i][j+b_j]==0 and maze[i+b_i][j+b_j]==0:
                while 0<=i+b_i<row and 0<=j+b_j<col and maze[i+b_i][j+b_j]==0:
                    i=i+b_i
                    j=j+b_j
                    back.append([i,j,visited[i][j]])
                    visited[i][j]=1
                    curlen+=1
                if back:
                    cursize+=curlen
                    roll_ball([i,j],cursize)
                    cursize-=curlen
                    for x,y,v in back:
                        visited[x][y]=v
    roll_ball(start,0)
    return min(pathsize)

maze = [[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,1],[0,0,0,0,1,0,0]]
start = [0,0]
destion = [8,6]

print(shortestDistance(maze,start,destion))