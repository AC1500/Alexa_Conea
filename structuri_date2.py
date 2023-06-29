Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t1= ('abcd', 786, 2.23, 'ion', 70.2)
>>> print(t1)
('abcd', 786, 2.23, 'ion', 70.2)
>>> #in tuplu nu se pot modifica elemente
>>> print("tuplul are" + str(len(t1)) + "elemente")
tuplul are5elemente
>>> t2 = [123,14]
>>> t2 = [123,14]
>>> t2=(123,14)
>>> print(t2)
(123, 14)
>>> print("minimul in t2" + str(min(t2)))
minimul in t214
>>> #nu putem gasi minimul in t1 pentru ca avem elemente de 2 tipuri de date
