s = input('Введите строку - ')
print(s[0].upper(), sep = '', end = '')
for i in range(1, len(s)):
    if s[i-1] == ' ':
        print(' ', sep = '', end = '')
        print(s[i].upper(), sep = '', end = '')
    else:
        print(s[i], sep = '', end = '')
        
