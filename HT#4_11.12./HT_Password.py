# Пароль минимум 12 символов, 1 большая буква, одна маленькая, один спецсимвол:

import re

print("Пароль должен состоять не менее, чем из 12 символов (латиницы), из них минимум одна заглавная буква, минимум одна маленькая и один спецсимвол (?!/@)")
while True:
    user_password = input("Please enter your password: ")
    if len(user_password) < 12:
        print("Password is insecure! Too short.")
        continue
    if not re.search("[A-Z]", user_password) or not re.search("[a-z]", user_password):
        print("Password is insecure! Missing uppercase or lowercase letters.")
        continue
    if not re.search("[0-9]", user_password):
        print("Password is insecure! Not enough numbers.")
        continue
    if not re.search("[?!@]", user_password):
        print("Password is insecure! Not enough spesial character (?/!@).")
        continue
    print(" Well done! Password is secure!")
    break