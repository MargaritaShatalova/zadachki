# Заменить все пробелы на "_"
full_name = 'Иванов Иван Иванович'

# через format
print('Иванов{0}Иван{0}Иванович'.format('_'))

# через f-string
print(f'Иванов{"_"}Иван{"_"}Иванович')

# через join
my_list_name = full_name.split()
print("_".join(my_list_name))

# через join покороче
print("_".join(full_name.split()))

# через translate
new_name = full_name.maketrans(' ', '_')
print(full_name.translate(new_name))