def Zadanie(n):
    q = 0
    w = 0
    while n != 0:
        q += 1
        w += n
        n = int(input('Число последовательности - '))
    print('Среднее значение -',w/q)
