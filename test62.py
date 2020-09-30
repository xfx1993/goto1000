def numberOfPatterns(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    tranform = [[],[2,4,5,6,8],[1,3,4,5,6,7,9],[2,4,5,6,8],[1,2,3,5,8,7,9],[1,2,3,4,6,7,8,9],[1,2,3,5,8,7,9],[2,4,5,6,8],[1,3,4,5,6,7,9],[2,4,5,6,8]]
    help = [[],[[3,2],[7,4],[9,5]],[[8,5]],[[1,2],[9,6],[7,5]],[[6,5]],[],[[4,5]],[[1,4],[9,8],[3,5]],[[2,5]],[[3,6],[7,8],[1,5]]]
    def dfs(visited,node,cen,curn):
        if cen==curn:
            return 1
        cur=0
        if node==-1:
            for i in range(1,10):
                if visited[i]==0:
                    visited[i]=1
                    cur+=dfs(visited,i,cen+1,curn)
                    visited[i]=0
        else:
            for i in tranform[node]:
                if visited[i]==0:
                    visited[i]=1
                    cur+=dfs(visited,i,cen+1,curn)
                    visited[i]=0
            for end,helpnum in help[node]:
                if visited[helpnum]==1 and visited[end]==0:
                    visited[end]=1
                    cur += dfs(visited, end, cen + 1, curn)
                    visited[end]=0
        return cur
    count = 0



    for i in range(m,n+1):
        visited = [0 for j in range(10)]
        count+=dfs(visited,-1,0,i)
    return count


print(numberOfPatterns(1,3))