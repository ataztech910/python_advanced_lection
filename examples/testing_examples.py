# -*- encoding: utf-8 -*-

def simple_func(value):
    assert type(value) == int
    assert value > 0

    return value*value

print(simple_func(2))
print(simple_func('2'))