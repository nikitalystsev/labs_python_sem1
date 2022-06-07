# Лысцев Н. Д. ИУ7-13Б

# Вычисление суммы бесконечного ряда с точностью эпсилон

# Ввод
# х - значение агрумента
# eps - требуемая точность вычисления
# max_num_of_iter - максимальное количество итераций
# step - шаг печати

# Вывод
# таблица с номером итерации, значением текущего члена и промежуточным значением суммы
# результат - вычисленное значение суммы ряда либо сообщение о том,
# что за указанное число итераций необходимой точности достичь не удалось

# Введение необходимых величин для вычисления суммы и проверка входных данных
x = float(input('Введите значение аргумента x: '))
eps = float(input('Введите требуемую точность вычисления: '))
if eps <= 0:
    print('Неверный ввод! Значение точности не может быть меньше нуля или равно нулю. ')
else:
    max_num_of_iter = int(input('Введите максимальное количество итераций: '))
    if max_num_of_iter <= 0:
        print('Неверный ввод! Максимальное количество итераций не может быть меньше нуля или равен нулю. ')
    else:
        step = int(input('Введите шаг печати: '))
        if step <= 0:
            print('Неверный ввод! Шаг печати  не может быть меньше нуля или равен нулю. ')
        else:
            # Вывод заголовка таблицы
            print(
                '---------------------------------------------------------------------------------')
            print(
                '|        № итерации        |            t             |            s            |')
            print(
                '|--------------------------------------------------------------------------------')

            # Переменные, необходимые для вычисления суммы
            num_of_iter = 0
            n = 1
            
            t = float("inf")
            b = 0
            s = 0
            new_x = x
            # Вычисление суммы бесконечного ряда с точностью eps
            while abs(t) > eps:
                num_of_iter += 1
                t = 2 * (x / n)
                if abs(t) > eps and num_of_iter > max_num_of_iter:
                    print('за указанное количество итераций вычислить сумму не удалось')
                    break
                elif abs(t) < eps:
                    print(
                        'Сумма бесконечного ряда - {:.7g}, вычислена за {} итераций'.format(s, num_of_iter - 1))
                    break
                s += t
                n += 2
                
                # Вывод значений с определенным шагом
                if num_of_iter - b * step == 1:
                    b += 1
                    print('| {:<10.4g}               |         {:^10.4g}       |         {:^10.4g}      |'.format(
                        num_of_iter, t, s))
                x = x * (new_x ** 2)       
