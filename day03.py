# Метод 1. Инт и обычное сложение
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

print(x + y)

# Метод 1.1. Инт и разделение по 3 цифрам
x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

z = x + y
print(f"{z:,}")

# Метод 2. Флоат и обычное сложение
x = float(input("Enter a number: "))    
y = float(input("Enter another number: "))
print(x + y)

# Метод 3. Флоат и округление
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

z = round(x + y)
print(z)

# Метод 4. Флоат и округление до 2 знаков после запятой
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

z = round(x + y, 2)
print(z)

# Метод 5. Флоат и округление до 2 знаков после запятой
# с использованием форматирования
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

z = x + y
print(f"{z:.2f}")