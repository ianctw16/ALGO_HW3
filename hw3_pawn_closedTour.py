import numpy as np
import tkinter as tk
import time

n = 0
m = 0


# main program
def main():
    time_start = time.time()
    global n
    global m
    # preprocess board's width and height
    if(m % 2 == 0 and n % 2 == 1):
        tmp = n
        n = m
        m = tmp

    # creat board
    board = np.zeros((n, m))

    i = 0
    j = 0
    control_j = 0
    colors = ['springgreen', 'deepskyblue']
    int_color = 0

    # main pawn's tour
    if(n % 2 == 0):
        # giving board the number in order.
        for point in range(1, n*m+1):
            board[i][j] = point
            # ui display
            lb = tk.Label(window,
                          text=int(board[i][j]),
                          height=2, width=5,
                          bg=colors[int_color])
            lb.grid(row=i, column=j)
            window.update()
            time.sleep(0.2)
            # color control
            if(int_color + 1 >= 2):
                int_color = 0
            else:
                int_color = int_color + 1

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
            # normal situation j = j + 1
            if(control_j == 0 and (i != n - 1) and (j != 0)):
                j = j + 1
                continue
            # another situation j = j - 1
            elif(control_j == 1 and (j != 0)):
                j = j - 1
                continue
            # when it goes last line in the board.
            if(i == n - 1 and (j == 1)):
                j = 0
                continue
            if(j == 0 and (i in range(1, n))):
                i = i - 1
                continue
    else:
        print("Pawn's closed tour does not exist [odd*odd] board's solution.")

    print(time.time()-time_start)
    print(board)
    window.update()
    window.mainloop()


#  get board size and ui display
def getSize():
    global n
    global m
    n = e1.get()
    m = e2.get()
    window.title(n + '*' + m + ' pawnClosedTour')
    n = int(n)
    m = int(m)
    lb1.destroy()
    lb2.destroy()
    e1.destroy()
    e2.destroy()
    bt1.destroy()
    main()


# ui widgets
window = tk.Tk()
window.configure(background='white')
# frame = tk.Frame(window)

# n = input("n*m board n: ")  # row
# m = input("n*m board m: ")  # col

lb1 = tk.Label(window, text="Board Width:", width=11, height=1, bg='gold')
lb2 = tk.Label(window, text="Board Height:", width=11, height=1, bg='gold')
lb1.grid(row=0)
lb2.grid(row=1)
e1 = tk.Entry(window)
e2 = tk.Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

bt1 = tk.Button(window, text="Submit", command=getSize, bg='lawngreen')
bt1.grid(row=3, column=3)

bt1.mainloop()

# window.geometry('600x400')
