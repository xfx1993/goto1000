def distinctSubseqII( S):
    """
    :type S: str
    :rtype: int
    """
    size = len(S)
    used = dict()
    for i in S:
        if i in used:
            used[i]+=1
        else:
            used[i]=1
    dp = [0 for i in range(size)]
    cut = 0
    cur = 0
    for i in range(size-1,-1,-1):
        if i==size-1:
            dp[i]=1

        else:
            dp[i]=2*dp[i+1]+1
        used[S[i]] = used[S[i]] - 1
        if used[S[i]] > 0:
            cut += dp[i]
    return (dp[0]-cut)%(10**9+7)


S = "zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn"
print(distinctSubseqII(S))