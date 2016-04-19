def main():
    a, b = [int(i) for i in input().split()]
    mat =[]
    for i in range(1,a+1):
        mat.append([int(i) for i in input()])

    def relax(i, j):
        nonlocal mat
        num = []
        try:
            num.append(mat[i][j])
            num.append(mat[i+1][j-1])
            num.append(mat[i+1][j+1])
            num.append(mat[i+2][j])
        except IndexError:
            return
        else:
            miNum = min(num)
            mat[i][j] -= miNum
            mat[i+1][j-1] -= miNum
            mat[i+1][j+1] -= miNum
            mat[i+2][j] -= miNum
            mat[i+1][j] += miNum

    for i in range(0, a):
        for j in range(0, b):
            relax(i, j)

    for i in range(0, a):
        for j in range(0, b):
            print(mat[i][j], end='')
        print('\n', end='')

main()
