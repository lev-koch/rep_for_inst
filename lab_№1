#1
def f(ls):
    return ls[0], ls[2], ls[-2]

print(*f([1, 2, 3, 4, 5]))

# 2
def f(ls, n):
    try:
        return ls[n] ** n
    except:
        return -1

print(f([0], 0))

# 3
def f(string, let):
    return len(string[:string.find(let)]) + string[string.find(let) + 1:].find(let) + 1


print(f('сербанкб', "б"))

# 4
def f(num):
    num = str(num)[::-1]
    return len(num[:num.index('1')])

print(f(101100110100))

# 5
def f(string):
    return string[::-1]


print(f('string'))


# 6
def f(x):
    if len(x) == 0:
        return 'массив пустой'
    if x.count(x[0]) == len(x):
        return 'массив состоит из одного и того же элемента'
    return 'массив содержит различные значения'


print(f([1,2,4]))

# 7
def f(password):
    low = 'abcdefghijklmnopqrstuvwxyz' 
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    flag1 = [1 for i in password if i in low]
    flag2 = [1 for i in password if i in up]
    num = sum(i.isdigit() for i in password)


    if sum(flag1) >= 1 and sum(flag2) >= 1 and num >= 1 and \
    (len(password) - sum(flag1) - sum(flag2) - num == 0) and len(password) >= 16:
        return 'пароль подходит'

    return 'пароль не подходит'



print(f('11111111W111111111111q111111111111'))

# 8
def f(ls):
    ls = ls[:]
    i = 0
    while True:
        try:
            while isinstance(ls[i], list):
                item = ls.pop(i)
                for inner_item in reversed(item):
                    ls.insert(i, inner_item)
            i += 1
        except IndexError:
            break
    return ls

print(f([[1, 2, [1, 2, 3, [(1, 3, 4)]], [[[[[[[[[[[[1, [[1, [23, 4, ['string', [1]]]]]]]]]]]]]]]]]]]))

# 9
def f(dc):
    val = list(dc.values())
    key = list(dc.keys())
    return key[val.index(max(val))]


print(f({'first': 3.1, 'second': 3.2, 'third': 3.3}))

# 10
def f(x):
    ls = []
    for i in x:
        if x.count(i) > 1:
            ls.append(i)

    return ls


print(f([1,2,3,1,3])) # тут подается список
