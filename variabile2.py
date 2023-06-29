Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= 3
>>> b= 3.2
>>> c = " Ionut Popescu"
>>> d = " Learn"
>>> print(a+b)
6.2
>>> print (a+c)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print (a+c)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> #nu se pot aduna int cu string
>>> 
>>> print (c+d)
 Ionut Popescu Learn
>>> print((str(b) + c)
...       print ((str(b) +c)[:4])
...       
SyntaxError: '(' was never closed
>>> print (str(b)+c)
...       
3.2 Ionut Popescu
>>> print ((str(b) +c)[:4])
...       
3.2 
>>> #b trebuie convertit in string pt a putea arata primele 4 caractere ale operatiei
...       
>>> 
>>> print(d*3)
...       
 Learn Learn Learn
>>> print (a*3)
...       
9
>>> del(b)
...       
