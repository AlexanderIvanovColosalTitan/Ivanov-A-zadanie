max = 0
q = 1
w = 0
n = int(input('Число последовательности - '))
while n != 0:
    if n == w:
        q += 1
    else:
        q = 1
    if q > max:
        max = q
    w = n
    n = int(input('Число последовательности - '))
print('Наибольшее число одинаковых, идущих подряд -',max)
