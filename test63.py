def findSquare( matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    row = len(matrix)
    col = len(matrix[0])
    bias = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
    dp = [[[0,0,0] for i in range(col)] for j in range(row)]
    maxres=0
    maxpos =[201,201]
    for i in range(row-1,-1,-1):
        for j in range(col-1,-1,-1):
            if matrix[i][j]==1:
                if 1<=i<row-1 and 1<=j<col-1:
                    for bi,bj in bias:
                        if matrix[bi+i][bj+j]==1:
                            break
                    else:
                        matrix[i][j]=0
            if i==row-1 and j==col-1:
                if matrix[i][j]==0:
                    dp[i][j]=[1,1,1]
                    maxres=1
                    maxpos=[i,j]
            elif i==row-1 and j!=col-1:
                if matrix[i][j]==0:
                    dp[i][j][0]=dp[i][j+1][0]+1
                    dp[i][j][1]=1
                    dp[i][j][2]=1
                    if dp[i][j][1]>=maxres:
                        maxres = dp[i][j][1]
                        maxpos =[i,j]
            elif i!=row-1 and j ==col-1:
                if matrix[i][j]==0:
                    dp[i][j][0]=1
                    dp[i][j][1]=1
                    dp[i][j][2]=dp[i+1][j][0]+1
                    if dp[i][j][1]>=maxres:
                        maxres = dp[i][j][1]
                        maxpos = [i, j]
            else:
                if matrix[i][j]==0:
                    dp[i][j][0]=dp[i][j+1][0]+1
                    dp[i][j][2]=dp[i+1][j][2]+1
                    if min(dp[i][j][0],dp[i][j][2])>dp[i+1][j+1][1]:
                        dp[i][j][1] =dp[i+1][j+1][1]+1
                    else:
                        dp[i][j][1]=  min(dp[i][j][0],dp[i][j][2])
                    if dp[i][j][1] >= maxres:
                        maxres =  dp[i][j][1]
                        maxpos = [i, j]
    return [maxpos[0],maxpos[1],maxres]





matrix =[[1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
         [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1, 0, 0, 1, 1, 1]]

print(findSquare(matrix))