
import copy
inp = open('11in.txt','r').read().split('\n')

grid = []

for row in inp:
    grid.append(list(row))

print(grid)


'''

changed = True

while changed:
    changed = False
    gridcopy = copy.deepcopy(grid)
    for row in range(len(grid)):
        for collum in range(len(grid[row])):
            if grid[row][collum] == 'L':
                clear = True
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if row + dx >= 0 and row + dx < len(grid) and collum + dy >= 0 and collum + dy < len(grid[row]):
                            if grid[row + dx][collum + dy] == '#':
                                clear = False



                if clear:
                    gridcopy[row][collum] = '#'
                    changed = True

            if grid[row][collum] == '#':
                nextto = 0
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if row + dx >= 0 and row + dx < len(grid) and collum + dy >= 0 and collum + dy < len(grid[row]):
                            if dx == 0 and dy == 0:
                                pass
                            else:
                                if grid[row + dx][collum + dy] == '#':

                                    nextto += 1


                if nextto > 3:
                    gridcopy[row][collum] = 'L'
                    changed = True




    if grid == gridcopy:
        break
    grid = gridcopy


num = 0
for row in grid:
    for collum in row:
        if collum == '#':
            num += 1

print(num)

'''


#part 2

changed = True
while changed:
    gridcopy = copy.deepcopy(grid)
    changed = False
    for row in range(len(grid)):
        for collum in range(len(grid[row])):

            if grid[row][collum] == 'L':
                clear = True
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if row + dx >= 0 and row + dx < len(grid) and collum + dy >= 0 and collum + dy < len(grid[row]):
                            found = False
                            n= 1
                            while not found:
                                if row + n * dx >= 0 and row + n *  dx < len(grid) and collum + n *  dy >= 0 and collum + n * dy < len(grid[row]):
                                    if grid[row + n * dx][collum + n * dy] == '#':
                                        clear = False
                                        found = True
                                    elif grid[row + n * dx][collum + n * dy] == 'L':
                                        found = True
                                else:
                                    found = True


                                n += 1



                if clear:
                    gridcopy[row][collum] = '#'
                    changed = True

            if grid[row][collum] == '#':
                nextto = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        found = False
                        n = 1
                        while not found:
                            if row + n *dx >= 0 and row + n*dx < len(grid) and collum + n*dy >= 0 and collum + n*dy < len(grid[row]):
                                if dx == 0 and dy == 0:
                                    found = True
                                    pass
                                else:
                                    if grid[row + n * dx][collum + n*dy] == '#':
                                        nextto += 1
                                        found = True
                                    elif grid[row + n * dx][collum + n*dy] == 'L':
                                        found = True

                            else:
                                found  = True
                            n += 1


                if nextto > 4:
                    gridcopy[row][collum] = 'L'
                    changed = True

    if grid == gridcopy:
        break
    grid = gridcopy



num = 0
for row in grid:
    for collum in row:
        if collum == '#':
            num += 1

print(num)