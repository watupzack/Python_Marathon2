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


sort_and_change_list([2, 55, 130, -20, -55, 200, 10])
