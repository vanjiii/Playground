'''
Нека да имаме следните списъци:

a = [1, 2, 3]
b = [4, 5, 6]
c = [1]
d = [8, 8, 10]
Напишете изрази, които:

Сливат всичи списъци, като крайният резултат трябва да е [1, 4, 5, 6, 1, 2, 3, 8, 8, 10]
Сливат списъците a с b
Сливат списъците c с d
Сливат списъка a с a
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [1]
d = [8, 8, 10]

all_lists = a + b + c + d

acb = a + c + b

ccd = c + c + d

aca = a + c + a

print(all_lists)
print(acb)
print(ccd)
print(aca)
