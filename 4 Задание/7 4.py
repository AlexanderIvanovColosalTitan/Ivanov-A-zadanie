def Zadanie(n):
    w = 0
    q = 1
    for i in range(1, n):
        q *= i
        w += q
    q *= n
    w += q
    print(w)
