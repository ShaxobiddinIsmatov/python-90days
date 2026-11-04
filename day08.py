# Лекция 3. Exceptions

# Ниже используем try-except для обработки исключений.
# Так же используем функцию main() для ввода числа пользователем
def main():
    x = int(input("Введите число: "))
    return x

try:
    x = main()

except ValueError:
    print("Вы ввели текст, а не число!")

else:
    print(x, "- это число, с которым мы работаем!")