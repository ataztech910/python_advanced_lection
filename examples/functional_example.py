#!/usr/bin/python3
# -*- coding: utf-8 -*-

from past.builtins import xrange

# Списковые включения или генератор списка
print ([x * 2 if x % 2 == 0 else x + 1 for x in xrange(5, 10)])

list1 = [7, 2, 3, 10, 12]
list2 = [-1, 1, -5, 4, 6]
print(list(map(lambda x, y: x*y, list1, list2)))
print ([x*y for x, y in zip(list1, list2)])

numbers = [10, 4, 2, -1, 6]
print(list(filter(lambda x: x < 5, numbers)))
print([x for x in numbers if x < 5])


# apply()
# Функция для применения другой функции к позиционным и именованным аргументам, заданным списком и словарем соответственно 
def f(x, y, z, a=None, b=None):
    print (x, y, z, a, b)

# Python 2
apply(f, [1, 2, 3], {'a': 4, 'b': 5})

# Python 3
f(*[1, 2, 3], **{'a': 4, 'b': 5})