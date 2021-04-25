# -*- coding: utf-8 -*-
from decimal import Decimal
 
class Fees(object):
    """"""
    def __init__(self):
        """Конструктор"""
        self._fee = None
    
    def get_fee(self):
        """
        Возвращаем текущую комиссию
        """
        return self._fee
 
    def set_fee(self, value):
        """
        Устанавливаем размер комиссии
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

    fee = property(get_fee, set_fee)

f = Fees()
f.set_fee("1")
print(f.get_fee())

f.fee = "2"
print( f.get_fee() )