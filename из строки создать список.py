# разбить строку на подстроки
example_string2 = "Apples,Oranges,Pears"
groceries = example_string2.split(',')
for el in groceries:
    print(el)

numbers = '1 2 3'
print(numbers.split(' '))

my_string = "I code for 2 hours everyday"
print(my_string.split())
print(my_string.split('o',2)) # в скобках - необязательные аргументы

# объединить подстроки в строку
my_list = my_string.split()
print(" ".join(my_list))