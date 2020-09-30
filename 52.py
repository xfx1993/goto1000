def solveSudoku( board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    usenum = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def getnumlist(i, j, board):

        used = dict()
        for k in range(9):
            if board[k][j] != '.':
                if board[k][j] not in used:
                    used[board[k][j]] = 1
        for k in range(9):
            if board[i][k] != '.':
                if board[i][k] not in used:
                    used[board[i][k]] = 1
        start = 0
        end = 0
        if i // 3 == 0:
            start = 0
        elif i // 3 == 1:
            start = 1 * 3
        else:
            start = 2 * 3
        if j // 3 == 0:
            end = 0
        elif j // 3 == 1:
            end = 1 * 3
        else:
            end = 2 * 3
        for k in range(3):
            for l in range(3):
                if board[k + start][l + end] != '.':
                    if board[k + start][l + end] not in used:
                        used[board[k + start][l + end]] = 1
        res = []
        for i in range(9):
            if usenum[i] not in used:
                res.append(usenum[i])
        return res

    flag = [False]
    memo = dict()
    stack=[]
    def fillboard(board):
        if flag[0]:
            return
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    nums = getnumlist(i, j, board)
                    for num in nums:
                        board[i][j] = num
                        fillboard(board)
                        if not flag[0]:
                            board[i][j] = '.'
                        else:
                            break
                    return
        flag[0] = True

    fillboard(board)
    return board
board =[["5","3","4","6","7","8","9",".","."],["6","7","2","1","9","5",".",".","."],["1","9","8","3","4",".",".","6","."],["8","5","9","7","6",".",".",".","3"],["4","2","6","8","5","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],['3', '4', '5', '2', '8', '6', '1', '7', '9']]
print(solveSudoku(board))

