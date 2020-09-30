def minSumOfLengths( arr, target):
    """
    :type arr: List[int]
    :type target: int
    :rtype: int
    """
    size = len(arr)
    dic = dict()
    dp = [0 for i in range(size)]
    targetlist = []
    for i in range(size):
        if i == 0:
            dp[i]=arr[i]
            dic[dp[i]]=i
        else:
            dp[i]=dp[i-1]+arr[i]
            dic[dp[i]] = i
        if arr[i]==target:
            targetlist.append([i,i,1])
        elif dp[i]==target:
            targetlist.append([0,i,i+1])
        else:
            if dp[i]-target in dic:
                index = dic[dp[i]-target]
                targetlist.append([index+1,i,i-index])
    if not targetlist:
        return -1
    targetlist.sort(key=lambda x:x[2])
    size1 = len(targetlist)
    if size1==1:
        return -1
    minlength=float('inf')
    for i in range(size1-1):
        for j in range(1,size1):
            s1,v1,l1 = targetlist[i]
            s2,v2,l2 = targetlist[j]
            if v1<s2 or v2<s1:
                if l1+l2<minlength:
                    minlength = l1+l2
                    break


    return minlength if minlength!=float('inf') else -1



arr=[2,2,4,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target =20
print(minSumOfLengths(arr,target))


