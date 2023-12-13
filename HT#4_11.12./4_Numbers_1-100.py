# print(list(range(10))) # range - выводит цифры от 1 до 10
#
# for i in range(2): # вывод строк х2
#     print(list(range(10)))
#
# # for i in range(2):  # вывод строк х2
# #     print(list(range(i*10)))  # от начала конца шагом 10
#
# print(list(range(10, 50, 10))) # !!!(start, end, step)!!!

"""
1 2 3 4 5 ... 10
....
90 91 ...... 100
"""
# print(list(range(0, 100, 10)))  # (start, end, step)
# 10, 11, 12, 13 ...
# 20, 21, 22, 23 ...

# range(10, 110, 10) == от 10 до 110, каждый 10 символ
start = 0 # начинать с "0"
for i in range(10, 110, 10): # 100, 10 == 100 цифр по 10 символов в каждой строке
    line = ''  #
    for j in range(start, i):
        line = line + f" {j:2}" # line  строка отформатраванна с помощью f{:2}
    print(line)
    start = i # начальный отрезок становится стартовым


print(list(range(0, 25, 2))) # от 0 до 25 каждый второй символ