Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -*- coding: utf-8 -*-
... second = int(input())
... day = 0
... hour = 0
... minute = 0
... seconds = 0
... day = second // 86400
... second = second % 86400
... hour = second // 3600
... second = second % 3600
... minute = second // 60
... second = second % 60
... seconds = second
... print (day, hour, minute, seconds)
SyntaxError: multiple statements found while compiling a single statement
