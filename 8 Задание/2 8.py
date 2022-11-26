def Zadanie2(s):
    q = ''
    i = len(s)-1
    while i >= 0:
        if s[i] == ' ':
            q = q + s[i+1:] + ' '
            s = s[:i]
            i = len(s) - 1
        else:
            i -= 1
    q = q + s
    return q
w = input()
w = Zadanie2(w)
print(w)
