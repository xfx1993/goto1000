def minimumOperations(leaves):
    """
    :type leaves: str
    :rtype: int
    """
    size = len(leaves)
    dp = [[0,0] for i in range(len(leaves))]
    rcount =0
    ycount = 0

    for i,r in enumerate(leaves):
        if i==0:
            if r=='r':
                rcount+=1
                dp[0][0]+=1
            else:
                ycount+=1
                dp[0][0]+=1
        else:
            if r=='r':
                rcount+=1
                dp[i][0]=dp[i-1][0]+1
                dp[i][1] = dp[i-1][1]
            else:
                ycount+=1
                dp[i][1] = dp[i-1][1]+1
                dp[i][0] = dp[i-1][0]
    left_y = []
    right_y = []
    for i in range(1,size):
        if leaves[i]=='y' and leaves[i-1]=='r':
            left_y.append(i)
    for i in range(size-2,-1,-1):
        if leaves[i]=='y' and leaves[i+1]=='r':
            right_y.append(i)
    minchange = float('inf')
    for i in left_y:
        for j in right_y:
            if i>j:
                break
            rnum = dp[j][0]-dp[i-1][0]
            ynum = dp[j][1]-dp[i-1][1]
            curchange = ycount-ynum+rnum
            if curchange<minchange:
                minchange = curchange
    return minchange

leaves = "rrryyyrryyyrr"
print(minimumOperations(leaves))






