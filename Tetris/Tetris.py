# from dataclasses import dataclass
import queue
# from typing_extensions import Self
import random
import pygame

class Piece():
    def __init__(self, n_grid, n_color):
        self.n_grid = n_grid
        self.n_color = n_color

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
                return (x+(i-1), y)

queue = []
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

def gameStart():
    y = random.randint(0, 6)
    all_pieces = [t_piece, i_piece, z_piece, s_piece, j_piece, o_piece, l_piece]
    queue.append(all_pieces[y])

scores = 0

    # try to read highest record from saved file,jump over this step if fail

class Board:
    level = 1

    gameStart = False
    
    def __init__(self):
        board = [[0 for n in range(14)] for m in range(24)]
        for i in range(14):
            for j in range(24):
                if i < 2 or j > 19 or i > 11:
                    board[j][i] = 5
        print(*board, sep="\n")

    def add_to_board(self, board, piece, coords):
        x, y = coords
        board_temp = [[0 for n in range(14)] for m in range(22)]
        for m in range(0, 20):
            for n in range(2, 12):
                board_temp[m][n] = board[m][n]
        for m in range(x, x+4):
            for n in range(y, y+4):
                board_temp[m][n] = board[m][n] + piece[m - x][n - y]
        return board_temp

    def hit(self, board, piece, coords):
        board_temp = self.add_to_board(board.copy(), piece, coords)
        for m in range(22):
            for n in range(14):
                if board_temp[m][n] == 2 or board_temp[m][n] == 6:
                    return True
        return False

    def lineClear(self):  # check if a horizontal line is fullfilled and delete it, and add scores. --Qi Chen
        for i in self.board:
            if i == [1 for n in range(16)]:
                scores += 1  # replace '1' by the specific marks.
                for m in range(1, self.board.index(i)):
                    self.board[m] = self.board[m-1]

# save scores as a file if it's higher than the record

count = 0
fps = 25
gameOn = True


#Game Loop
while gameOn:
    #adds pieces to queue 
    #Moving Pieces Down, can add level system very easy
    if (count % (fps // Board.level) == 0):
        if board.gameStart: 
            piece.push_down
    count += 1

    #Inputs will be controlled using some sofware, I assume pygame
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Piece.rot_cw
            if event.key == pygame.K_DOWN:
                Piece.push_down
            if event.key == pygame.K_LEFT:
                Piece.move_left
            if event.key == pygame.K_RIGHT:
                Piece.move_right
            if event.key == pygame.K_SPACE:
                gameOn = False
            if event.key == pygame.K_ESCAPE: 
                piece_queue = 0 # piece that is pulled from queue, increases when piece is placed later
                for i in range (200): #appends 200 pieces to queue when escape is hit(initialized)
                    gameStart()
    
    Placed = False
    #when a piece is added to board, make true
    while Placed:
        piece_queue += 1
        Board.add_to_board(Board, queue[piece_queue], (0, 12))

    


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
