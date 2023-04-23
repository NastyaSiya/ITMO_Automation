a = 10
b = 20

if a > b:
    print(a)
elif a == b:
    print(a)
else:
    print(b)

c = 100
d = 236

if c - d == 135 or c - d == -135:
    print('yes')
else:
    print('No')

m = 5

if m == 12 or m == 1 or m == 2:
    print('zima')
elif m == 3 or m == 4 or m == 5:
    print('vesna')
elif m == 6 or m == 7 or m == 8:
    print('leto')
elif m == 9 or m == 10 or m == 11:
    print('osen')

k = 20
d = 30
t = 10

if k > 10 and d > 10 and t > 10:
    print('yes')
else:
    print('no')

q = [1, -4, -3, 8, -256]
n = 0
i = 0

for i in range(5):
    if 0 < q[i]:
        n = n + 1
print(n)

year = 4
month = 3

print((year*12 + month)*29)


zvanie = 5

if 1 <= zvanie <= 4:
    print('bakalavr')
elif 5 <= zvanie <= 6:
    print('magistr')
elif 7 <= zvanie <= 9:
    print('aspirant')
else:
    print('Vvedite korrektniy god obucheniya')
