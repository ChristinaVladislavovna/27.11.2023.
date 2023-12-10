# Lebels
UAH_USD_BUY = 40 #40 грн на Доллар
UAH_USD_SELL = UAH_USD_BUY * 1.05 #+5% от продажи
# print(UAH_USD_SELL)
UAH_EURO_BUY = 45
UAH_EURO_SELL = UAH_EURO_BUY * 1.05
# print(UAH_EURO_SELL)
UAH_GBP_BUY = 50
UAH_GBP_SELL = UAH_GBP_BUY * 1.05
# print (UAH_GBP_SELL)

print("**"*19)
print(f"| {'BUY':^10} | {'CURRENCY':^9} | {'SELL':^9} |")
print("--"*19)
print(f"| {UAH_USD_BUY:^10.2f} | {'USD':^9} | {UAH_USD_SELL:^9.2f} |")
print(f"| {UAH_EURO_BUY:^10.2f} | {'EUR':^9} | {UAH_EURO_SELL:^9.2f} |")
print(f"| {UAH_GBP_BUY:^10.2f} | {'GBP':^9} | {UAH_GBP_SELL:^9.2f} |")
print("**"*19)

# def exchange_operation():
#     amount = float(input("Введите сумму для обмена: "))
#     operation = input("Выберите операцию (купить - 'buy' / продать - 'sell'): ")
#
#     if operation == 'buy':
#         # Цены на покупку и продажу, установите сами
#         usd_to_uah = 28.5  # Курс доллара к гривне для покупки
#         result = amount * usd_to_uah
#         print(f"Вы получите {result} гривен за {amount} долларов.")
#     elif operation == 'sell':
#         usd_to_uah = 27.8  # Курс доллара к гривне для продажи
#         result = amount * usd_to_uah
#         print(f"Вы получите {result} долларов за {amount} гривен.")
#     else:
#         print("Выбрана недопустимая операция. Пожалуйста, выберите 'buy' или 'sell'.")
#
# # Вызываем функцию обмена
# exchange_operation()


def exchange_operation():
    UAH_USD_BUY = 40  # 40 грн на Доллар
    UAH_USD_SELL = UAH_USD_BUY * 1.05  # +5% от продажи

    operation = input("Выберите операцию (купить - 'buy' / продать - 'sell'): ")

    if operation == 'buy':
        amount_uah = float(input("Введите сумму в гривнах для обмена на доллары: "))
        result_usd = amount_uah / UAH_USD_BUY
        print(f"Вы получите {result_usd:.2f} долларов за {amount_uah} гривен.")
    elif operation == 'sell':
        amount_usd = float(input("Введите сумму в долларах для продажи за гривны: "))
        result_uah = amount_usd * UAH_USD_SELL
        print(f"Вы получите {result_uah:.2f} гривен за {amount_usd:.2f} долларов.")
    else:
        print("Выбрана недопустимая операция. Пожалуйста, выберите 'buy' или 'sell'.")

# Вызываем функцию обмена
exchange_operation()


# currencies = {
#         'usd': {'buy': 40, 'sell': 42},
#         'euro': {'buy': 45, 'sell': 47},
#         'gbp': {'buy': 50, 'sell': 52}
#     }
#
# currency = input("Выберите валюту (usd / euro / gbp): ").lower()
# operation = input("Выберите операцию (купить - 'buy' / продать - 'sell'): ")
#
# if currency in currencies:
#     buy_rate = currencies[currency]['buy']
#     sell_rate = currencies[currency]['sell']
#
#     if operation == 'buy':
#         amount_uah = float(input(f"Введите сумму в гривнах для покупки {currency.upper()}: "))
#         result_currency = amount_uah / buy_rate
#         print(f"Вы получите {result_currency:.2f} {currency.upper()} за {amount_uah:.2f} гривен.")
#     elif operation == 'sell':
#         amount_currency = float(input(f"Введите сумму в {currency.upper()} для продажи за гривны: "))
#         result_uah = amount_currency * sell_rate
#         print(f"Вы получите {result_uah:.2f} гривен за {amount_currency:.2f} {currency.upper()}.")
#     else:
#         print("Выбрана недопустимая операция. Пожалуйста, выберите 'buy' или 'sell'.")
# else:
#     print("Выбрана недопустимая валюта. Пожалуйста, выберите из 'usd', 'euro' или 'gbp'.")

