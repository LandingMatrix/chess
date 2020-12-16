import pieces

BLACK = 0
WHITE = 1

class Board():
    def __init__(self):
        self.board = ['.'*8 for i in range(8)]
        self.pieces = []
        self.side = WHITE #white side

    def set_pieces(self):

        black = []
        black.append(pieces.Rook(0,0,BLACK))
        black.append(pieces.Rook(0,7,BLACK))
        black.append(pieces.Knight(0,1,BLACK))
        black.append(pieces.Knight(0,6,BLACK))
        black.append(pieces.Bishop(0,2,BLACK))
        black.append(pieces.Bishop(0,5,BLACK))
        black.append(pieces.Queen(0,3,BLACK))
        black.append(pieces.King(0,4,BLACK))
        for x in range(8):
            black.append(pieces.Pawn(1,x,BLACK))

        white = []
        white.append(pieces.Rook(7,0,WHITE))
        white.append(pieces.Rook(7,7,WHITE))
        white.append(pieces.Knight(7,1,WHITE))
        white.append(pieces.Knight(7,6,WHITE))
        white.append(pieces.Bishop(7,2,WHITE))
        white.append(pieces.Bishop(7,5,WHITE))
        white.append(pieces.Queen(7,3,WHITE))
        white.append(pieces.King(7,4,WHITE))
        for x in range(8):
            white.append(pieces.Pawn(6,x,WHITE))

        self.pieces = black + white

    def update_board(self):
        for piece in self.pieces:
            self.insert(piece.y, piece.x, piece.symbol)

    def flip(self):
        reverse_board = self.board[::-1]
        self.board = [row[::-1] for row in reverse_board]
        self.side *= -1

    def insert(self, y, x, c):
        row = self.board[y]
        self.board[y] = row[:x] + c + row[x+1:]

    def print_board(self):
        rows = [8, 7, 6, 5, 4, 3, 2, 1][::self.side]
        columns = 'abcdefgh'
        for i in range(8):
            print(rows[i], end=' ')
            print(' '.join(self.board[i]))
        print(end='  ')
        print(' '.join(columns[::self.side]))

def convert_coords(coordinates):
    '''
    in form of e5
    from chess notation 1-8, a-h
    from whites pov
    '''
    columns = ['a','b','c','d','e','f','g','h']

    if len(coordinates) != 2:
        raise ValueError("invalid coordinates")
    col = coordinates[0]
    row = coordinates[1]

    y = int(row) - 1
    x = columns.index(col)
