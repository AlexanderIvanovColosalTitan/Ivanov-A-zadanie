def Zadanie(n):
    q = 1
    for i in range(1, n):
        q *= i
    q *= n
    print(q)
