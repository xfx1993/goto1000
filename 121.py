def maxWidthRamp( A):
    """
    :type A: List[int]
    :rtype: int
    """
    size = len(A)
    dp = [0 for i in range(size)]

    dp[0] = 0
    maxw = 0
    for i in range(1, size):
        cur = i

        index = i - 1
        while index >= 0:
            if A[index] > A[i]:
                if dp[index] == index:
                    break
                elif A[index] == A[i]:
                    cur = dp[index]
                    break
                else:
                    index -=1
            else:
                cur = dp[index]
                index = dp[index] - 1
        dp[i] = cur
        if i - dp[i] > maxw:
            maxw = i - dp[i]
    return maxw



A=[49999,49999,49999,49998,49995,49990,49988,49988,49986,49983,49983,49980,49979,49975,49975,49975,49974,49972,49971,49969,49968,49968,49968,49967,49965,49964,49963,49963,49962,49959,49957,49957,49953,49953,49952,49951,49950,49950,49950,49950,49947,49947]
print(maxWidthRamp(A))