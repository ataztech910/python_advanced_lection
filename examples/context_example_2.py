# -*- coding: utf-8 -*-

f = open('context_example_2.txt', 'w')
try:
    f.write('Привет')
except:
    print('Ошибка!')
finally:
    f.close()