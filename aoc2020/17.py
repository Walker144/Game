eqs = open('day17.txt','r').read().split('\n')

print(eqs)

def partone(eqs):


    def evaluateex(string):

        depth = 0
        i = 0
        string = list(string)
        toremove = []
        for c in range(len(string)):
            if string[c] == ' ':
                toremove.append(c)

        for d in sorted(toremove)[::-1]:
            string.pop(d)
        start = 0




        toedit = []
        brackets = False
        i = 0


        while i < len(string):
            c = string[i]

            if c == '(' and depth == 0:
                brackets = True
                depth += 1
                start = i
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    newvalue = evaluateex(string[start + 1:i])
                    print(newvalue)
                    clearstring = range(i, start, -1)
                    for count in clearstring:
                        string.pop(count)
                    string[start] = newvalue
                    i = 0





            i += 1




        part = 0

        op = ''
        for s in string:
            if s in ['*', '+']:
                op = s
            else:
                if op == '':
                    print('p',part)
                    part = int(s)
                else:
                    part = eval(f'{s} {op} {part}')
        return part



    sum = 0
    for eq in eqs:
        sum += evaluateex(eq)

    print(sum)



def parttwo(eqs):


    def evaluateex(string):

        depth = 0
        i = 0
        string = list(string)
        toremove = []
        for c in range(len(string)):
            if string[c] == ' ':
                toremove.append(c)

        for d in sorted(toremove)[::-1]:
            string.pop(d)
        start = 0




        toedit = []
        brackets = False
        i = 0


        while i < len(string):
            c = string[i]

            if c == '(' and depth == 0:
                brackets = True
                depth += 1
                start = i
            elif c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    newvalue = evaluateex(string[start + 1:i])

                    clearstring = range(i, start, -1)
                    for count in clearstring:
                        string.pop(count)
                    string[start] = newvalue
                    i = 0





            i += 1




        part = 0

        op = ''
        return evaluatenobrackets(string)


    sum = 0
    for eq in eqs:
        sum += evaluateex(eq)

    print(sum)


def evaluatenobrackets(list):
    print(list)
    if len(list) == 3:
        print('simple')
        return eval(f'{list[0]} {list[1]} {list[2]}')
    if '+' in list:
        if '*' not in list:
            for item in range(len(list)):
                list[item] = str(list[item])
            return eval(' '.join(list))
    if '*' in list:
        if '+' not in list:
            for item in range(len(list)):
                list[item] = str(list[item])
            return eval(' '.join(list))
    if '*' in list and '+' in list:
        print('hellox')
        i = 0
        print(list)
        while i < len(list):

            if list[i] == '+':
                print(list[i-1:i+2])
                rep = evaluatenobrackets(list[i-1:i+2])
                list.pop(i + 1)
                list.pop(i)
                list[i-1] = rep
                i = 0
            else:
                i += 1
        for item in range(len(list)):
            list[item] = str(list[item])
        return eval(' '.join(list))





parttwo(eqs)