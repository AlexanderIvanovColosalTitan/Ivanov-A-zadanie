q = []
n = int(input('Введите длину массива - '))
w = 0
k = 0
s = 0
for i in range(n):
    print('Введите', i, 'элемент массива')
    q.append(int(input()))
while n >= w:
    k = 0
    while n > k:
        if (q[w] == q[k]) and (w != k):
            print(q[w])
            s = q[w]
            q.remove(s)
            k += 1
        else:
            k += 1
    w += 1
            
        
