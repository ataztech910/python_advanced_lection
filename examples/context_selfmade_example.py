class Resource:
    def __init__(self, name):
        print('Resource: create {}'.format(name))
        self.__name = name
    def get_name(self):
        return self.__name
    def post_work(self):
        print('Resource: close')

class ResourceForWith:
    def __init__(self, name):
        self.__resource = Resource(name)
    def __enter__(self):
        return self.__resource
    def __exit__(self, type, value, traceback):
        self.__resource.post_work()

with ResourceForWith('Worker') as r:
    print(r.get_name())