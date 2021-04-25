# -*- coding: utf-8 -*-
 
class DecoratorTest(object):
    """
    Тестируем обычный метод против @classmethod против @staticmethod
    """
    def __init__(self):
        """Конструктор"""
        pass
    
    def doubler(self, x):
        print("умножаем на 2")
        return x*2
 
    @classmethod
    def class_tripler(class_, x):
        print("умножаем на 3: %s" % class_)
        return x*3
    
    @staticmethod
    def static_quad(x):
        print("умножаем на 4")
        return x*4
 
 
if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(DecoratorTest.static_quad(2))
    print(decor.static_quad(3))
 
    print(decor.doubler)
    print(decor.class_tripler)
    print(decor.static_quad)