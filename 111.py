def probabilityOfHeads( prob, target):
    """
    :type prob: List[float]
    :type target: int
    :rtype: float
    """

    size = len(prob)

    dp = [[0 for i in range(size)] for j in range(target+1)]

    for i in range(target+1):
        for j in range(size):
            if i==0 and j==0:
                dp[i][j]=1-prob[j]
            elif i==0:
                dp[i][j]=(1-prob[j])*dp[i][j-1]
            else:
                if j+1<i:
                    continue
                if j==0 and i==1:
                    dp[i][j]=prob[j]
                else:
                    dp[i][j]=dp[i][j-1]*(1-prob[j])+dp[i-1][j-1]*prob[j]

    return dp[-1][-1]








prob = [0.5,0.3,0.4,0.1,0.6,0.4,0,0.5,0.2,0.7]
target = 15
print(probabilityOfHeads(prob,target))


size = len(prob)
        memo = dict()
        right= [0 for i in range(size)]
        right[-1]=1-prob[-1]
        for i in range(size-1,-1,-1):
            if i==size-1:
                continue
            right[i]=right[i+1]*(1-prob[i])

        def flit(index,n):
            if (index,n) in memo:
                return memo[(index,n)]
            if n==target:
                if index==size:
                    return 1
                return right[index]
            if index==size:
                return 0
            cur1=0
            cur1+=prob[index]*flit(index+1,n+1)
            cur1+=(1-prob[index])*flit(index+1,n)
            memo[(index,n)]=cur1
            return cur1
        return flit(0,0)