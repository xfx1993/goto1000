def longestSubsequence( arr, difference):
    """
    :type arr: List[int]
    :type difference: int
    :rtype: int
    """
    size =len(arr)
    dp = [0 for i in range(size)]

    if size ==1:
        return 1
    dp[0]=1
    used=dict()
    used[arr[0]]=0


    for i in range(1,size):
        if arr[i]-difference in used:
            dp[i] = dp[used[arr[i]-difference]]+1
            used[arr[i]]=i
        else:
            dp[i]=1
            used[arr[i]]=i
    return max(dp)

arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(longestSubsequence(arr,difference))


