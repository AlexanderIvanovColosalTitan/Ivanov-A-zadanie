Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -*- coding: utf-8 -*-
... year = int(input('Введите год: '))
... if year % 4 != 0:
...     print('НЕТ')
... elif year % 100 == 0:
... if year % 400 == 0:
...     print('ДА')
... else:
...     print('НЕТ')
... else:
...     print('ДА')
...     
SyntaxError: multiple statements found while compiling a single statement
