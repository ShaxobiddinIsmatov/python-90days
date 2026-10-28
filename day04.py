# Функция square() возвращает квадрат числа a. В функции main() запрашивается ввод числа x
# затем вызывается функция square() для вычисления квадрата x и выводится результат.
def main():
    x = int(input("Enter a x: "))
    print(f"x squared is: {square(x)}")

def square(a):
    return a * a

main()