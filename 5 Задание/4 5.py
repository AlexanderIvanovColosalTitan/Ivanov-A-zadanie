def Zadanie(x, y):
    q = x
    w = 1
    while y > x:
        x *= 1.1
        q += x
        w += 1
        if q > y:
            break
    print('Преодолеет на',w, 'день')
