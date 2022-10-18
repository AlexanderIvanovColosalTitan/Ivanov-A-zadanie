"n! = q"
q = 1
n = int(input("n = "))
for i in range(1, n):
    q *= i
q *= n
print(q)
