A = int(input("A = "))
B = int(input("B = "))
if A <= B:
    for i in range(A, B):
        print(A)
        A += 1
    print(B)
else:
    print('A должно быть <= B')
