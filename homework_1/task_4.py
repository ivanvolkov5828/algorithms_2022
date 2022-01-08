# пусть есть пользователь с данными
user = {
    "login": "ivan_volkov2003",
    "password": "1235522",
    "activation": True
}

# алгоритм № 1 O(1)
def checkout(data):
    login_u = input("Введите логин пользователя: ") # O(1)
    password_u = input("Введите пароль пользователя: ") # O(1)

    if (data["login"] == login_u and data["password"] == password_u) and (data["activation"]): # O(1) + O(1) + O(1)
        print("Добро пожаловать")
    else:
        print("Данные введены неверно, либо пользователь не активирован")

checkout(user)

# алгоритм № 2 O(n)
def checkout_1(data):
    for key, value in data.items(): # O(n)
        if key == "activation": # O(1)
            if data[key]: # O(1)
                print("Пользователь аутентифицирован")
                break
            else: # O(1)
                print("Нужно пройти аутентификацию")
                break

        login_or_pass = input("Введите данные: ") # O(1)
        if value == login_or_pass: # O(1)
            print("Данные введены верно")
        else: # O(1)
            print("Данные введены неверно")

checkout_1(user)

# Эффективнее будет первый алгоритм, так как константная сложность
