import pyautogui as pg
import numpy as np
import time 

grid = [] ##create a new empty grid
while True:
    row = list(input('Row: ')) ##convert a sequence row of numbers to a list as strings
    ints = [] ##create an empty list

    for n in row:
        ints.append(int(n)) ##convert each value to string and add it to list of ints
    grid.append(ints) 

    if len(grid) == 9: ##once we have 9 rows(9 sublist) we break
        break
    print("Row " + str(len(grid)) + " Complete")

time.sleep(3) 

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('---------------------------')
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
 
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j) #row, col y,x
    return None ##if there are no open spaces return none

def valid_spot(board,value,position):
    ## check the row
    for i in range(len(board[0])): ##i = 0,1,2,3,4,5,6,7,8
        if board[position[0]][i] == value and position[1] != i:
            return False


    ##check the column
    for i in range(len(board[0])):
        if board[i][position[1]] == value and position[0] != i:
            return False

    ##check the 3x3
    x_box = position[1] // 3 
    y_box = position[0] // 3 

    for i in range(y_box*3, y_box*3 + 3): ##loop through 3x3
        for j in range(x_box*3, x_box*3 + 3): ##loop through 3x3
            if board[i][j] == value and (i, j) != position: #if any value in our 3x3 is = to the value we just added return false
                return False
    return True ##if we get through each chck our spot is valid

def print(matrix):
    final = [] ##basically our grid
    str_fin = []
    for i in range(9):
        final.append(matrix[i]) ##add each row to final(as a string)

    for lists in final: ##go into each row in final
        for number in lists: ## go into each element in each row
            str_fin.append(str(number)) ##convert element to string and add to final ls

    counter = []
    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)

        if len(counter) % 9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            


def solve_board(board):
    find = find_empty(board)
    if not find:
        return True ##if we find the solutio to the board return true
    else: 
        row, col = find
    for i in range(1,10): ##i = 1-9
        if valid_spot(board,i, (row, col)):
            board[row][col] = i ##if the spot is valid at the value we will plug it into the board

            if solve_board(board): ## call the solve board func again(recursivley) with out new value plugged in and try again
                return True
            
            board[row][col] = 0 ##if solve board is false reset out current position bacl to 0 and retry with a new value

        return False
    print(np.matrix(grid))

solve_board(grid)







""" print_board(grid)
solve_board(grid)
print("#######################################################")
print_board(grid) """
