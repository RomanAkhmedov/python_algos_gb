"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from random import randint, choice
from string import ascii_letters
from time import time


def timing(func):
    start_time = time()
    func()
    end_time = time()
    return round(end_time - start_time, 10)


@timing
def list_init():
    array = []
    for i in range(100000):
        array.append(randint(1, 1001))
    return array


@timing
def dict_init():
    data = {}
    for i in range(100000):
        data[choice(ascii_letters)] = randint(1, 1001)
    return data


first = list_init
second = dict_init

print(f'Время формирования списка: {first} сек.')
print(f'Время формирования словаря: {second} сек.')

'''
Генерация словаря происходит приблизительно в полтора раза дольше генерации списка, поскольку при генерации словаря
происходит процесс хэширования, который занимает некорое время. Однако при действиях со словарями (хэш-таблицами)
наблюдается значительное превосходство в скорости над действиями со списками, поскольку операционная сложность словаря
в большинстве случаев составляет О(1) против О(N) для списков.
'''