n = input("n*m board n: ")  # row
m = input("n*m board m: ")  # col

n = int(n)
m = int(m)

board = [[0]*m]*n
print(board)


i = 0
j = 0
control_i = 0
control_j = 0

if(n % 2 == 0):
    for point in range(1, n*m):
        print(point)
        board[i][j] = point
        # when j reach end of row, change line and let j decrease.
        if(i == 0 and j == 0):
            j = j + 1
        if(j == m-1):
            i = i + 1
            control_j = 1
        # when i = 1, change line
        if(j == 1 and (i != 0)):
            i = i + 1
            control_j = 0
        if(control_j == 0 and (i != n - 1) and (j != 0)):
            j = j + 1
        elif(control_j == 1 and (j != 0)):
            j = j - 1
        if(i == n - 1 and (j == 1)):
            j = 0
        if(j == 0 and (i != n - 1)):
            i = i - 1
print(board)
