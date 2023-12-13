# # float chteck:

# print("1234567.890".isdigit() == True)
# """
# выдалить точку и спросить метод isdigit
# """
# """
# уточнить что символ число или точка
# просчитать количество чисел и точек
# сумма должна совпадать со строкой
# """

value = "1234567.890"
letter_count = 0
period_count = 0

for i in value: # цикл, где i - перебирает каждое значение в value (переменая)
    if i in "1234567.890": #
        letter_count+=1 #
    elif i == ".": #
        period_count+=1 #

if (letter_count+period_count) == len(value): #
    print("It's float") #
else:
    print("Not a flaot!") #

# с импортированными методами и функциями:

# №2

from string import ascii_letters, digits, ascii_lowercase

print(ascii_letters)
print(digits)

for i in value: # цикл, где i - перебирает каждое значение в value (переменая)
    if i in digits: # если каждое значение i есть в цифрах
        letter_count+=1 #
    elif i == ".": #
        period_count+=1 #

if (letter_count+period_count) == len(value) and value.startswith(".") and not value.endswith("."): #
    print("It's float") #
else:
    print("Not a flaot!") #