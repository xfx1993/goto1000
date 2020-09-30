def largestRectangleArea( heights):
    """
    :type heights: List[int]
    :rtype: int
    """

    size = len(heights)
    maxarea = 0
    left = [i for i in range(size)]
    right = [size-1 for i in range(size)]

    stack = []
    for i,h in enumerate(heights):
        if not stack:
            stack.append(i)
        else:
            while  stack and h<heights[stack[-1]]:
                index = stack.pop()
                right[index]=i-1
            if not stack:
                left[i]=0
            else:
                left[i]=stack[-1]+1
            stack.append(i)

    print(left)
    print(right)
    for i in range(size):
        cur = heights[i]
        l = left[i]
        r = right[i]
        maxarea = max(maxarea, (r-l + 1) * cur)
    return maxarea



heights = [3,6,5,7,4,8,1,0]
print(largestRectangleArea(heights))