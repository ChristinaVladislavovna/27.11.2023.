total = 0
while True:
    user_input = input("ВВедите число или 'end' для завершения: ")
    if user_input.lower() == 'end':
        break
    try:
        number = float(user_input)
        total += number
    except ValueError:
        print("Пожалуйста, введите действительное число или 'end' для завершения.")
print(f"Сума введеных чисел: {total}")