def validTicTacToe( board):
    """
    :type board: List[str]
    :rtype: bool
    """
    numx = 0
    numo = 0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='X':
                numx+=1
            elif board[i][j] == 'O':
                numo +=1
    if numx-numo>=2 or numo>numx:
        return False
    for i in range(3):
        if board[i][0]=='X' and board[i][1]=='X' and board[i][2]=='X':
            if numx==numo:
                return False
        elif board[0][i]=='X' and board[1][i]=='X' and board[2][i]=='X':
            if numx==numo:
                return False

    if board[0][0]=='X' and board[1][1]=='X' and board[2][2]=='X':
        if numx == numo:
            return False
    if board[0][2]=='X' and board[1][1]=='X' and board[2][0]=='X':
        if numx == numo:
            return False
    return True
