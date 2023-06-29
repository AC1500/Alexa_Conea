Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dictionar_ro_en = {'creion':'pencil', 'birou':'desk', 'masa':'table'}
>>> print("Cuvintele in romana: ", dictionar_ro_en.keys())
Cuvintele in romana:  dict_keys(['creion', 'birou', 'masa'])
>>> print(dictionar_ro_en.values())
dict_values(['pencil', 'desk', 'table'])
>>> print(dictionar_ro_en["creion"])
pencil
>>> print(dictionar_ro_en.get("creion"))
pencil
>>> print(dictionar_ro.en("doi"))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(dictionar_ro.en("doi"))
NameError: name 'dictionar_ro' is not defined. Did you mean: 'dictionar_ro_en'?
