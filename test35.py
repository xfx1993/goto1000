def canArrange( arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: bool
    """
    all = sum(arr)
    if all % k != 0:
        return False

    arr.sort()
    size = len(arr)
    used = dict()

    for i in range(size):
        if i == 0:
            used[arr[i]] = 1
            continue
        for key,value in used.items():
            if (key+arr[i])%k==0:
                used[key]-=1
                if used[key]==0:
                    del used[key]
                    break
        else:
            if arr[i] not in used:
                used[arr[i]]=1
            else:
                used[arr[i]]+=1



    if not used:
        return True
    else:
        return False


arr=[-4,-7,5,2,9,1,10,4,-8,-3]
k=3
print(canArrange(arr, k))