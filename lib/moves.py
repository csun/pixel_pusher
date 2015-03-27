class Move:
    row = 0
    col = 0

    def __init__(self, raw_array):
        self.row = int(raw_array[0])
        self.col = int(raw_array[1])

def list_from_file(filename):
    f = open(filename, "r")

    moves = []
    num_moves = int(f.readline())
    for move in range(num_moves):
        moves.append(Move(f.readline().split()))

    return moves