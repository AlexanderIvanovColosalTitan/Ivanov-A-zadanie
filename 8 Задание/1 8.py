n = int(input('n = '))
if n <= 210 or n >= 231:
    print("Нужно n, большее 210 и меньшее 231")
else:
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    q = 0
    for i in range (100, n + 1):
        if (a*100+b*10+c)==i or (a*100+c*10+b)==i or (b*100+a*10+c)==i or (b*100+c*10+a)==i or (c*100+a*10+b)==i or (c*100+b*10+a)==i:
            q += 1
    print('Кол-во чисел, составленных из букв a, b, c =', q)
        
    
