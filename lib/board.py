from moves import Move

class Board:
    rows = []
    size = 0

    hole_row = 0
    hole_col = 0

    moves = 0

    def __init__(self, raw_matrix):
        self.size = len(raw_matrix)
        for row_index in range(self.size):
            row = raw_matrix[row_index]
            for col_index in range(self.size):
                if row[col_index] == "*":
                    self.hole_row = row_index
                    self.hole_col = col_index
                else:
                    row[col_index] = int(row[col_index])

            self.rows.append(row)

    def execute_moves(self, moves):
        for move in moves:
            self.move(move)

        return len(moves)

    def move(self, move):
        if not self.can_move(move):
            raise Exception("Attempting illegal move")

        self.rows[self.hole_row][self.hole_col] = self.rows[move.row][move.col]
        self.rows[move.row][move.col] = "*"

        self.hole_row = move.row
        self.hole_col = move.col

    def can_move(self, move):
        if max(move.row, move.col) >= self.size or min(move.row, move.col) < 0:
            return False

        return abs(self.hole_row - move.row) + abs(self.hole_col - move.col) == 1

    def valid_moves(self):
        moves = [
            Move([self.hole_row, self.hole_col + 1]),
            Move([self.hole_row, self.hole_col - 1]),
            Move([self.hole_row + 1, self.hole_col]),
            Move([self.hole_row - 1, self.hole_col])
        ]

        return [move for move in moves if self.can_move(move)]

    def is_solved(self):
        last_seen = 0

        if self.rows[self.size - 1][self.size - 1] != "*":
            return False

        for row in self.rows:
            for col in row:
                if col != "*" and col < last_seen:
                    return False

        return True

    def write_to_file(self, filename):
        f = open(filename, "w")

        f.write(str(self.size) + "\n")
        for row in self.rows:
            f.write(' '.join(str(col) for col in row) + "\n")

        f.close()

def from_file(filename):
    f = open(filename, "r")
    size = int(f.readline())

    rows = []
    for row in range(size):
        rows.append(f.readline().split())

    return Board(rows)