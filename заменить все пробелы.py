# Заменить все пробелы на "_"
print('Иванов{0}Иван{0}Иванович'.format('_'))

# через join
full_name = 'Иванов Иван Иванович'
my_list_name = full_name.split()
print("_".join(my_list_name))

# через join покороче
full_name = 'Иванов Иван Иванович'
print("_".join(full_name.split()))

# через translate
full_name = 'Иванов Иван Иванович'
new_name = full_name.maketrans(' ', '_')
print(full_name.translate(new_name))