def findLengthOfShortestSubarray( arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    size = len(arr)
    indexfront = -1
    indextail = -1
    for i in range(0,size-1):
        if arr[i]>arr[i+1]:
            indexfront = i
            break
    if indexfront==-1:
        return 0
    for i in range(size-1,indexfront,-1):
        if arr[i]<arr[i-1]:
            indextail = i
            break
    if indexfront==0 and indextail==size-1:
        if arr[indextail]<arr[indexfront]:
            return size-1
        else:
            return size-2
    left = 0
    for i in range(indexfront,-1,-1):
        if arr[i]<=arr[indextail]:
            left = i
            break
    right = size-1
    for i in range(indextail,size):
        if arr[i]>=arr[indexfront]:
            right = i
            break
    minlength = 999999
    for i in range(left,indexfront+1):
        for j in range(right,indextail-1,-1):
            if arr[i]>arr[j]:
                if j+1<size:
                    if j-i<minlength:
                        minlength = j-i
                break
        else:
            if j-i-1<minlength:
                minlength = j-i-1
    if minlength==999999:
        return min(indexfront-left+1,right-indextail+1)


    return minlength


arr =[10,13,17,21,15,15,9,17,22,22,13]
print(findLengthOfShortestSubarray(arr))




