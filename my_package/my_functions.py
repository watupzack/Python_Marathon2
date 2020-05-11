print("Here are my functions")


def greet(name):
    print("Привет, " + name + ", каков ваш возраст?")
    user_age = ""
    while user_age == "":
        try:
            user_age = int(input())
            if int(user_age) < 0:
                raise ValueError("No!")
        except ValueError:
            user_age = ""
            print("А я думал вы человек (0_0)")
            print("Так, каков же ваш возраст?")


# Бред какой то, но да
def sort_and_change_list(list1):
    # removes first element, adds one at the end
    list1.sort()
    list1.pop(0)
    list1.append("million")
    print("Обновленный список -", list1)


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