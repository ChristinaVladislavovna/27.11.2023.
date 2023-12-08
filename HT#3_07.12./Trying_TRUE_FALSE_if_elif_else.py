# # FALSE or TRUE - не соответствует или соостветствует
#
# print(5<4)
# a = 5 < 4 #FALSE
# print(a)
#
# a = 5 > 4 #TRUE
# print(a)
#
# a = 5 <= 5 #TRUE
# print(a)
#
# a = 5 != 0 #TRUE
# print(a)
#
# a = 5 == 5 #TRUE
# print(a)


# and   true and true = true   |   false and false = false
# print(True and True)
# print(5 == 5 and 5 > 4)
# print(False and False)
# print(5 != 5 and 5 > 6)
# print(False and True)
# print(5 != 5 and 5 > 4)
# print(True and False)
# print(5 == 5 and 5 > 6)
# print(not True)
# print(not False)


# сложение TRUE False
# print(0 == False)
# print(True + 44)   # = 45
# print(45 - False)  # = 5
# print(45 + False)  # = 45


# Наличие УСЛОВИЙ "if elis else"
# № 1
# condition1 = 5 > 3
# condition2 = 3 < 5
# if condition1:
#     print("Условие выполнено")
# elif condition2:
#     print("Условие 1 не выполнено, условие 2 выпослено")
# else:
#     print("Ни одно условие не было выполнено")
#
# № 2
# condition1 = False
# condition2 = 3 < 5
# if condition1:
#     print("Условие выполнено")
# elif condition2:
#     print("Условие 1 не выполнено, условие 2 выпослено")
# else:
#     print("Ни одно условие не было выполнено")
#
# № 3
# condition1 = False
# condition2 = False
# if condition1:
#     print("Условие выполнено")
# elif condition2:
#     print("Условие 1 не выполнено, условие 2 выпослено")
# else:
#     print("Ни одно условие не было выполнено")

# № 4
# condition1 = False
# condition2 = False
# if condition1:
#     print("Условие выполнено")
# elif condition2:
#     print("Условие 1 не выполнено, условие 2 выпослено")
#     pass # блокирует выполнение строки
# else:
#     print("Ни одно условие не было выполнено")

# № 5
# condition1 = False
# condition2 = False
# if condition1:
#     print("Условие выполнено")
# elif condition2:
#     print("Условие 1 не выполнено, условие 2 выпослено")
# else:
#     print("Ни одно условие не было выполнено")
#     pass  # блокирует выполнение модуля - но это не точно!!!
#     print("Ни одно условие не было выполнено")

# # 5
# condition1 = False
# condition2 = True
#
# if condition1:
#     print("Условие выполнено")
# elif condition2:
#     if condition1:
#         print("Imposible to")
#     else:
#         pass
#     print("Условие 2 выполнено")
# else:
#     print("Ни одно условие не было выполнено")
#
# print("Next orders.")
# # True and True and (True or False) and not False
# # (a > b) and (check_volue (c) and (.......))
#
# if True and True and (True or False) and not False:
#     print("Do somethink")
# if 1:
#     print("True")
# if not "" or [] or () or {}:
#     print("Count as False")
#
# """
# Что триггерит False:
# Вместо False в if может быть 0, NONE, "", {}, (), []
# "",{}, (), [] - пустая строка или любая пустая последовательность
# """
# d - None # NONE обозначает НИЧЕГО!!!!!
# print("") # "" = str string пустой





