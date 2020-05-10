print("User")

number_one = ""
number_two = ""

while number_one == "" or number_two == "":
    try:
        number_one = int(input("Введите первое неотрицательное число: "))
        if number_one < 0:
            raise ValueError("ValueError exception thrown")

        number_two = int(input("Введите второе неотрицательное число: "))
        if number_two < 0:
            raise ValueError("ValueError exception thrown")

        # Addition and subtraction
        print(f"Результат сложения = {number_one+number_two}")
        print(f"Результат вычитания = {number_one-number_two}")

        # Multiplication and division
        print(f"Результат умножения = {number_one*number_two}")
        try:
            print(f"Результат деления = {number_one/number_two}")
        except ZeroDivisionError:
            print("Результата деления не будет, так как к сожалению на 0 делить нельзя")

    except ValueError:
        number_one = ""
        number_two = ""
        print("Ничего кроме неотрицательных чисел!")
        print("Заново!")
