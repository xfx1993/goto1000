def getWinner( arr, k):
    """
    :type arr: List[int]
    :type k: int
    :rtype: int
    """
    size = len(arr)
    if k >= len(arr) - 1:
        return max(arr)

    curmax = -1

    leftmax = [0 for i in range(size)]
    for i in range(size):
        if arr[i] > curmax:
            leftmax[i] = arr[i]
            curmax = arr[i]
        else:
            leftmax[i] = curmax

    stack = []

    for i in range(size):
        if not stack:
            stack.append([i, arr[i]])
        else:
            while stack and arr[i] > stack[-1][1]:
                inx, val = stack.pop()
                if i-inx-1 != 0:
                    if leftmax[inx] == val :
                        cur=i-inx-1
                        if inx!=0:
                            cur = i-inx
                        if cur >= k:
                            return val

            stack.append([i, arr[i]])

arr = [1,9,8,2,3,7,6,4,5]
k = 7

print(getWinner( arr, k))