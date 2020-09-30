def snakesAndLadders( board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    size  = len(board)
    visited = [0 for i in range(size*size+1)]
    helper = dict()
    x = size-1
    y =0
    count = 1
    bias = 1
    while x>=0:
        helper[count]=[x,y]
        y = y+bias
        count+=1
        if y==size:
            x=x-1
            y=size-1
            bias=-1*bias
        elif y==-1:
            x=x-1
            y=0
            bias=-1*bias

    s_x= size-1
    s_y = 0
    visited[1]=1
    def getminsetp(curnum):
        if curnum==size*size:
            return 0
        cur =999999
        index =6
        for i in range(1,7):
            if curnum+i<=size*size:
                s,v = helper[curnum+i]
                if board[s][v]!=-1 and visited[curnum+i]==0:
                    visited[curnum+i]=1
                    nextnum =board[s][v]
                    if nextnum==1:
                        continue
                    visited[nextnum]=1
                    cur = min(cur,1+getminsetp(nextnum))
                    visited[nextnum]=0
                    #visited[curnum+i]=0
            else:
                index=i
                break
        if index-1+curnum!=size*size:
            for j in range(index-1,0,-1):
                k,v = helper[curnum+j]
                if visited[curnum+j]==0 and board[k][v]==-1:
                    visited[curnum+j]=1
                    cur=min(cur,1+getminsetp(curnum+j))
                    visited[curnum+j]=0
                    break


        return cur

    mincost = getminsetp(1)
    return mincost if mincost!=999999 else -1

board = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]




print(snakesAndLadders(board))


