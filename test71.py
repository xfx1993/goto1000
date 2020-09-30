def numSubarrayBoundedMax( A, L, R):
    """
    :type A: List[int]
    :type L: int
    :type R: int
    :rtype: int
    """
    size = len(A)
    pos = []
    for i in range(size):
        if A[i] > R:
            pos.append(i)
    res = 0
    if not pos:
        return (1 + size) * size // 2
    else:
        cur = 0
        for p in pos:
            n = p - cur
            if n != 0:
                res += (1 + n) * n // 2
            cur = p + 1

        if size - cur > 0:
            res += (1 + size - cur) * (size - cur) // 2

    small = 0
    used = dict()
    for i in range(size):
        if A[i] < L and i not in used:
            used[i]=1
            left = 0
            right = 0
            pov = i
            index = i
            while index - 1 >= 0 and A[index - 1] <= A[pov]:
                index = index - 1
                used[index]=1
                left += 1
            index = i
            while index + 1 < size and A[index + 1] <= A[pov]:
                index = index + 1
                used[index]=1
                right += 1
            left = i - left
            right = i + right
            n = right - left + 1
            small += (n + 1) * n // 2


    return res - small


A= [73,55,36,5,55,14,9,7,72,52]
L = 32
R = 69
print(numSubarrayBoundedMax(A,L,R))