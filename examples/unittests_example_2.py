# -*- encoding: utf-8 -*-

import unittest


class TestUM(unittest.TestCase):

    def testAssertTrue(self):
        """
        Вызывает ошибку если значение аргумента != True
        :return:
        """
        self.assertTrue(True)

    def testFailUnless(self):
        """
        Устаревшее название для assertTrue()
        Вызывает ошибку если значение аргумента != True
        :return:
        """
        self.failUnless(True)

    def testFailIf(self):
        """
        Устаревшая функция, теперь называется assertFalse()
        :return:
        """
        self.failIf(False)

    def testAssertFalse(self):
        """
        Если значение аргумент != False, то кидает ошибку
        :return:
        """
        self.assertFalse(False)

    def testEqual(self):
        """
        Проверка равенства двух аргументов
        :return:
        """
        self.failUnlessEqual(1, 3 - 2)

    def testNotEqual(self):
        """
        Проверка НЕ равенства двух аргументов
        :return:
        """
        self.failIfEqual(2, 3 - 2)

    def testEqualFail(self):
        """
        Ругается если значение аргументов равно
        :return:
        """
        self.failIfEqual(1, 2)

    def testNotEqualFail(self):
        """
        Ругается если значение аргументов не равно
        :return:
        """
        self.failUnlessEqual(2, 3 - 1)

    def testNotAlmostEqual(self):
        """
        Старое название функции.
        Теперь называется assertNotAlmostEqual()
        Сравнивает два аргумента с округлением, можно задать это округление
        Ругается если значения равны
        :return:
        """
        self.failIfAlmostEqual(1.1, 3.3 - 2.0, places=1)

    def testAlmostEqual(self):
        """
        Старое название функции
        Теперь называется assertAlmostEqual()
        Сравнивает два аргумента с округлением, можно задать это округление
        Ругается если значения не равны
        :return:
        """
        self.failUnlessAlmostEqual(1.1, 3.3 - 2.0, places=0)


if __name__ == '__main__':
    unittest.main()