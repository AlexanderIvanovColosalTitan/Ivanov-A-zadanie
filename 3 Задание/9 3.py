def Zadanie_8(n, m, k):
    if k < n * m and ((k % n == 0) or (k % m == 0)):
        print('ДА')
    else:
        print('НЕТ')
