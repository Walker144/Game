
inp = open('day20inp.txt','r').read().split('\n')


matrixes = []

class dmatrix():
    def __init__(self,firstrow,grid):
        self.firstrow = firstrow
        self.grid = grid

    def __repr__(self):
        return f'{self.firstrow}, {self.grid}'



i = 0

for row in inp:
    if 'Tile' in row:
        start = i
    elif row == '':
        end = i
        matrixes.append(dmatrix(inp[start].split()[1][0:-1],inp[start+1: end]))


    i += 1





def rotate(matrix):
    new = [[] for i in range(len(matrix))]
    for row in matrix:
        i = 0
        for p in row:
            new[i].append(p)
            i += 1
    d = []
    for row in new:
        d.append(row[::-1])

    return dl9o



print(matrixes[0].grid, 'ge\n',rotate(matrixes[0].grid))

