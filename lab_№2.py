# 1
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(int(input())))

# 2
def delete(ls1, ls2):
    res1, res2 = [], []

    for i in ls1:
        if i not in ls2:
            res1.append(i)
    for i in ls2:
        if i not in ls1:
            res2.append(i)

    return res1, res2


print(*delete([1,2,3,4,5,6], [4,5,6,7,8,9]))

# 3
def f(ls, n):
    res = []
    for i in ls:
        if ls.count(i) >= n:
            res.append(i)

    return list(set(res))

print(*f([1,2,3,3,3,3,3], 4))

# 4
def f(a, rec):

    ls = []
    var = 0

    for i in a:
        if type(i) is list:
            i = f(i, rec + 1)
        if rec == 1:
            ls.append(i)
        else:
            var += i


    if rec == 1:
        return ls
    return var


print(f([1, [2, [3, 4]]], 1))

# 5
def f(ls):
    a, b, c, d = 0, 1, 0, 0
    for i in range(len(ls)):
        if len(ls) == 1:
            d, c = 1, 0
            break
        if i == 0:
            i += 1
        if ls[i - 1] < ls[i]:
            b += 1
        else:
            if d - c < b - a:
                d, c = b, a
            a, b = i, i + 1

    if d - c < b - a:
        d, c = b, a

    return ls[c:d]


print(f([1, 2, 3, 2, 4, 5, 6, 7]))

# 6
def f(string):
    res = ''
    flag = True
    for i in string:
        if i.isalpha():
            if flag:
                res += i.upper()
            else:
                res += i.lower()
            if flag:
                flag = False
            else:
                flag = True
        else:
            res += i


    return res


print(f('чмаф всех в чатике'))

# 7
def f(a, b):

    _ = 0
    oo = a // 2

    for i in range(b):
        for j in range(a):
            if j == oo + _ or j == oo - _:
                print('#', end='')
            else:
                print(' ', end='')
        if i >= b // 2:
            _ -= 1
        else:
            _ += 1

        print('')


f(10, 9)


# 8
def f(n):
    ls = [[1] * n for i in range(n)]
    for i in range(n - 1):
        for j in range(n - 1):
            ls[i + 1][j + 1] = ls[i][j + 1] + ls[i + 1][j]

    return ls


for i in f(int(input())):
    print(*i)

# 9
def f(string):
    res = ''
    for i in string:
        if i.isalpha():
            res += ' '
        else:
            res += i

    return sum([int(i) for i in res.split()])

print(f('В этой1 стр13ок14е 4 всего 5 четыре числа 9'))

# 10
def f(string):
    res = ''
    for i in string:
        if i.isalpha():
            res += ' '
        else:
            res += i

    ls = res.split()
    res = 0
    for i in ls:
        sums = 0
        for j in range(len(i)):
            sums += (ord(i[j]) - 48) * (10 ** (len(i) - j - 1))
        res += sums

    return res

print(f('В этой1 стр13ок14е 4 всего 5 четыре числа 9'))

