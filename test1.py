def combinationSum( candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    size = len(candidates)
    stack= []
    res = []
    def dfs(cursum,stack,index):

        if cursum==target:
            res.append(stack[:])
            return
        if cursum>target:
            return
        if index>=size:
            return
        for i in range(index,size):
            stack.append(candidates[i])
            cursum+=candidates[i]
            dfs(cursum,stack,i)
            cursum-=stack.pop()
    dfs(0,stack,0)
    return res

candidates = [2,3,5]
target = 8
print(combinationSum(candidates,target))