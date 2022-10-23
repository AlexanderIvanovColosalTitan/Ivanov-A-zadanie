n = int(input('Число - '))
q = 2
if n < 2:
    print("Нужно больше двух")
for i in range (2, n):
    if n%q == 0:
        break
    q += 1
print("Наименьший делитель - ",q)
