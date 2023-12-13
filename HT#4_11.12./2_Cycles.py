s = list(range(10))
print(s)
s = list(range(1, 10, 2))
print(s)

for i in range(3): # переменная в цикле
    print(f"yo {i} time")

s = [1, 2, 3] # 1, 2, 3 - отображаются последоватлельно на экране
for i in s: # переменная в цикле
    print(f"yo {i} time")


s = [1, 2, 4, 3]
for i in range(len(s)): # range(len - длинна последовательности
    if i == 2:
        break   # прирывает цикл
    elif i == 1:
        continue   # продолжить в любом случае если i = 1
    print(f"it is {i} 's element")


s = [1, 2, 4, 3]
for i in range(len(s)): # range(len - длинна последовательности
    if i == len(s):  # ecли i = длинне послеовательности
        break   # прирывает цикл
    elif i == 1:
        continue   # продолжить в любом случае если i = 1
    print(f"it is {i} 's element")


s = [1, 2, 4, 3]
counter = 0  #
for i in range(len(s)): # range(len - длинна последовательности
    print(f"it is {i} 's element")
    counter+= 1  # увеличить на 1
if counter ==len(s): # если увеличение = длинне последовательности
    print("Success")


s = [1, 2, 4, 3]
counter = 0  #
for i in range(len(s)): # range(len - длинна последовательности
    print(f"it is {i} 's element")
    counter=+1
else:
    print("Yeah!")


"""
ЦИКЛ с предусловиями PRECONDITIONS
"""

condition = True
while condition:
    print("TRUE") # бесконечное выполнение цикла
    condition = False # нужно обоснованное условие для остановки цикла ( с случае если известно сколько циктов должно быть)

# цикл в цикле
for i in range(3):
    for j in range(2): # выполняется по 2 цикла, в каждом из 3х циклов
        print("Hi!") # = х6Hi!
