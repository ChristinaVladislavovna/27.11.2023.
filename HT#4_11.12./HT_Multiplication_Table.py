# 10*100
number = int(input("Введіть число від 1 до 100: "))

if 1 <= number <= 100:
    print(f"Таблиця множення для числа {number}:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")
else:
    print("Будь ласка, введіть число від 1 до 100.")

# 100*100
number = int(input("Введіть число від 1 до 100: "))

if 1 <= number <= 100:
    print(f"Таблиця множення для числа {number} (до 100*100):")
    for i in range(1, 101):
        print(f"{number} * {i} = {number * i}")
else:
    print("Будь ласка, введіть число від 1 до 100.")