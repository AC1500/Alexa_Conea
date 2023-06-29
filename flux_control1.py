Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=3
>>> b= 'test'
>>> c= [1,2,3]
>>> d = 'none'
>>> e = None
>>> f = 0
>>> 
>>> print(a or b)
3
>>> print(a and b)
test
>>> print(a and c)
[1, 2, 3]
>>> print( a and d)
none
>>> print(b or d)
test
>>> print (a and e)
None
>>> print (a and f)
0
#setare valoare variabila 
var = 56.11
if type(var)is int:
	if(var>=5):
	print("Numar mai mare decat 5")
	else:
	print("Numar mai mic decat 5")
	elif type(var) is str:
	print("string")
	else:
	print("alceva")

#l1

l1 = ['abcd', 786, 2.23, 'ion', 70.2]
for i in range(len(l1)):
	print(l1[i])
for (i,val) in enumerate(l1):
	print(i,val)

# numerele pare din intervalul 5 si 47

i = 5
while i<= 47:
	if i % 2 == 0:
	print(i)
	i += 1


#evidenta aprozar

l_fructe = ['mere', 'pere', 'nuci']
l_pret = [10,14,15]

print("stocul curent")
for fruct, pret in zip(l_fructe, l_pret):
	print(fruct.capitalize(), ':', pret, 'lei/kg')

print('produs sub 14 lei:')
for fruct, pret in zip(l_fructe, l_pret):
	if pret < 14:
	print(fruct.capitalize(), ':', pret, 'lei/kg')



	


