
start  = [0,1,4,13,15,12,16]
dict = {}


for num in range(len(start)-1):
    dict[start[num]] = num +1

print(dict)


lastn = start[-1]
print(lastn)
for i in range(7,30000000):

    try:
        lastt = dict[lastn]
    except:
        #print(lastn, 'has not been spoken before')
        lastt = i
    #print(i,i - lastt)
    #print(dict)
    if i % 1000== 0:
        print(i)

    dict[lastn] = i
    lastn = i - lastt
    #print('speak',lastn)

print(lastn)

