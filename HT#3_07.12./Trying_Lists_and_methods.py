s = "abcdefg"

print(s[0]) # первый символ
print(s[-1]) # первый символ с обратной стороны (задом наперед)
print(s[0:-2]) # от первого символа до "от минус второго"
print(len(s)) # расчитает п=количество символов в сторке
print(s[0:5:2]) # от 0 до 5, каждаый второй (включая первый символ)
print(s[:4]) # от первого до 4
print(s[:]) #от начала до конца
print(s[::]) #от начала до конца каждый симлов
print(s[::2]) # от начала до конца каждый второй символ
print(s[::-1]) # от начала до конца в обратном порядке
print(s[::3]) # adg
print(s[1:4:-1]) # не дает ответ почему то
print(s[-1:-4:-1]) # тоже ответ все мимо

s = "hello"
print(s.capitalize()) # делает первую символ заглавным = Hello
print(s.upper()) # делает все символы заглавными = HELLO
print(s)
# a = s.upper()
# print(a)
# print(a.lower()) # делает символы маленькими
# print(a.startswith("H")) # true or false Если начивается с "Н"
# print(a.endswith("O")) #  true or false Если заканчивается "О"
print(s.strip("h")) # уберает символы с обоих сторон
print(s.rstrip("h")) # уберает символ справа
print(s.lstrip("h")) # убирает символ слева
print(s.replace("o", "!")) # меняет символы местами
print(s.count("a")) # поиск по симвовам
print(s.count("l")) # поиск по симвовам = количество символов в строке
print(s.isdigit()) # проверяет цифра это или нет
print("12345".isdigit())
print("12345".isdecimal())
print(s.index("e")) # количество символов
print(s.index("l",3)) # показывает позицию
print(s.find("!")) # поиск


c = "0123456789"

if "b" in c:
    print(False)
elif "4" in c or "c" in c:
    print(False)
elif "2" in c and "3" in c:
    print(True)
else:
    print(OK)
