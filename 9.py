def paintingPlan( n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """

    if k<n:
        return 0
    paint = [[0 for i in range(n)] for j in range(n)]

    row = [[1,i] for i in range(n)]
    col = [[2,i] for i in range(n)]

    all = row+col

    visited = [0 for i in range(2*n)]

    stack = []
    res =[]
    def pain(stack):
        if len(stack)==k:
            re = sorted(stack,key=lambda x: (x[0],x[1]))
            if re not in res:
                res.append(re[:])
            return
        if len(stack) >= k:
            return
        for i in range(2*n):
            if visited[i]==0:
                id,g = all[i]
                visited[i]=1
                painnode = []
                if id==1:
                    for j in range(n):
                        if [g,j] not in stack:
                            paint[g][j] = 1
                            painnode.append([g,j])
                            stack.append([g,j])
                if id==2:
                    for j in range(n):
                        if [j, g] not in stack:
                            paint[j][g] = 1
                            painnode.append([j, g])
                            stack.append([j, g])
                pain(stack)
                for x,y in painnode:
                    paint[x][y]=0
                    stack.pop()
                visited[i]=0
    pain(stack)
    print(res)
    return len(res)


print(paintingPlan(4,15))









