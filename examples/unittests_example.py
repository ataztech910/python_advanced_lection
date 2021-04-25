 # -*- encoding: utf-8 -*-

import unittest


# setUp – подготовка прогона теста; вызывается перед каждым тестом.
# tearDown – вызывается после того, как тест был запущен и результат записан. 
# Метод запускается даже в случае исключения (exception) в теле теста.
# setUpClass – метод вызывается перед запуском всех тестов класса.
# tearDownClass – вызывается после прогона всех тестов класса.
# setUpModule – вызывается перед запуском всех классов модуля.
# tearDownModule – вызывается после прогона всех тестов модуля.

class TestExampleClass(unittest.TestCase):
    # вызывается ПЕРЕД каждым тестом
    def setUp(self):
        print ('Before test')
        pass

    # вызывается ПОСЛЕ каждого теста    
    def tearDown(self):
        print ('After test')
        pass

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')


if __name__ == '__main__':
    unittest.main()