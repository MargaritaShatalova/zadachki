# "Иванов Иванович" - вставить в середину имя
# через f-string
name = 'Иван'
print(f'Иванов {name} Иванович')

# еще вариант
sername = 'Иванов '
print(str(sername) + 'Иван Иванович')

# через format
name = 'Иван'
name2 = 'Иванович'
print('Иванов {0} {1}'.format(name, name2))
