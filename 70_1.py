def findPaths( m, n, N, s1, s2):
    """
    :type m: int
    :type n: int
    :type N: int
    :type i: int
    :type j: int
    :rtype: int
    """
    bias = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    cen= n-1

    dp =[[[0 for i in range(n)] for j in range(m)]for



