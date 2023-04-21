# 1
import numpy as np
ls = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def f(x):
    matrix = np.transpose(ls)
    return matrix

print(f(a))

# 2
ls = [('Тобик', 7, 'Имя', 'Фамилия'), ('Найк', 1, 'Нейм', 'Сернейм'), ('Камбоджа', 3, 'Нейм', 'Сернейм')]

def f(ans):
    dc = {} 
    for an in ans:
        a, b, c, d = an
        var = c, d
        if var not in dc:  
            dc[var] = []
        dc[var].append((a, b))

    return dc

print(f(ls))

# 3
def f(ls):
    dc = {}
    for i in ls:
        i = i.lower()
        if i not in dc:
            dc[i] = 1
        else:
            dc[i] += 1
    ls2 = sorted([(i, dc[i]) for i in dc], key=lambda x: (x[1], x[0]))
    return ls2[0][0]

print(f('ТЕСТ тест г г г в в а а б абама'.split()))

# 4
def f(ls):
    dc = {}
    for i in [j.lower() for j in ls if j.isalpha()]:
        if i not in dc:
            dc[i] = 1
        else:
            dc[i] += 1
    ls2 = sorted([(i, dc[i]) for i in dc], key=lambda x: (x[1], x[0]))
    return ls2[-1][0]

print(f('г - д - е - в - в - б - б - б - а - а а г г'))

# 5
def f(x):
    x = x.replace(' ', '')
    
    flag = True
    if len(x) > 1:
        if x[0].lower() == x[-1].lower(): 
            flag = f(x[1:-1])
        else:
            flag = False
    return flag

print(f('не зело полезен'))

# 6
def f(x):
    dc = {} 
    for i in x:
        if i not in dc:  
            dc[i] = 1
        else:
            dc[i] += 1

    return sorted(x, key=lambda y: (-dc[y], x.index(y)))


print(f([3, 7, 2, 7, 2, 3]))

# 7
def f(x):
    sl = x.split()
    for i in range(2, len(sl)):
        if all(j.isalpha() for j in sl[(i - 2):(i + 1)]):
            return True
    return False


print(f('ниче не могу придумать впишите сами пж'))

# 8
def f(x):
    x = x.lower()  
    maxs = 0  
    var = 1

    for i in range(1, len(x)): 
        if x[i] == x[i - 1] and x.isalpha():
            var += 1
        else:
            if var > maxs:
                maxs = var
            var = 1

    if var > maxs:
        maxs = var
    
    return maxs


print(f('aaaaaaabbcdddddddddddd'))

# 9
def f(x):
    yep = '0123456789.+-*/()'
    if not all (i in yep for i in x):
        raise ValueError('символ поменяй понял или нет че ты')
    result = eval(x)
    return result


print(f('2+2*2'))

# 10
def f(x):
    dc = {}
    for i in x:
        for a, b in i.items():
            if a not in dc:
                dc[a] = b
            else:
                dc[a] += b 
    return dc


ls = [{'var': 1, 'var1': 2, 'var3': 3},
             {'var': 4, 'var1': 5, 'var4': 6},
             {'var1': 7, 'var4': 8, 'var5': 9},
             {'var6': 10, 'var7': 11, 'var8': 12}]  

print(f(ls))

