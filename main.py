from random import randint

grid = [["🟥","🟥","🟥","🟥"],
        ["⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","🟥"]]

order = ["🟥","🟧","🟨","🟩","🟦","🟪"]

def display_grid():
    for i in grid:
        print("".join(i))

def add_tiles():
    while True:
        row = randint(0,3)
        col = randint(0,3)
        if grid[row][col] == "⬜":
            if randint(1,100) < 90:
                grid[row][col] = "🟥"
            else:
                grid[row][col] = "🟧"
            break

def move(direction):
    if direction == "right":
        for k in range(2):
            for i in range(2, -1, -1):  # Iterate from the second-to-last column towards the first column
                for j in range(4):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j][i+1] == grid[j][i]:
                                grid[j][i+1] = order[order.index(grid[j][i+1]) + 1]
                                grid[j][i] = "⬜"
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

    elif direction == "left":
        for k in range(4):
            for i in range(1, 3):  # Iterate from the second-to-last column towards the first column
                for j in range(4):
                    if grid[j][i] == "⬜":
                        continue
                    else:
                        try:
                            if grid[j][i-1] == grid[j][i]:
                                grid[j][i-1] = order[order.index(grid[j][i-1]) + 1]
                                grid[j][i] = "⬜"
                        except IndexError:
                            continue
            for i in range(4):  # Iterate from the second-to-last column towards the first column
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
display_grid()
print("")
move("left")
display_grid()
