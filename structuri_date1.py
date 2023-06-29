Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l1=['abcd', 786, 2.23, 'ion', 70.2]
>>> print(l1, "/n", l1[0])
['abcd', 786, 2.23, 'ion', 70.2] /n abcd
>>> print(l1[2], l1[3], l1[4])
2.23 ion 70.2
>>> print (l1, l1)
['abcd', 786, 2.23, 'ion', 70.2] ['abcd', 786, 2.23, 'ion', 70.2]
>>> l2 = [123,14]
>>> l3 = l1 + l2
>>> l1[1] = 1
>>> print (l3)
['abcd', 786, 2.23, 'ion', 70.2, 123, 14]
>>> l4 = l2
>>> l2[0] = 2
>>> print(l4)
[2, 14]
>>> l5 = [1,2,3,4,5]
>>> print(l5)
[1, 2, 3, 4, 5]
>>> LASTTWO = slice[1,2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    LASTTWO = slice[1,2]
TypeError: type 'slice' is not subscriptable
>>> l5[1:1] = [7,7,7,7,7,7]
>>> print(l5)
[1, 7, 7, 7, 7, 7, 7, 2, 3, 4, 5]
>>> l5[:0] = l5
>>> print(l5)
[1, 7, 7, 7, 7, 7, 7, 2, 3, 4, 5, 1, 7, 7, 7, 7, 7, 7, 2, 3, 4, 5]
>>> del l5
>>> l6 = [l1,l2,l5]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l6 = [l1,l2,l5]
NameError: name 'l5' is not defined. Did you mean: 'l1'?
>>> l5= [1,2,3,4,5]
>>> l6 = [l1,l2,l5]
>>> l6[0] = 'h'
>>> print(l6)
['h', [2, 14], [1, 2, 3, 4, 5]]
