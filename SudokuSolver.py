# A recursive sudoku solver
# import time for a timer
from time import time

# empty v easy for computer
# sudoku = [[0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0],
#           [0,0,1,0,0,0,0,0,0],
#           [0,0,0,0,0,0,2,0,0],
#           [0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0],
#           [0,0,0,0,0,0,0,0,0]]
# also very easy for computer
# sudoku = [[0,0,0,0,0,0,0,0,0],
#           [0,3,0,0,0,0,1,6,0],
#           [0,6,7,0,3,5,0,0,4],
#           [6,0,8,1,2,0,9,0,0],
#           [0,9,0,0,8,0,0,3,0],
#           [0,0,2,0,7,9,8,0,6],
#           [8,0,0,6,9,0,3,5,0],
#           [0,2,6,0,0,0,0,9,0],
#           [0,0,0,0,0,0,0,0,0]]
# slightly longer to computer
# sudoku = [[0,0,0,0,0,0,2,0,0],
#           [0,8,0,0,0,7,0,9,0],
#           [6,0,2,0,0,0,5,0,0],
#           [0,7,0,0,6,0,0,0,0],
#           [0,0,0,9,0,1,0,0,0],
#           [0,0,0,0,2,0,0,4,0],
#           [0,0,5,0,0,0,6,0,3],
#           [0,9,0,4,0,0,0,7,0],
#           [0,0,6,0,0,0,0,0,0]]
# difficult sudoku for humans
sudoku = [[2,0,5,0,0,0,2,0,0],
          [3,0,8,6,0,0,9,0,0],
          [0,0,0,1,0,0,4,0,0],
          [0,0,0,0,5,0,0,1,0],
          [0,0,0,0,9,0,0,2,0],
          [8,7,0,0,2,0,0,0,0],
          [0,0,0,0,8,9,0,0,3],
          [0,0,6,0,0,3,0,0,5],
          [5,0,4,0,0,0,0,0,1]]

# Function that determines whether a number can be added in said spot or no
def valid(num, pos):
    # Check row
    for i in range(len(sudoku[0])):
        if sudoku[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(sudoku)):
        if sudoku[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if sudoku[i][j] == num and (i,j) != pos:
                return False

    return True


# Recursive function which returns true if solution has been found
def solve():
    find = find_empty()
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(i, (row, col)):
            sudoku[row][col] = i

            if solve():
                return True

            sudoku[row][col] = 0

    return False


# This function finds the next empty cell and returns the position of it
def find_empty():
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i, j)  # row, col
    return None


# this function prints the board
def print_board():
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end="")
        print("")


if __name__ == "__main__":
    start_time = time()
    print_board()
    solve()
    print("== Final Board ==")
    print_board()
    end_time = time()
    final_time = end_time - start_time
    print("Time taken to solve was: " + str(final_time) + " seconds")


