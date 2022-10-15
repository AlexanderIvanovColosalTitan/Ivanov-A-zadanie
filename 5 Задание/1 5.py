n = int(input('n = '))
q = 2
while n >= q:
    if n % q == 0:
        print(q)
        break
    else:
        q += 1
