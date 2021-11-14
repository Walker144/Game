inp = open('day14inp.txt','r').read().split('\n')


import copy


mask = ''

numdict = {}

def bintoden(string):
    r = 2 ** (len(string)-1)
    p = 0
    den = 0
    while r > 0.5:
        if string[p] == '1':
           den += r
        p += 1
        r = r /2

    return den
def dentobin(den):
    den  = int(den)
    r = 2**35
    num = ''
    while r > 0.5:
        if den >= r:
            num += '1'
            den = den - r
        else:
            num += '0'
        r =  r/2

    return num



for row in inp:
    row = row.split()
    if row[0] == 'mask':
        mask = row[2]
    else:
        pos = row[0][4:-1]
        value = row[2]
        premask = dentobin(int(pos))
        premask = list(premask)

        for p in range(36):

            if mask[p] == '1':
                premask[p] = '1'
            elif mask[p] == 'X':
                premask[p] = 'X'


        poslist = [premask]
        flattened = False
        while not flattened:
            flattened = True
            new = []
            for pos in poslist:
                l = list(pos)
                passed = True
                for p in range(len(l)):
                    if l[p] == 'X':
                        lcopy = copy.deepcopy(l)
                        lcopy[p] = '0'
                        new.append(copy.deepcopy(lcopy))
                        lcopy[p] = '1'
                        new.append(lcopy)
                        passed = False
                        flattened = False
                        break
                if passed:
                    new.append(''.join(l))

            poslist = new


        for p in poslist:

            numdict[bintoden(p)] = value










sum = 0
for item in numdict:
    sum += int(numdict[item])






print(sum)
