Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -*- coding: utf-8 -*-
... second = int(input())
... days = 0
... hours = 0
... minutes = 0
... seconds = 0
... days = second // 86400
... second = second % 86400
... hours = second // 3600
... second = second % 3600
... minutes = second // 60
... second = second % 60
... seconds = second
