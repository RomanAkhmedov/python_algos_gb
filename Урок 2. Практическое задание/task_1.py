"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calc():
    def summation(frst_num, scnd_num):
        return frst_num + scnd_num

    def subtraction(frst_num, scnd_num):
        return frst_num - scnd_num

    def increase(frst_num, scnd_num):
        return frst_num * scnd_num

    def division(frst_num, scnd_num):
        if scnd_num == 0:
            return f'деление на ноль невозможно'
        else:
            return frst_num / scnd_num

    operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')

    if operation == '0':
        return print('выход')
    else:
        frst_num = input('Введите первое число: ')
        scnd_num = input('Введите второе число: ')

        if frst_num.isdigit() is not True or scnd_num.isdigit() is not True:
            print('ввод должен содержать числовые значения')
            return calc()

        frst_num, scnd_num = int(frst_num), int(scnd_num)

        if operation == '+':
            print(summation(frst_num, scnd_num))
        elif operation == '-':
            print(subtraction(frst_num, scnd_num))
        elif operation == '*':
            print(increase(frst_num, scnd_num))
        elif operation == '/':
            print(division(frst_num, scnd_num))
        else:
            print('неверный ввод символа операции')

        return calc()


calc()
