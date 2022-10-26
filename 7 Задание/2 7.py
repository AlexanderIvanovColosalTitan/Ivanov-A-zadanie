n = 15
q = []
for i in range(n):
    print('Введите', i, 'элемент массива')
    q.append(int(input()))
print('Первоначальный массив - ', q)
for i in range(n):
    if q[i] < 10:
        q[i] = 0
    if q[i] > 20:
        q[i] = 1
print('Преобразованный массив - ', q)
        
