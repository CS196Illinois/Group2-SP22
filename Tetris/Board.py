
class Board:
    level = 1

    def __init__(self):
        height = 20
        width = 10
        border = 2
        board = [[0 for n in range(width + border * 2)]   # use extends to replace it
                 for m in range(height + border)]
        for i in range(width + border * 2):
            for j in range(height + border):
                if i not in range(border, width + border) or j not in range(0, height):
                    board[j][i] = 1

    def add_to_board(self, piece, coords):
        x, y = coords
        for m in range(x, x+4):
            for n in range(y, y+4):
                # m, n are position of current slot in  board's coordinate; x, y are that in piece's coordinate
                self[m][n] = self[m][n] + piece[m - x][n - y]

    def hit(self, piece, coords):
        board_temp = self.add_to_board(
            self.copy(), piece, coords)  # create a temp to simulate
        for m in range(self.height + self.border):
            for n in range(self.width + self.border * 2):
                if board_temp[m][n] % 2 != 0:
                    return True
        return False

    def lineClear(self):  # check if a horizontal line is fullfilled and delete it, and add scores. --Qi Chen
        for i in self:
            lineFull = True
            for j in i:
                if j == 0:
                    lineFull = False
                    break
            if lineFull:
                scores += 1  # replace '1' by the specific marks.
                for m in range(self.board.index(i)):
                    self.board[m+1] = self.board[m]

    def remove_from_board(self, board, piece, coords):
        x, y = coords
        for m in range(x, x+4):
            for n in range(y, y+4):
                # m, n are position of current slot in  board's coordinate; x, y are that in piece's coordinate
                self[m][n] = self[m][n] - piece[m - x][n - y]
