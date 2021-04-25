# -*- encoding: utf-8 -*-

import unittest

# одно подчеркивание - значит что метод или переменная приватные и 
# используются только внутри класса

# двойное подчеркивание в начале для переменной класса создаст 
# префикс для переменной.
"""
Например:

class Person:
    def __init__(self):
        self.name = 'Sarah'
        self._age = 26
        self.__id = 30
p = Person()
dir(p)
['_Person__id', ..., '_age', 'name']        
"""

# одно подчеркивание после имени - необходжимо в случаях 
# когда нужно избежать пересечение с системными именами питона
"""
Например:

def method(name, class='Classname'):   # ❌
SyntaxError: "invalid syntax"
def method(name, class_='Classname'):  # ✅
pass

"""

# _ - безымянная переменная. Можно использовать в циклах
"""
Например:

for _ in range(10):
    print('Welcome Sarah!!')
    
"""

# __str__ - специальный метод отвечающий за строковое представление объекта
# __eq__ - автоматически создает сравнение при создании экземпляра
# __ne__ - автоматически создает обратное сравнение при создании экземпляра

class Point(object):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def __eq__(self, other):
        return True if ((self.x == other.x) and (self.y == other.y)) else False

    def __ne__(self, other):
        return True if ((self.x != other.x) or (self.y != other.y)) else False


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.A = Point(5, 6)
        self.B = Point(6, 10)
        self.C = Point(5.0, 6.0)
        self.D = Point(-5, -6)

    def test_init(self):
        self.assertEqual((self.A.x, self.A.y), (float(5), float(6)), "Полученные значения не являются вещественными!!!")
        self.assertEqual((self.B.x, self.B.y), (float(6), float(10)),
                         "Полученные значения не являются вещественными!!!")
        self.assertEqual((self.C.x, self.C.y), (float(5), float(6)), "Полученные значения не являются вещественными!!!")
        self.assertEqual((self.D.x, self.D.y), (float(-5), float(-6)),
                         "Полученные значения не являются вещественными!!!")

    def test_str(self):
        self.assertTrue(str(self.A) == "(5.0, 6.0)", "Неправильный вывод на экран!!!")
        self.assertTrue(str(self.B) == "(6.0, 10.0)", "Неправильный вывод на экран!!!")
        self.assertTrue(str(self.C) == "(5.0, 6.0)", "Неправильный вывод на экран!!!")
        self.assertTrue(str(self.D) == "(-5.0, -6.0)", "Неправильный вывод на экран!!!")

    def test_eq(self):
        self.assertTrue(self.A == self.C,
                        "Данные две точки равны, а в результате тестирования, они оказались неравными!!!")
        self.assertFalse(self.A == self.B,
                         "Данные две точки неравны, а в результате тестирования, они оказались равными!!!")
        self.assertFalse(self.A == self.D,
                         "Данные две точки неравны, а в результате тестирования, они оказались равными!!!")

    def test_ne(self):
        self.assertFalse(self.A != self.C,
                         "Данные две точки равны, а в результате тестирования, они оказались неравными!!!")
        self.assertTrue(self.A != self.B,
                        "Данные две точки неравны, а в результате тестирования, они оказались равными!!!")
        self.assertTrue(self.A != self.D,
                        "Данные две точки неравны, а в результате тестирования, они оказались равными!!!")


if __name__ == '__main__':
    unittest.main()