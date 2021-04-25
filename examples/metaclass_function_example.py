def upper_attr(future_class_name, future_class_parents, future_class_attr):
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr 
class Foo(): 
    bar = 'bip'
    pass


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)

# python metaclass_function_example.py => часть старого языка