A = int(input('A = '))
B = int(input('B = '))
if A > B:
    while A >= B:
        print(A)
        A -= 1
else:
    while B >= A:
        print(B)
        B -= 1
