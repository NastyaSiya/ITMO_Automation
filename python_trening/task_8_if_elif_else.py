num_float = 24.11


if num_float > 0:
    print('Polozhitelnoe chislo')
elif num_float == 0:
    print('Nol')
else:
    print('Chislo otritsatelnoe')


permit_print = True
num = 3


if num > 0 and permit_print:
    print('num - polozhitelnoe chislo')
elif not permit_print:
    print('Pechat zapreschena')


num_2 = 120


if num_2 > 100 or num_2 < -100:
    print('-')
else:
    print('+')
