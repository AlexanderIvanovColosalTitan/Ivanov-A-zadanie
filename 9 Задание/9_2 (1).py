print('Введите количество строк - m')
print('Введите количество столбцов - n')
def Zadanie(m, n):
    D = []
    for i in range(m):
        b = []
        for j in range(n):
            print('Введите [',i,',',j,'] элемент')
            b.append(int(input()))
        D.append(b)
    print('Исходный массив:')
    for i in range(m):
        for j in range(n):
            print(D[i][j], end=' ')
        print()
    print("Введите строку, столбцы которой нужно расположить в порядке возрастания")
    k = int(input('==>'))
    if (k<1) or (k>m):
        print('k должна быть в диапазоне(1<=k<='+m+')')
    else:
        for j in range(n+1):
            y = j-1
            for i in range(n+1):
                u = i-1
                if D[k][u] > D[k][y]:
                    p = 0
                    while p != (n):
                        D[p][y], D[p][u], = D[p][u], D[p][y]
                        p += 1
    for i in range(m):
        for j in range(n):
            print(D[i][j], end=' ')
        print()
          
