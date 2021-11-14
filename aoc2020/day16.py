inp = open('day16inp.txt','r').read().split('\n')

print(inp)

endofranges = inp.index('')




ranges = []

for i in range(endofranges):
    parts = inp[i].split(': ')
    parts = parts[1]
    parts = parts.split(' or ')

    for part in parts:
        p = part.split('-')
        p[0],p[1] = int(p[0]),int(p[1])
        ranges.append(p)


startoflist = inp.index('nearby tickets:')


sum = 0
for i in range(startoflist + 1, len(inp)):
    nums = inp[i].split(',')

    for n in nums:
        valid = False
        for rangel in ranges:
            if not valid:
                if int(n) >= int(rangel[0]) and int(n) <= int(rangel[1]):
                    valid = True
        if not valid:
            inp[i] = 0
            break

newlist = []
ticketlist = inp[startoflist + 1: len(inp)]
a = len(ticketlist)
print(a)

for p in range(a):
    if ticketlist[p] != 0:
        newlist.append(ticketlist[p])

print(ranges)
print(newlist)
print(newlist[0])


nofields = int(len(ranges)/2)

sortedlist = [[] for i in range(len(newlist[0].split(',')))]


for f in newlist:
    f = f.split(',')
    for c in range(len(f)):
        sortedlist[c].append(f[c])




possible = [[] for i in range(nofields)]

for field in range(int(nofields)):
    rangetotest = ranges[field * 2 : field * 2 + 2]


    for set in range(len(sortedlist)):
        valid = True
        for value in sortedlist[set]:
            value = int(value)
            if value < rangetotest[0][0] or value > rangetotest[1][1] or (value > rangetotest[0][1] and value < rangetotest[1][0]):
                valid = False
                break
        if valid:
            possible[field].append(set)
print(possible)

collums = [[]for i in range(len(sortedlist))]

for row in range(len(possible)):
    for p in range(len(possible[row])):
        collums[p].append(row)
found = [collums[-1][0]]

for row in collums[::-1]:
    print(row)
    for f in found:
        try:
            row.remove(f)
        except:
            pass
    if len(row) > 0:
        found.append(row[0])
    #print(row)
sum = 1
ticketpos = inp.index('your ticket:') + 1
myticket = inp[ticketpos].split(',')
print(collums)
print(myticket)



print(sum)

print(ticketpos)

print(inp[ticketpos])


sum = 1



'''
for row in collums:
    print(row)
'''






