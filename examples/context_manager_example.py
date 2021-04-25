# -*- coding: utf-8 -*-

from contextlib import contextmanager

@contextmanager
def processor():
    print('--> start processing')
    yield # это генератор и об этом наша следующая тема
    print('<-- stop processing')
with processor():
    print(':: processing')

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    yield f
    f.close()
with open_file('context_namager_example.txt', 'w') as fw:
    fw.write('Привет')