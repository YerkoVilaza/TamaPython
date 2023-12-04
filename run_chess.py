class Color:
    WHITE = 0
    BLACK = 1

class Board:

    FIELD_SIZE = 8
    
    def __init__(self) -> None:
        self.field = []
        self.current_color = Color.WHITE
        for i in range(self.FIELD_SIZE):
            self.field.append([None] * self.FIELD_SIZE)
        
        self.field[0] = [
            Rook(  0, 0, Color.WHITE, self), 
            Knight(0, 1, Color.WHITE, self),
            Bishop(0, 2, Color.WHITE, self),
            Queen( 0, 3, Color.WHITE, self),
            King(  0, 4, Color.WHITE, self),
            Bishop(0, 5, Color.WHITE, self), 
            Knight(0, 6, Color.WHITE, self), 
            Rook(  0, 7, Color.WHITE, self),
        ]

        self.field[1] = [
            Pawn(1, 0, Color.WHITE, self),
            Pawn(1, 1, Color.WHITE, self),
            Pawn(1, 2, Color.WHITE, self),
            Pawn(1, 3, Color.WHITE, self),
            Pawn(1, 4, Color.WHITE, self),
            Pawn(1, 5, Color.WHITE, self),
            Pawn(1, 6, Color.WHITE, self),
            Pawn(1, 7, Color.WHITE, self),
        ]

        self.field[6] = [
            Pawn(6, 0, Color.BLACK, self),
            Pawn(6, 1, Color.BLACK, self),
            Pawn(6, 2, Color.BLACK, self),
            Pawn(6, 3, Color.BLACK, self),
            Pawn(6, 4, Color.BLACK, self),
            Pawn(6, 5, Color.BLACK, self),
            Pawn(6, 6, Color.BLACK, self),
            Pawn(6, 7, Color.BLACK, self),
        ]
        
        self.field[7] = [
            Rook(  7, 0, Color.BLACK, self), 
            Knight(7, 1, Color.BLACK, self), 
            Bishop(7, 2, Color.BLACK, self),
            Queen( 7, 3, Color.BLACK, self),
            King(  7, 4, Color.BLACK, self),
            Bishop(7, 5, Color.BLACK, self), 
            Knight(7, 6, Color.BLACK, self), 
            Rook(  7, 7, Color.BLACK, self),
        ]
        
    def print(self):
        print('     +----+----+----+----+----+----+----+----+')
        for row in range(7, -1, -1):
            print(' ', row, end='  ')
            for col in range(8):
                print('|', self.cell(row, col), end=' ')
            print('|')
            print('     +----+----+----+----+----+----+----+----+')
        print(end='       ')
        for col in range(8):
            print(col, end='    ')
        print()

    def cell(self, row: int, col: int) -> str:
        piece = self.field[row][col]
        if piece:
            return piece.char() + ' '
        else:
            return '  '

    def can_move(self, row: int, col: int, row_new: int, col_new: int):
        if not (0 <= col < self.FIELD_SIZE and 0 <= row < self.FIELD_SIZE and 0 <= col_new < self.FIELD_SIZE and 0 <= row_new < self.FIELD_SIZE):
            return False
        if row == row_new and col == col_new:
            return False
        
        figure_from = self.field[row][col]
        figure_to = self.field[row_new][col_new]
        
        if figure_from is None:
            return False

        if figure_to:
            if figure_from.color == figure_to.color:
                return False

        if figure_from.color != self.current_color:
            return False

        return figure_from.can_move(row_new, col_new)
        
    def change_color(self):
        if self.current_color == Color.WHITE:
            self.current_color = Color.BLACK
        else:
            self.current_color = Color.WHITE
    
    def move(self, row, col, row_new, col_new):

        piece = self.field[row][col]
        self.field[row][col] = None
        self.field[row_new][col_new] = piece
        piece.row = row_new
        piece.col = col_new

class AbstractChessFigure:

    def __init__(self, row: int, col: int, color: int, board) -> None:
        self.row = row
        self.col = col
        self.color = color
        self.board = board

    def char(self):
        return None
    
    def can_move(self, row, col):
        return True

class Queen(AbstractChessFigure):
    
    def char(self):
        if self.color == Color.WHITE:
            return '♕'
        else:
            return '♛'

    def can_move(self, row, col):
        if abs(self.row - row) == abs(self.col - col):
            return True
        else:
            if self.row == row or self.col == col:
                return True
            else:
                return False

class King(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♔'
        else:
            return '♚'
        
    def can_move(self, row, col):
        dx = abs(self.col - col)
        dy = abs(self.row - row)
        if 0 <= dx <= 1 and 0 <= dy <= 1:
            return True
        else:
            return False

class Pawn(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♙'
        else:
            return '♟'
        
    def can_move(self, row, col):
        if self.col != col:
            return False

        if self.color == Color.WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if self.row + direction == row:
            return True

        if self.row == start_row and self.row + 2 * direction == row:
            return True
        
        return False

class Knight(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♘'
        else:
            return '♞'
        
    def can_move(self, row, col):
        dx = abs(self.col - col)
        dy = abs(self.row - row)
        if abs(dx*dy) == 2:
            return True
        else:
            return False
        
class Bishop(AbstractChessFigure):
    
    def char(self):
        if self.color == Color.WHITE:
            return '♗'
        else:
            return '♝'

    def can_move(self, row, col):
        if abs(self.row - row) == abs(self.col - col):
            return True
        else:
            return False
        
class Rook(AbstractChessFigure):

    def char(self):
        if self.color == Color.WHITE:
            return '♖'
        else:
            return '♜'
        
    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        
        step = 1 if (row >= self.row) else -1

        for r in range(self.row + step, row, step):
            if self.board.field[r][self.col]:
                return False

        step = 1 if (col >= self.col) else -1

        for c in range(self.col + step, col, step):
            if self.board.field[self.row][c]:
                return False

        return True

def jugarajedrez():
    board = Board()
    board.print()

    print()
    print('Juguemos Ajedrez parte blancos')
    print('Fila es vertical | Columna es horizontal')
    print('Mover una pieza: <Fila-1> <Col-1> <Fila-2> <Col-2>')
    print('Salir del juego: salir')

    while True:
        if board.current_color == Color.WHITE:
            print('Turno de las blancas')
        else:
            print('Turno de las negras')

        command = input('Ingrese las coordenadas: ')
        if command == 'salir':
            return
        
        command = command.split()
        col, row, col_new, row_new = map(int, command)
        
        if board.can_move(row, col, row_new, col_new):
            board.move(row, col, row_new, col_new)
            board.change_color()
            board.print()
