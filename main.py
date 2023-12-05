from random import randint

grid = [["⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜"]]
point = 0


order = ["🎄", "🎅", "🤶", "⛄", "🎁", "🔔", "🎉", "🌟", "❅", "🕯️", "🍪", "🥛"]
points_order = [2] + [2**i for i in range(1, 12)]

def display_grid():
    for i in grid:
        print("".join(i))

def add_tiles():
    while True:
        row = randint(0,3)
        col = randint(0,3)
        if grid[row][col] == "⬜":
            if randint(1,100) < 90:
                grid[row][col] = "🎄"
            else:
                grid[row][col] = "🎅"
            break

def move(direction, points):
    if direction == "right":
        for k in range(4):
            for i in range(2, -1, -1):  # Iterate from the second-to-last column towards the first column
                for j in range(4):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j][i+1] == grid[j][i]:
                                grid[j][i+1] = order[order.index(grid[j][i+1]) + 1]
                                grid[j][i] = "⬜"
                                points += points_order[order.index(grid[j][i+1]) + 1]
                        except IndexError:
                            continue
            for i in range(4):  # Iterate from the second-to-last column towards the first column
                for j in range(4):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j][i+1] == "⬜":
                                grid[j][i+1] = grid[j][i]
                                grid[j][i] = "⬜"
                        except IndexError:
                            continue
    if direction == "left":
        for k in range(4):
            for i in range(1, 4):
                for j in range(4):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j][i-1] == grid[j][i]:
                                grid[j][i-1] = order[order.index(grid[j][i-1]) + 1]
                                grid[j][i] = "⬜"
                                points += points_order[order.index(grid[j][i-1]) + 1]
                        except IndexError:
                            continue
            for i in range(3,0,-1):
                for j in range(4):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j][i-1] == "⬜":
                                grid[j][i-1] = grid[j][i]
                                grid[j][i] = "⬜"
                        except IndexError:
                            continue
    if direction == "up":
        for k in range(4):
            for i in range(4):
                for j in range(1,4):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j-1][i] == grid[j][i]:
                                grid[j-1][i] = order[order.index(grid[j-1][i]) + 1]
                                grid[j][i] = "⬜"
                                points += points_order[order.index(grid[j-1][i]) + 1]
                        except IndexError:
                            continue
            for i in range(4):  # Iterate from the second-to-last column towards the first column
                for j in range(3,0,-1):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j-1][i] == "⬜":
                                grid[j-1][i] = grid[j][i]
                                grid[j][i] = "⬜"
                        except IndexError:
                            continue
    if direction == "down":
        for k in range(4):
            for i in range(4):
                for j in range(2, -1, -1):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j+1][i] == grid[j][i]:
                                grid[j+1][i] = order[order.index(grid[j+1][i]) + 1]
                                grid[j][i] = "⬜"
                                points += points_order[order.index(grid[j+1][i]) + 1]
                        except IndexError:
                            continue
            for i in range(4):  # Iterate from the second-to-last column towards the first column
                for j in range(4):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j+1][i] == "⬜":
                                grid[j+1][i] = grid[j][i]
                                grid[j][i] = "⬜"
                        except IndexError:
                            continue
    return points                        

def game_loop():
    point = 0
    valid_directions = ["right", "left", "up", "down"]
    add_tiles()
    display_grid()
    while True:
        dir = input("direction: ")
        if dir in valid_directions:
            point = move(dir, point)
            add_tiles()
            print(f'points: {point}')
            display_grid()
        else:
            print("invalid input")

game_loop()
