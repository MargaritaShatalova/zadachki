# Удалить все повторяющиеся буквы
def removeDupes(name):
    newStr = ""
    for i in name:
        if i not in newStr:
            newStr = newStr + i
    return newStr
print(removeDupes("Иванов Иван Иванович".lower()))

# написать предикат который проверяет наличие в строке повторяющиеся буквы
# написать предикат который проверяет наличие всех букв латинского алфавита в строке

