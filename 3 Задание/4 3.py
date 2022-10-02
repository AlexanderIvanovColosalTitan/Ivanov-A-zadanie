def Zadanie_4(a, b, l, N):
    sh = ((N*2-1)*a)+((N*2-2)*b)+2*l
    if sh == 0:
        print("У вас нет шнурков*_*")
    else:
        print("Вам нужны шнурки длинны - ", sh)
