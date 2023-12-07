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

# d = int(input("enter amound uah"))
# result = d / 40
# print(f'result {result}')