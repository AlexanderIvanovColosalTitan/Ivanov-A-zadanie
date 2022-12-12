def Zadanie():
    q = int(input())
    if q == 0:
        return 0
    else:
        return max(q, Zadanie())
print(Zadanie())
