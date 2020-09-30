def minimumDeleteSum( s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: int
    """

    row = len(s1)
    col = len(s2)

    dp = [[0 for i in range(col)] for j in range(row)]

    for i in range(row):
        for j in range(col):
            if i==0 and j==0:
                dp[i][j]=ord(s1[i]) if s1[0]==s2[0] else 0
            if i == 0 and j != 0:
                dp[i][j] = max(ord(s1[i]),dp[i][j-1]) if s1[i] == s2[j] else dp[i][j-1]
            elif  i != 0 and j == 0:
                dp[i][j] = max(ord(s1[i]),dp[i-1][j]) if s1[i] == s2[j] else dp[i-1][j]
            else:
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i])
                dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i - 1][j])


    alls1 = 0
    for s in s1:
        alls1 +=ord(s)
    alls2 = 0
    for s in s2:
        alls2 +=ord(s)

    return alls1-dp[-1][-1]+alls2-dp[-1][-1]


s1 = "delete"
s2 = "leet"
print(minimumDeleteSum(s1,s2))