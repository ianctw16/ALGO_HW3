import numpy as np

n = input("n*m board n: ")
m = input("n*m board m: ")

n = int(n)
m = int(m)

i = 0
j = 0
control_i = 0
control_j = 0

board = np.zeros((n, m))

for point in range(1, n*m+1):
    board[i][j] = point
    if(i == 0 and j == 0):
        j = j + 1
        continue
    if(j == m-1 and control_j == 0):
        i = i + 1
        control_j = 1
        continue
    if(j == 0 and control_j == 1):
        i = i + 1
        control_j = 0
        continue
    if(control_j == 1):
        j = j - 1
        continue
    if(control_j == 0):
        j = j + 1
        continue
print(board)
