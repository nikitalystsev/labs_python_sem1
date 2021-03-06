# Лысцев Н. Д. ИУ7-13Б
#
# Решение квадратного уравнения
#
# Ввод
# а - коэффициент перед x**2
# b - коэффициент перед x
# c - свободный член квадратного уравнения
#
# Вывод
# Если уравнение имеет 2 корня х1 и х2, то вывод этих корней
# Если уравнение имеет 1 корень х, то вывод этого корня
# Если уравнение не имеет корней, то вывод сообщения о том, что решений нет

# Ввод коэффициентов квадратного уравнения
a = float(input('Введите коэффициент перед x**2: '))
b = float(input('Введите коэффициент перед x: '))
c = float(input('Введите свободный член квадратного уравнения: '))

# В зависимости от введенных значений переменных вывод соответствующей информации
if a == 0:
    if b == 0:
        if c == 0:
            print('x - любое число')
        else:
            print('x - любое число')
    else:
        if c == 0:
            print('x = 0')
        else:
            x = (-c / b)
            print('x = {:.7g}'.format(x))
else:
    if b == 0:
        if c == 0:
            print('x = 0')
        else:
            x = (-c / a) ** 0.5
            print('x = {:.7g}'.format(x))
    else:
        if c == 0:
            print('x1 = 0')
            x2 = (-b / a)
            print('x2 = {:.7g}'.format(x2))
        else:
            D = b * b - 4 * a * c
            if D > 0:
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                print('x1 = {:.7g}'.format(x1))
                print('x2 = {:.7g}'.format(x2))
            elif D == 0:
                x = (-b) / (2 * a)
                print('x = {:.7g}'.format(x))
            else:
                print('Нет решений')
