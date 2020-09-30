def twoSumLessThanK(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    A.sort()
    size = len(A)

    def findnear(num, target):
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] <= target:
                left = mid + 1
            else:
                right = mid

        if target == A[left]:
            return target + num

        if A[left] + num < K:
            return A[left] + num

        else:
            return A[left - 1] + num

    mindiff = float('inf')
    res = 0
    for i in range(size):
        if K - A[i] < A[0]:
            break
        if K - A[i] == A[0]:
            return K
        target = K - A[i]
        cur = findnear(A[i], target)
        if K - cur < mindiff:
            res = cur
            mindiff = K - cur
    return res


A = [34,23,1,24,75,33,54,8]
K= 60
print(twoSumLessThanK(A,K))