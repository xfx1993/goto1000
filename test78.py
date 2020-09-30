def maxChunksToSorted( arr):
    """
    :type arr: List[int]
    :rtype: int
    """

    size = len(arr)
    rightmin = [0 for i in range(size)]
    curmin = arr[-1]
    for i in range(size - 1, -1, -1):
        curmin = min(curmin, arr[i])
        rightmin[i] = curmin

    leftmax = arr[0]
    count = 0
    for i in range(size - 1):
        leftmax = max(leftmax, arr[i])
        if leftmax==i and rightmin[i+1]==i+1:
            leftmax = arr[i + 1]
            count += 1
    return count + 1

print(maxChunksToSorted([1,0,2,3,4]))