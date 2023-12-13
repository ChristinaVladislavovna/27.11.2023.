a = int(input("Введіть число a (1 < a < 200): "))
b = int(input("Введіть число b (1 < b < 200): "))

if 1 < a < 200 and 1 < b < 200:
    for divisor in range(2, 7):
        print(f"Divisible by {divisor}:", end=" ")
        count = 0
        for number in range(a, b):
            if number % divisor == 0:
                print(number, end=", ")
                count += 1
                if count % 10 == 0:
                    print()
        print()
else:
    print("Числа a та b повинні бути у межах від 1 до 200.")
