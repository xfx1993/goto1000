def smallestRangeII(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """

    A.sort()
    size = len(A)
    if size == 1:
        return 0


    newbig = max(A[0]+K,A[-1]-K)
    newsmall = min(A[0]+K,A[-1]-K)

    for i in range(1,size-1):
        if newsmall<=A[i]+K<=newbig:
            continue
        if newsmall<=A[i]-K<=newbig:
            continue
        if A[i]+K>newbig and A[i]-K<newsmall:
            if A[i]+K-newsmall<newbig-(A[i]-K):
                newbig = A[i]+K
            else:
                newsmall = A[i]-K
    return newbig-newsmall


A = [1,3,6,7,5,4,6,4,3,6,4,5,7,5,1,5,3]
K= 3
print(smallestRangeII(A,K))