# #1
def calculate_bmi(height, weight):
    bmi = weight / ((height / 100) ** 2)
    return bmi

def print_bmi_table():
    print("--" * 25)
    print(f"| {'ИМТ':^14} | {'ИМТ':^30}|")
    print("--" * 25)
    print("| Менее 16       | Выраженный дефицит массы тела |")
    print("| 16 - 18.49     | Недостаточная масса тела      |")
    print("| 18.5 - 24.99   | Норма                         |")
    print("| 25 - 29.99     | Избыточная масса тела         |")
    print("| 30 - 34.99     | Ожирение первой степени       |")
    print("| 35 - 39.99     | Ожирение второй степени       |")
    print("| Более 40       | Ожирение третьей степени      |")
    print("--" * 25)

print("Таблица категорий ИМТ:")
print_bmi_table()


    def main():
        print("Выберите систему измерения:")
        print("1. Метрическая (кг, см)")
        print("2. Английская (фунты, футы)")

        choice = input("Введите ваш выбор (1 или 2): ")

        if choice == "1":
            weight = float(input("Введите ваш вес в килограммах: "))
            height = float(input("Введите ваш рост в сантиметрах: "))
            bmi = calculate_bmi(weight, height, "metric")
        elif choice == "2":
            weight = float(input("Введите ваш вес в фунтах: "))
            height = float(input("Введите ваш рост в футах: "))
            bmi = calculate_bmi(weight, height, "imperial")
        else:
            print("Неверный выбор.")
            return

        print(f"Ваш ИМТ составляет: {bmi:.2f}")


    #
    if __name__ == "__main__":
        main()