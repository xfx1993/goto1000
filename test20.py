def minSwaps(data):
    """
    :type data: List[int]
    :rtype: int
    """
    size = len(data)
    dp = [0 for i in range(size)]
    count = 0
    for i in range(size):
        if data[i]==1:
            count+=1
        if i==0:
            dp[0]=1 if data[0]==1 else 0
        else:
            dp[i]= dp[i-1]+data[i]
    left = count-1
    change = float('inf')
    for i in range(left,size):
        if data[i]==1:
            curchange=0
            if i-count+1==0:
                curchange = count - dp[i]
            else:
                curchange = count -(dp[i]-dp[i-count])
            if curchange<change:
                change = curchange
    return change if change!=float('inf') else 0


data = [0,0,0,1,0]
print(minSwaps(data))


