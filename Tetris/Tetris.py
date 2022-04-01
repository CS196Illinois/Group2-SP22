from dataclasses import dataclass
from queue import queue
from typing_extensions import Self
from random import random


class Piece ():
    def __init__(self, n_grid, n_color):
        self.n_grid = n_grid
        self.n_color = n_color
    # include rotate functions, etc

def startGame():
    queue = queue()
    y = 7 * random()
    i_piece = Piece([
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0]]
    , "blue")
    t_piece = Piece([
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ], "yellow")
    z_piece = Piece([
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], "red")
    s_piece = Piece([
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], "orange")
    j_piece = Piece([
        [0, 1, 0, 0],
        [0, 1, 0, 0], 
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ], "green")
    o_piece = Piece([
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ], "purple")
    l_piece = Piece([
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ], "pink")
    all_pieces = [t_piece, i_piece, z_piece, s_piece, j_piece, o_piece, l_piece]
    queue.append(all_pieces[y])

scores = 0

# try to read highest record from saved file,jump over this step if fail


class Board:

    level = 1

    gameStart = false
    
    def __init__(self):
        board = [[0 for n in range(14)] for m in range(22)]
        for i in range(14):
            for j in range(22):
                if i < 2 or j > 19 or i > 11:
                    board[j][i] = 1
        print(*board, sep="\n")

    def add_to_board(self, board, piece, coords):
        x, y = coords
        board_temp = [[0 for n in range(10)] for m in range(20)]
        for m in range(0, 20):
            for n in range(0, 10):
                board_temp[m][n] = board[m][n]
        for m in range(x, x+4):
            for n in range(y, y+4):
                board_temp[m][n] = board[m][n] + piece[m - x][n - y]
        return board_temp

    def hit(self, board, piece, coords):
        board_temp = self.add_to_board(board, piece, coords)
        for m in range(20):
            for n in range(10):
                if board_temp[m][n] > 1:
                    return True
        return False

    def lineClear(self):  # check if a horizontal line is fullfilled and delete it, and add scores. --Qi Chen
        for i in self.board:
            if i == [1 for n in range(14)]:
                scores += 1  # replace '1' by the specific marks.
                for m in range(1, self.board.index(i)):
                    self.board[m] = self.board[m-1]


class Piece:
    def __init__(self, setShape) -> None:
        self.shape = setShape

    def rot_ccw(self, piece):  # rotate couterclockwise
        rotpiece = [[0 for n in range(4)] for m in range(4)]
        for m in range(0, 4):
            for n in range(0, 4):
                rotpiece[m][n] = piece[n][3 - m]
        return rotpiece

    def rot_cw(self, piece):  # rotate clockwise
        rotpiece = [[0 for n in range(4)] for m in range(4)]
        for m in range(0, 4):
            for n in range(0, 4):
                rotpiece[m][n] = piece[3 - n][m]
        return rotpiece

    def move_right(self, board, piece, coords):
        x, y = coords
        if Board.hit(board, piece, (x, y+1)) == False:
            return (x, y+1)
        else:
            return (x, y)

    def move_left(self, board, piece, coords):
        x, y = coords
        if Board.hit(board, piece, (x, y-1)) == False:
            return (x, y-1)
        else:
            return (x, y)

    def push_down(self, board, piece, coords):
        x, y = coords
        for i in range(15):
            if Board.hit(board, piece, (x + i, y)) == True:
                print(x + i, y)
                return (x+(i-1), y)


# save scores as a file if it's higher than the record


x, y = 0, 3
coords = (x, y)

test = adjust_coords(I, coords)
#print(*test, sep = "\n")
print(test)

counter = 0
fps = 25

#Game Loop
while True:
    #Moving Pieces Down, can add level system very easy
    if (counter % (fps // board.level) == 0) {
        if board.gameStart {
            piece.push_down
        }
    }
    count++

    #Inputs will be controlled using some sofware, I assume pygame
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                piece.rot_cw
            if event.key == pygame.K_DOWN:
                piece.push_down
            if event.key == pygame.K_LEFT:
                piece.move_left
            if event.key == pygame.K_RIGHT:
                piece.move_right

                
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
