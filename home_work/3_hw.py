def z1(a, b):

    if a > b:
        return a
    elif a == b:
        return a
    else:
        return b


print(z1(10, 20))


def z2(c, y):

    if c - y == 135 or c - y == -135:
        return 'yes'
    else:
        return 'No'


print(z2(100, 236))


def z3(m):
    if m == 12 or m == 1 or m == 2:
        return 'zima'
    elif m == 3 or m == 4 or m == 5:
        return 'vesna'
    elif m == 6 or m == 7 or m == 8:
        return 'leto'
    elif m == 9 or m == 10 or m == 11:
        return 'osen'


print(z3(5))


def z4(k, d, t):
    if k > 10 and d > 10 and t > 10:
        return 'yes'
    else:
        return 'no'


print(z4(220, 30, 10))


def z5(q, n, i):
    for i in range(5):
        if 0 < q[i]:
            n = n + 1
        return n


print(z5([1, -4, -3, 8, -256], 0, 0))


def z6(year, month):
    return (year*12 + month)*29


print(z6(4, 3))
zvanie = 5


def z6(g):
    if 1 <= g <= 4:
        return 'bakalavr'
    elif 5 <= g <= 6:
        return 'magistr'
    elif 7 <= g <= 9:
        return 'aspirant'
    else:
        return 'Vvedite korrektniy god obucheniya'


print(z6(5))
