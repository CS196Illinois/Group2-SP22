L = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0]
]

I = [
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0]
]

scores = 0

# try to read highest record from saved file,jump over this step if fail

board = [[0 for n in range(14)] for m in range(22)]
for i in range(14):
    for j in range(22):
        if i < 2 or j > 19 or i > 11:
            board[j][i] = 1
print(*board, sep = "\n")


def rot_ccw(piece):  # rotate couterclockwise
    rotpiece = [[0 for n in range(4)] for m in range(4)]
    for m in range(0, 4):
        for n in range(0, 4):
            rotpiece[m][n] = piece[n][3 - m]
    return rotpiece


def rot_cw(piece):  # rotate clockwise
    rotpiece = [[0 for n in range(4)] for m in range(4)]
    for m in range(0, 4):
        for n in range(0, 4):
            rotpiece[m][n] = piece[3 - n][m]
    return rotpiece


def add_to_board(board, piece, coords): 
    x,y = coords
    board_temp = [[0 for n in range(10)] for m in range(20)]
    for m in range(0, 20):
        for n in range(0, 10):
            board_temp[m][n] = board[m][n]
    for m in range(x, x+4):
        for n in range(y, y+4):
            board_temp[m][n] = board[m][n] + piece[m - x][n - y]
    return board_temp

def hit(board, piece, coords): 
    board_temp = add_to_board(board, piece, coords)
    for m in range(20):
        for n in range(10):
            if board_temp[m][n] > 1:
                return True
    return False


def lineClear():  # check if a horizontal line is fullfilled and delete it, and add scores. --Qi Chen
    pass



def move_right(board, piece, coords):
    x,y = coords
    if hit(board, piece, (x, y+1)) == False:
        return (x,y+1)
    else: 
        return (x, y)

def move_left(board, piece, coords):
    x,y = coords
    if hit(board, piece, (x, y-1)) == False:
        return (x,y-1)
    else: 
        return (x, y)

def push_down(board, piece, coords):
    x,y = coords
    for i in range(15):
        if hit(board, piece, (x + i,y)) == True:
            print(x + i, y)
            return (x+(i-1), y)


# save scores as a file if it's higher than the record


x, y = 0, 3
coords = (x, y)

test = adjust_coords(I, coords)
#print(*test, sep = "\n")
print(test)

while True:
    # generate initial pieces, use link list to generate 200 or so pieces initally -- Evan
    # default coordinates for where pieces drop--row 22 to 23 -- Evan
    # do default coordinates change based on piece? what is the default position for each piece? -- Evan

    # start dropping pieces -- Joseph
    # use second iteration of board that updates with moving pieces -- Joseph
    # falls, controlled w/ inputs-- Joseph
    # pushdown function -- anyone with extra time??
    # hit floor, get added to board -- devon
    # delay between blocks hitting & being added to permanent board (not being able to control piece anymore) -- devon
    # lines clear, added to score --Qi Chen
    # function that tests if/how many lines have been cleared--Qi Chen
    # gameover -- Qi Chen
    # have game over function by start dropping peices, checks if top lines has enough space for piece