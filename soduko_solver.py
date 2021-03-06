'''
Experimentation with backtracking algorithm,
and soduko solver.
'''

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def solve(brd):
    find = find_empty(brd)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(brd, i, (row, col)):
            brd[row][col] = i

            if solve(brd):
                return True

            brd[row][col] = 0
    return False



def valid(brd, num, pos):
    # check row
    for i in range (len(brd[0])):
        if brd[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(brd)):
        if brd[i][pos[1]] == num and pos[0] != i:
            return False

    #check for 3x3 cube
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if brd[i][j] == num and (i, j) != pos:
                return False
    return True


def find_empty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i,j)


    return None



def print_board(brd):

    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("-----------------")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end ="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end = "")


print_board(board)
solve(board)
print('\n')
print_board(board)