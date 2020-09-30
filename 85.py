def fraction(cont):
    """
    :type cont: List[int]
    :rtype: List[int]
    """
    size = len(cont)

    def helper(a, b):
        while a % b != 0:
            temp = a % b
            a = b
            b = temp
        return b

    def dfs(index):
        if index >= size:
            return [-1, -1]

        a = cont[index]

        cur = dfs(index + 1)
        if cur == [-1, -1]:
            return [ a, 1]

        m = cur[0]##分子
        n = cur[1]##分母

        fenzi = m*a+n
        fenmu = m
        b = helper(fenzi, fenmu)

        return [(m*a+n) // b,  m // b]

    return dfs(0)


cont = [3, 2, 0, 2]
print(fraction(cont))