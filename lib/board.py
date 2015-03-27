class Board:
    rows = []
    size = 0

    hole_row = 0
    hole_col = 0

    moves = 0

    def __init__(self, raw_matrix):
        self.size = len(raw_matrix)
        for row in raw_matrix:
            for col in self.size:
                if row[col] == "*":
                    self.hole_row = row
                    self.hole_col = col
                else:
                    row[col] = int(row[col])

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
        return abs(self.hole_row - move.row) + abs(self.hole_col - move.col) == 1

    def is_solved(self):
        last_seen = 0

        if self.rows[self.size - 1][self.size - 1] != "*":
            return False

        for row in self.rows:
            for col in row:
                if col != "*" and col < last_seen:
                    return False

        return True

def from_file(filename):
    f = open(filename, "r")
    size = f.readline()

    rows = []
    for row in range(size):
        rows.append(f.readline.split())

    return Board(rows)