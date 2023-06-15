def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def exponentiate(x, y):
    return x ** y


def remainder(x, y):
    return x % y


print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Нахождение остатка от деления")

choice = input("Введите номер операции (1/2/3/4/5/6): ")
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == '5':
    print(num1, "в степени", num2, "=", exponentiate(num1, num2))
elif choice == '6':
    print("Остаток от деления", num1, "на", num2, "=", remainder(num1, num2))
else:
    print("Неверный ввод операции")
