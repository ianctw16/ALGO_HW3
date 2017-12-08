import numpy as np
import tkinter as tk

window = tk.Tk()
frame = tk.Frame(window)

n = input("n*m board n: ")  # row
m = input("n*m board m: ")  # col

window.title(n + '*' + m + 'pawnClosedTour')
n = int(n)
m = int(m)

# window.geometry('600x400')

if(m % 2 == 0 and n % 2 == 1):
    tmp = n
    n = m
    m = tmp

frame.pack(fill=tk.X, padx=n, pady=m)

board = np.zeros((n, m))
# print(board)


i = 0
j = 0
control_i = 0
control_j = 0

if(n % 2 == 0):
    for point in range(1, n*m+1):
        board[i][j] = point
        # when j reach end of row, change line and let j decrease.
        if(i == 0 and j == 0):
            j = j + 1
            continue
        if(j == m-1 and control_j == 0):
            i = i + 1
            control_j = 1
            continue
        # when i = 1, change line
        if(j == 1 and (i != n - 1) and (control_j == 1)):
            i = i + 1
            control_j = 0
            continue
        if(control_j == 0 and (i != n - 1) and (j != 0)):
            j = j + 1
            continue
        elif(control_j == 1 and (j != 0)):
            j = j - 1
            continue
        if(i == n - 1 and (j == 1)):
            j = 0
            continue
        if(j == 0 and (i in range(1, n))):
            i = i - 1
            continue
else:
    """
    ################# !! WRONG!!! It's open tour.. HAHA ##################
    """
    for point in range(1, n*m+1):
        print(i, j, point)
        board[i][j] = point
print(board)

for i in range(0, n):
    for j in range(0, m):
        if(i == 0 and j == 0):
            b = tk.Label(frame, text=int(board[i][j]), bg='orangered', width=5, height=2)
        if(j == 0 and i != 0):
            b = tk.Label(frame, text=int(board[i][j]), bg='springgreen', width=5, height=2)
        if(i % 2 == 0 and j != 0):
            b = tk.Label(frame, text=int(board[i][j]), bg='cyan', width=5, height=2)
        if(i % 2 == 1 and j != 0):
            b = tk.Label(frame, text=int(board[i][j]), bg='greenyellow', width=5, height=2)
        b.grid(row=i, column=j)

window.update()
window.mainloop()
