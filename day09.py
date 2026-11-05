# Лекция 3. Exceptions. Pass, return

# Ниже код для вычисления квадрата числа с функцией
# где используется операторы pass и return.
def code():
    y = getInt()
    print(y ** 2)


def getInt():
    while True:
        try:
            return int(input("Введите число: "))
        except ValueError:
            print("Вы ввели текст, а не число!")

code()