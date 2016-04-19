def queens(board, placed, target):

    if placed == target:
        print(board)
        return

    def place_q(i, j):
        nonlocal board
        for ind1 in range(0, n):
            if ~board[ind1][j]:
                board[ind1][j] = 1
        for ind2 in range(0, n):
            if ~board[i][ind2]:
                board[i][ind2] = 1
        for ind1 in range(0, n):
            ind2 = i+j-ind1
            if ind2 in range(0, n):
                if ~board[ind1][ind2]:
                    board[ind1][ind2] = 1
        for ind1 in range(0, n):
            ind2 = j-i+ind1
            if ind2 in range(0, n):
                if ~board[ind1][ind2]:
                    board[ind1][ind2] = 1
        board[i][j] = 2

    for i in range(0, n):
        for j in range(0, n):
            if ~board[i][j]:
                place_q(i, j)
                placed += 1
                queens(board,placed,target)


n = int(input())
board = [[0]*n]*n
queens(board, 0, n)
