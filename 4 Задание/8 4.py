def Zadanie(n):
    for i in range(1, n):
        q = 1
        while i >= q:
            print(q, end="")
            q = q + 1
        print(end='\n')
    q = 1
    while n >= q:
        print(q, end="")
        q = q + 1
