def olr(formel, letter):
    newFormel = []
    for x in formel:
        curletter = letter
        if len(letter) >= 2:
            curletter = letter[1:]
        else:
            curletter = "¬" + letter
        if curletter in x:
            list = []
            for y in x:
                if curletter != y:
                    list.append(y)
            newFormel.append(list)
        elif letter not in x:
            newFormel.append(x)
    return newFormel

def plr(formel, letter):
    newFormel = []
    for x in formel:
        if letter not in x:
            newFormel.append(x)
    return newFormel

def getvalue(string):
    if len(string) >= 2:
        return (ord(string[1:])*2 + 1)
    return ord(string)*2

def mergesort(list):
    if len(list) <= 1:
        return list
    size = len(list) / 2
    left = list[0:int(size)]
    right = list[int(size):len(list)]

    mergesort(left)
    mergesort(right)

    p1 = 0
    p2 = 0
    i = 0 #iterator for main list

    while p1 < len(left) and p2 < len(right):
        if getvalue(left[p1]) < getvalue(right[p2]):
            list[i] = left[p1]
            p1 += 1
        else:
            list[i] = right[p2]
            p2 += 1
        i+=1
    while p1 < len(left):
        list[i] = left[p1]
        p1+=1
        i+=1
    while p2 < len(right):
        list[i] = right[p2]
        p2+=1
        i+=1

def getletters(formel):
    list = []
    for x in formel:
        for y in x:
            if y not in list:
                list.append(y)
    return list

def isListSame(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True

def deleteDuplicates(formel):
    newFormel = []
    for x in formel:
        curList = []
        for y in x:
            if y not in curList:
                curList.append(y)
        newFormel.append(curList)

    newList = []
    for x in formel:
        mergesort(x)
    for i in range(len(newFormel)):
        b = True
        j = i+1
        while j < len(newFormel):
            if isListSame(newFormel[i],newFormel[j]):
                #print('same' + str(i) + str(j))
                b = False
                break
            j+=1
        if b:
            newList.append(newFormel[i])
    formel = newList
    return formel

def startDPLLAlgorithm(formel, abstand):
    formel = deleteDuplicates(formel)
    print(abstand + str(formel))
    if len(formel) == 0:
        return True
    for x in formel:
        if len(x) == 0:
            return False

    #OLR
    cur = []
    for x in formel:
        if len(x) == 1:
            cur.append(x[0])
    if len(cur) > 0:
        mergesort(cur)
        formel = olr(formel, cur[0])
        print(abstand + "OLR {" + cur[0] + "}")
        return startDPLLAlgorithm(formel, abstand)

    #PLR
    cur = []
    curletters = getletters(formel)
    for x in curletters:
        isthere = True
        for y in curletters:
            if len(x) >= 2:
                if x[1:] == y:
                    isthere = False
                    break
            else:
                if "¬"+x == y:
                    isthere = False
                    break
        if isthere:
            cur.append(x)

    if len(cur) > 0:
        mergesort(cur)
        formel = plr(formel, cur[0])
        print(abstand + "PLR {" + cur[0] + "}")
        return startDPLLAlgorithm(formel, abstand)

    #case
    curletters = getletters(formel)
    mergesort(curletters)
    curletter = curletters[0]
    formel1 = olr(formel, curletter)
    print(abstand + "case {" + curletter + "}")
    b = startDPLLAlgorithm(formel1, abstand + "    ")
    if b:
        return True

    if len(curletter) >= 2:
        curletter = curletter[1:]
    else:
        curletter = "¬"+curletter

    formel2 = olr(formel, curletter)
    print(abstand + "case {" + curletter + "}")
    return startDPLLAlgorithm(formel2, abstand + "    ")

def formelInMatrix(formel):
    formel = formel[1:len(formel)-1].replace(' ', '')
    matrix = []
    index = 0
    for i in range(len(formel)):
        if formel[i] == ',':
            if formel[i+1] == '{':
                matrix.append(formel[index+1:i])
                index = i
    matrix.append(formel[index+1:i+1])
    for i in range(len(matrix)):
        matrix[i] = matrix[i].replace('{', '').replace('}', '')
        matrix[i] = matrix[i].split(',')
    return matrix

#formel = "{{u}, {p, ¬y}, {y, ¬t, ¬u, ¬q}, {¬y, ¬q}, {y, p, ¬t, ¬u}, {y, q, ¬p}, {t}, {q, ¬t, ¬y, ¬u, ¬p}}"
#formel = "{{A, ¬B, ¬C}, {A, B, D}, {A, ¬C, ¬D}, {¬A, B}, {¬A, ¬B}}"
exits = ['exit','end','error','clear', '', ' ']
messageDE = "Bitte gib die Formel ein.\nNutze dafür geschweifte Klammern ('{','}') und das Negationszeichen ('¬').\nDenk auch dran um die ganze Formel noch einmal die geschweiften Klammern zu setzen, sonst erkennt das Programm nicht, dass es sich um eine Klauselmenge handelt.\nBeispiel: {{a, ¬b, d}, {¬a, ¬c}, {a, ¬c}, {¬a, b, ¬d}, {¬a, ¬d}}\nUm das Programm zu beenden schreib einfach 'exit' oder drücke die Entertaste.\n"
messageEN = "Please insert your formula.\nUse braces ('{','}') and the negationsymbol ('¬').\nDon't forget to but braces around the whole formula, otherwise the programm won't detect that it is a set of clauses.\nExample: {{a, ¬b, d}, {¬a, ¬c}, {a, ¬c}, {¬a, b, ¬d}, {¬a, ¬d}}\nTo end the program, just type 'end' or click the enter key.\n"
formel = input(messageEN)

if formel in exits:
    exit()
print("\n")

matrix = formelInMatrix(formel)
print(matrix)
for x in matrix:
    mergesort(x)
print("SORT")
done = startDPLLAlgorithm(matrix, "")
print(str(done) + "\n")
