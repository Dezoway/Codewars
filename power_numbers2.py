queenpos = [x, x]
directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
for dir in directions:
    for m in [-1, 1]:
        d = dir * m
        for i in range(8):
            row = queenpos[0] + d[0]
            col = queenpos[1] + d[1]
            if row < 8 and row > -1 and col < 8 and col > -1:
            obs = board.getpiece(row, col)
            if obs is not None: break
            print(row, col)