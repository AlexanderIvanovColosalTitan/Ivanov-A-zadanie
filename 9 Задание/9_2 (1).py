m = int(input('Введите количество строк - '))
n = int(input('Введите количество столбцов - '))
D = []
q = 0
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
if (k<=1) or (k>m):
    print('k должна быть в диапазоне(1<=k<='+m+')')
'''min = D[k][0]
for i in range(n):
    if D[k][i] < min:
        D[0],D[i] = D[i],D[0]'''
q = m-1
while k > 0:
    t = 0
    for i in range(q+1):
        if D[q][i] > D[q][t]:
            t = i
    for j in range(n):
        r = D[j][t]
        D[j][t] = D[j][q]
        D[j][q] = r
    q -= 1
for i in range(m):
    for j in range(n):
        print(D[i][j], end=' ')
    print()         
