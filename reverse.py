# Развернуть в обратном порядке только первое и последнее слово строки - "вонавИ Иван чивонавИ"
def abc(fio):
    mass = fio.split(' ')
    mass[0] = mass[0][::-1]
    mass[2] = mass[2][::-1]
    return " ".join(mass)
print(abc('Иванов Иван Иванович'))

# через format
a = 'Иванов'[::-1]
b = 'Иван'
c = 'Иванович'[::-1]
print('{0} {1} {2}'.format(a, b, c))

# f-string
print(f'{"Иванов"[::-1]} {"Иван"} {"Иванович"[::-1]}')