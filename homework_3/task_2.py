import hashlib
import csv

def creating_a_hash():
    # первая часть программы для создания хеша
    passwd = input("Введите пароль: ")
    salt = "123321"
    result = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    with open('text.csv', 'w') as f:
        f.write(result)
    return result

def password_verification():
    # вторая часть программы для проверки пароля
    passwd = input("Введите пароль повторно: ")
    salt = "123321"
    result = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
    with open('text.csv', 'r') as f:
        hash = f.read(len(result))
    if hash == result:
        return f"Добро пожаловать!"
    else:
        return f"Пароль введен неверно. Попробуйте еще раз"

print(creating_a_hash())
print(password_verification())