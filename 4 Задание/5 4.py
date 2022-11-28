def Zadanie(n):
    q = 0
    for i in range(1, n):
        q = q + i**3
    q = q + n**3
    print(q)
