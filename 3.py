def maxSubarraySumCircular( A):
    """
    :type A: List[int]
    :rtype: int
    """
    size = len(A)
    A = A + A
    if max(A) <= 0:
        return max(A)
    tail = 0
    cursum = 0
    maxsum = 0
    for i in range(size * 2):
        cursum = cursum + A[i]
        while tail <= i and (cursum <= 0 or i - size >= tail or A[tail]<=0):
            cursum = cursum - A[tail]
            maxsum = max(cursum, maxsum)
            tail += 1
        maxsum = max(cursum, maxsum)
    return maxsum


A= [5,5,0,-5,3,-3,2]
print(maxSubarraySumCircular(A))