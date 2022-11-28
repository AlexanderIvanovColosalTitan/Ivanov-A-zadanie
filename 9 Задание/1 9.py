print('m = кличество сток')
print('n = кличество столбцов')
def Zadanie(m, n):
    q = 0
    max = 0
    w = 0
    r = 0
    a = []
    for i in range(m):
        b = []
        for j in range(n):
            print('Введите [',i,',',j,'] элемент')
            b.append(int(input()))
        a.append(b)
    print('Исходный массив:')
    for i in range(m):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
    while q <= m:
        for i in range(n-1):
            w = 0
            if a[q-1][i-1] > a[q-1][i]:
                for j in range(n-1):
                    if a[q-1][j-1] > a[q-1][j]:
                       w += 1
                if w == n-2:
                    if a[q-1][0] > max:
                        max = a[q-1][0]
            elif a[q-1][i-1] < a[q-1][i]:
                for j in range(n-1):
                    if a[q-1][j-1] < a[q-1][j]:
                       w += 1
                if w == n-2:
                    if a[q-1][n-1] > max:
                        max = a[q-1][n-1]
        q += 1
    print(max)
            
