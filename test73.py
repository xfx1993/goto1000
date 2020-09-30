def shortestBridge( A):
    """
    :type A: List[List[int]]
    :rtype: int
    """
    bias = [[1,0],[-1,0],[0,1],[0,-1]]
    row = len(A)
    col = len(A[0])
    used =dict()
    lands = []
    for i in range(row):
        for j in range(col):
            if A[i][j]==1:
                nodes = [[i,j]]
                lands.append([i,j])
                A[i][j]=2
                while nodes:
                    curnodes = []
                    for x,y in nodes:
                        for x_,y_ in bias:
                            if 0<=x+x_<row and 0<=y+y_<col and A[x+x_][y+y_]==1:
                                lands.append((x+x_,y+y_))
                                A[x+x_][y+y_]=2
                                curnodes.append([x+x_,y+y_])
                    nodes = curnodes

                count = 0
                while lands:
                    curland = []
                    count += 1
                    for x, y in lands:
                        for x_, y_ in bias:
                            if 0 <= x + x_ < row and 0 <= y + y_ < col and A[x + x_][y + y_] != 2:
                                if A[x + x_][y + y_] == 1:
                                    return count-1
                                else:
                                    A[x + x_][y + y_] = 2
                                    curland.append([x + x_, y + y_])
                    lands = curland




A =[[0,1,0],[0,0,0],[0,0,1]]
print(shortestBridge(A))

