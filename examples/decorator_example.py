# -*- coding: utf-8 -*-
def another_function(func):
    """
    Функция которая принимает другую функцию.
    """
    
    def other_func():
        val = "Результат от %s это %s" % (func(),
            eval(func())
        )
        return val
    
    return other_func
 
 
@another_function
def a_function():
    """Обычная функция"""
    return "1+1"
 
 
if __name__ == "__main__":
    value = a_function()
    print(value)