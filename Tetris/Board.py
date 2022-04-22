
from os import sep


class Board:
    level = 1

    def __init__(self):
        self.height = 20
        self.width = 10
        self.border = 2
        self.list2d = [[0 for n in range(self.width + self.border * 2)]   # use extends to replace it
                 for m in range(self.height + self.border)]
        for i in range(self.width + self.border * 2):
            for j in range(self.height + self.border):
                if i not in range(self.border, self.width + self.border) or j not in range(0, self.height):
                    self.list2d[j][i] = 1

    def add_to_board(self, piece, coords):
        x, y = coords
        for m in range(x, x+4):
            for n in range(y, y+4):
                # m, n are position of current slot in  board's coordinate; x, y are that in piece's coordinate
                self.list2d[m][n] += piece[m - x][n - y]

    def hit(self, piece, coords):
        self.add_to_board(piece, coords)  # create a temp to simulate
        for m in range(self.height + self.border):
            for n in range(self.width + self.border * 2):
                if self.list2d[m][n] % 2 != 0:
                    self.remove_from_board(piece, coords)
                    return True
        self.remove_from_board(piece, coords)
        return False

    def lineClear(self):  # check if a horizontal line is fullfilled and delete it, and add scores. --Qi Chen
        for i in self.board:
            lineFull = True
            for j in i:
                if j == 0:
                    lineFull = False
                    break
            if lineFull:
                scores += 1  # replace '1' by the specific marks.
                for m in range(self.board.index(i)):
                    self.list2d[m+1] = self.list2d[m]

    def remove_from_board(self, piece, coords):
        x, y = coords
        for m in range(x, x+4):
            for n in range(y, y+4):
                # m, n are position of current slot in  board's coordinate; x, y are that in piece's coordinate
                self.list2d[m][n] = self.list2d[m][n] - piece[m - x][n - y]
    
    def sprint(self):
        print(*self.list2d, sep = "\n")
