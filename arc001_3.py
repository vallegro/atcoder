def place_queens(queens, n, init):

    def check_q(queens, n):
        board = [[0 for i in range(0, n)] for j in range(0, n)]
        for ind_q in range(0, queens.__len__()):
            i = queens[ind_q][0]
            j = queens[ind_q][1]
            for ind1 in range(0, n):
                if board[ind1][j] == 0:
                    board[ind1][j] = 1
            for ind2 in range(0, n):
                if board[i][ind2] == 0:
                    board[i][ind2] = 1
            for ind1 in range(0, n):
                ind2 = i+j-ind1
                if ind2 in range(0, n):
                    if board[ind1][ind2] == 0:
                        board[ind1][ind2] = 1
            for ind1 in range(0, n):
                ind2 = j-i+ind1
                if ind2 in range(0, n):
                    if board[ind1][ind2] == 0:
                        board[ind1][ind2] = 1
            board[i][j] = 2
        return board

    def print_res(queens, n):
        global total
        total += 1
        board = [['.' for i in range(0, n)] for j in range(0, n)]
        for i in range(0, n):
            board[queens[i][0]][queens[i][1]] = 'Q'
        for i in range(0, n):
            for j in range(0, n):
                print(board[i][j], end='')
            print('\n', end='')
        return

    if queens.__len__() == n:
        print_res(queens, n)
        del queens[-1]
        return

    pos = check_q(queens, n)
    i = queens.__len__()
    for j in range(0, n):
        if total >= 1:
            return
        if pos[i][j] == 0:
            queens.append([i, j])
            place_queens(queens, n, init)
        else:
            continue
    if queens.__len__() == init:
        return
    else:
        del queens[-1]
        return

board = []
queens = []
init = 0
total = 0
for i in range(0, 8):
    board.append(input())
for i in range(0, 8):
    for j in range(0, 8):
        if board[i][j] == 'Q':
            queens.append([i, j])
            init += 1
place_queens(queens, 8, init)
