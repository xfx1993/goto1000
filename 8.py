def bestSeqAtIndex( height, weight):
    """
    :type height: List[int]
    :type weight: List[int]
    :rtype: int
    """
    hw = [[height[i], weight[i]] for i in range(len(height))]

    hw.sort(key=lambda x:(x[0],-x[1]))

    stack = []




height = [6410,4261,939,8469,3780,6773,2255,474,6940,5581]


weight =[825,9198,4361,8999,8365,7399,6664,218,98,5210]
print(bestSeqAtIndex(height,weight))