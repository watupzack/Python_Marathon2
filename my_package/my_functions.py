print("Here are my functions")


# Несколько манипуляций с строкой
# Замена регистра и подсчет пробелов
def change_string(s):
    space_counter = 0
    for c in s:
        if c.isspace():
            space_counter += 1
    s = s.swapcase()
    print(s)
    print(f"Тут {space_counter} пробелов")


def seek_in_dict(dict):
    user_key = input("Какой ключ вы ищете? ")
    if dict.get(user_key) is not None:
        print(user_key, "содержит", dict.get(user_key))
    else:
        print("Такого ключа нет! Можете его добавить (и значение)")
        user_value = input("Введите значение: ")
        dict.setdefault(user_key, user_value)
        print(dict)
