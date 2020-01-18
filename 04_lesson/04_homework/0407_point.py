# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

# def fact(num):
#     if num == 1:
#         yield 1
#     else:
#         yield num * fact(num-1)
#
# n = 8
# print(el for el in fact(n))
#
# for i in range(n+1):
#     if i != 0:
#         print(f'{i}!')

from math import factorial
from itertools import count

def fibo_gen():
    for el in count(1):
       yield factorial(el)

x = 0
for i in fibo_gen():
    print('Factorial {} - {}'.format(x + 1, i))
    if x == 15:
        break
    x += 1