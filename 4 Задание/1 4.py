def Zadanie(A, B):
    if A <= B:
        for i in range(A, B):
            print(A)
            A += 1
        print(B)
    else:
        print('A должно быть <= B')
