
a = int(input("Введите число a (1 < a < 200): "))
b = int(input("Введите число b (1 < b < 200): "))

if 1 <= a <= 200 and 1 <= b <= 200: # Условие
    if a > b:
        a, b = b, a # Равнозначность
    for divisor in range(2, 7): # Строки - группы делимых чисел на 2, 3, 4, 5, 6
        print(f"Числа, которые делятся на {divisor}:")
        count = 0
        for number in range(a, b + 1): # + 1 = каждый последующий
            if number % divisor == 0:
                print(number, end=", ")
                count += 1
                if count % 10 == 0:
                    print()
        print()
else:
    print("Числа a и b должны быть в рамках от 1 до 200.")