# -*- coding: utf-8 -*-
 
class Person(object):
    def __init__(self, first_name, last_name):
        """Конструктор"""
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self):
        """
        Возвращаем полное имя
        """
        return "%s %s" % (self.first_name, self.last_name)

person = Person("Иван", "Иванов")
 
print(person.full_name) 
print(person.first_name)
 
# person.full_name = "Иваныч"

person.first_name = "Денис"
print(person.full_name) 