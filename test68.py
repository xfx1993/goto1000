def findLatestStep(arr, m):
    """
    :type arr: List[int]
    :type m: int
    :rtype: int
    """
    size = len(arr)
    chararr = [0 for i in range(size + 2)]
    head = dict()
    father = [i for i in range(size + 1)]
    memo = 0
    helper = 0

    def findfather(node):
        while father[node] != node:
            father[node] = father[father[node]]
            node = father[node]
        return node

    for i, index in enumerate(arr):
        chararr[index] = 1
        if chararr[index + 1] == 0 and chararr[index - 1] == 0:
            head[index] = 1
            if head[index]==m:
                helper+=1
        elif chararr[index + 1] == 1 and chararr[index - 1] == 0:
            father[index + 1] = father[index]
            head[index] = 1 + head[index + 1]
            if head[index]==m:
                helper+=1
            if head[index+1]==m:
                helper-=1
            del head[index+1]
        elif chararr[index + 1] == 0 and chararr[index - 1] == 1:
            root1 = findfather(index - 1)
            father[index] = root1
            if head[root1]==m:
                helper-=1
            head[root1] += 1
            if head[root1]==m:
                helper+=1
        else:
            root1 = findfather(index - 1)
            father[index] = root1
            father[index+1] = root1
            if head[root1]==m:
                helper-=1
            head[root1] += 1 + head[index+1]
            if head[root1]==m:
                helper+=1
            if head[index+1]==m:
                helper-=1
            del head[index+1]
        if helper>0:
            memo=i+1
    return memo


arr = [3,5,1,2,4]
m = 1
print(findLatestStep(arr,m))