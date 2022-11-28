def Zadanie(n):
    q = 2
    w = 1
    while n > q:
        q *= 2
        w += 1
        if q * 2 > n:
            break
    print('Степень -', w, 'Показатель степени - ', q)
