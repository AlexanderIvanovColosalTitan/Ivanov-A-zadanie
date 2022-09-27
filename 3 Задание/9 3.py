Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -*- coding: utf-8 -*-
... n = int(input())
... m = int(input())
... k = int(input())
... if k < n * m and ((k % n == 0) or (k % m == 0)):
...     print('ДА')
... else:
