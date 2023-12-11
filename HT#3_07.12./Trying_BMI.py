print("Выберите систему измерения:")
print("1. Метрическая (кг, см)")
print("2. Английская (фунты, футы)")

choice = input("Введите ваш выбор (1 или 2): ")

if choice == "1":
    weight = float(input("Введите ваш вес в килограммах: "))
    height = float(input("Введите ваш рост в сантиметрах: "))
    bmi = weight / ((height / 100) ** 2)  # Расчет ИМТ для метрической системы
    print(f"Ваш ИМТ составляет: {bmi:.2f}")
elif choice == "2":
    weight = float(input("Введите ваш вес в фунтах: "))
    height = float(input("Введите ваш рост в футах: "))
    bmi = (weight / (height ** 2)) * 703  # Расчет ИМТ для английской системы
    print(f"Ваш ИМТ составляет: {bmi:.2f}")
else:
    print("Неверный выбор.")

if bmi < 18.5:
    print("Underweight / Недостаток веса")
elif 18.5 <= bmi < 25:
    print("Normal weight / Нормальный вес")
elif 25 <= bmi < 30:
    print("Overweight / Избыточный вес")
else:
   print("Obesity / Ожирение")