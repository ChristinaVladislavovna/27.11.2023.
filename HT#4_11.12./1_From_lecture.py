"""
int - целые
float - дробные
str - строки текст (контейнер - сохраняет символы)
bool - логичные
None - ничего
"""
s = "sasasa"
print(s[0]) # первый символ на экран
list_1 = [1, 2, 3, 4.1, 'str', True, [1, 2, 3, 4]] #
print(list_1[0]) # первый = 1
print(list_1[-1]) # первый с конца (последний) = [1,2,3,4]
print(list_1[:4]) #  = 1,2,3,4.1
print(list_1[-1][0]) # последний с конца, в нем первый элемент = 1
print(list_1[4][0]) # 4й по счету, и 1й в списке = s
list_1 = [1, 2, 3, 4.1, 'str', True, [5, 6, 7, 8, [[9, 10, 11]]]]
print(list_1[6][4][0][1]) #
"""
list_1 = [1,2,3,4.1, 'str', True, [1,2,3,4[[1,2,3]]]]
[1,2,3,4.1, 'str', True, [1,2,3,4[[1,2,3]]]] - нулевой элемент
1 - нулевой элемент
2 - первый
3 - второй
4.1 - третий
'str' - червертый
True - пятый
[1,2,3,4[[1,2,3]]] - шестой
в шестом элементе:
[1,2,3,4[[1,2,3]]]
1 - нулевой
2 - первый
3 - второй
4 - третий
[[1,2,3]] - четверый
в четверном элементе:
[[1,2,3]] - нулевой
а в нем:
1 - нулевой
2 - первый
3 - второй
"""
list_2 = [1, 2, 3,]
list_2.append(4) # метод добавляет символ в конец списка
print(list_2)
print(list_1+list_2) # можно складывать списки
print(list_2.extend([5,6])) # объединяет списки
print(list_2)
s = [1, 2, 3]
s[0] = 4 # меняет символы нулевой (цифру 1) на цифру 4 = [4, 2, 3]
print(s)
s.remove(4) # удаление символа = [2, 3]
print(s)
s.pop(0) # удаляет по индексу = [3]
print(s)
q = [10, 11, 12, 13, 14]
# a.count() # считает количество символов
q.reverse() # переносит символы в обрантом порядке
print(q)
w = ["A", "1", "a", "aa", "aaa", "b"] # сортирует:
# 1 - цифры
# 2 - слова с Больших букв в алфавитном порядке
# 3 - слова с маленьких букв в алфавитном порядке
# 4 - спец символы
w.sort()
w.sort(reverse=True) # в обратном порядке
w.sort(key=len) # сортировка по длинне
print(w)

a = [1, 2, 3, 4]
b = a # получается один список - два названия
a.pop(2) # удалить второй индукс (3й по счету символ)
print(a, b) # обьединяет две таблицы
c = a.copy() # копирует объект
print(a, b, c)

print(a is b)  # a ЭТО b
print(a is c)

s1 = "a"
s2 = "b"
print(s1 is s1)  # == TRUE
s2 = s2.capitalize().lower()  # каждое слово с большой буквы + все в нижним реестре
print(s1 is s2)
print(s1 == s2)

val1 = 100000
val2 = 100000
print(val1 is val2) # TRUE
print(val1 == val2) # TRUE

print("1234567890".isdecimal()) # TRUE проверяет что это число
print("1234567890.".isdecimal()) # FALSE
print("1234567890".isdigit()) # TRUE

