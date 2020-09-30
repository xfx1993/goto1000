def maxSumTwoNoOverlap( A, L, M):
    """
    :type A: List[int]
    :type L: int
    :type M: int
    :rtype: int
    """
    #计算当前位置当右边长度为l的滑块最大和

    size = len(A)

    def get_left_max_list(n):
        cursum = 0
        maxsum = 0
        tail=size-1
        leftmax = [0 for i in range(size)]
        for i in range(size-1,-1,-1):
            if tail-i+1<n:
                cursum+=A[i]
            else:
                cursum += A[i]
                if cursum>maxsum:
                    maxsum = cursum
                leftmax[i]=maxsum
                cursum-=A[tail]
                tail-=1
        return leftmax

    def getmaxsum(l,r):
        leftmaxlsit = get_left_max_list(l)
        cursum = 0
        maxsum = 0
        tail = 0
        for i in range(size - l):
            if i - tail + 1 < r:
                cursum += A[i]
            else:
                cursum += A[i]
                if cursum + leftmaxlsit[i + 1] > maxsum:
                    maxsum = cursum + leftmaxlsit[i + 1]
                cursum -= A[tail]
                tail += 1
        return maxsum

    return max(getmaxsum(L,M),getmaxsum(M,L))


A = [3,8,1,3,2,1,8,9,0]
L = 3
M = 2
print(maxSumTwoNoOverlap(A,L,M))
