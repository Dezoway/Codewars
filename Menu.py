import pprint
def selection(fighters, initial_position, moves):
    solution=list()
    x,y =initial_position
    for move in moves:
        if move == 'up':
            x = 1
        elif move == 'down':
            x = 0
        elif move == 'right':
            y = (y + 1) % len(fighters[0])
        elif move == 'left':
            y = (y - 1) % len(fighters[0])
        solution.append(fighters[x][y])
    return solution



fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]]
moves = ['left'] * 8
print(selection(fighters, (0, 0), moves))
