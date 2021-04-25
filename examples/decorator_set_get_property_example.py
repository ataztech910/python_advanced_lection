# -*- coding: utf-8 -*-
from decimal import Decimal
 
class Fees(object):
    """"""
    def __init__(self):
        """Конструктор"""
        self._fee = None
    
    @property
    def fee(self):
        """
        Возвращаем текущую комиссию - геттер
        """
        return self._fee
 
    @fee.setter
    def fee(self, value):
        """
        Устанавливаем размер комиссии - сеттер
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value
 
 
if __name__ == "__main__":
    f = Fees()

f = Fees()
f.fee = "1"

print( f.fee )

f.fee = "2"
print( f.fee )