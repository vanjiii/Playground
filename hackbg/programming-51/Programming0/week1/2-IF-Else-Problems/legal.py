'''
Във файл, който се казва legal.py, напишете програма, която прави следното:

Чете от потребителя число, което отговаря на годините му.
Ако годините са >= 21, му казва, че е легален.
Иначе му казва, че е нелегален!
'''

age = input("Enter age: ")
age = int(age)

if age >= 21:
	print("You are LEGAL!!!")
else:
	print("You are ILLIGAl!!!")