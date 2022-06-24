# "Иванов Иванович" - вставить в середину имя
print('Иванов {} Иванович'.format('Иван'))

# второй вариант
name = 'Иван'
name2 = 'Иванович'
print('Иванов {0} {1}'.format(name, name2))

# третий вариант
first_name = "Иван"
middle_name = 'Иванович'
last_name = "Иванов"
message = f"Меня зовут {first_name} {middle_name}, и фамилия моя {last_name}"
print(message)