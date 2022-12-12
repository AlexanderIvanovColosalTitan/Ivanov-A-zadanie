def Zadanie(n): 
    if len(n) == 1:
        return n
    else:
        return n[-1] + Zadanie(n[:-1])
print(Zadanie(input()))
