import atexit
try:
    with open("counterfile") as infile:
        _count = int(infile.read())
except FileNotFoundError:
    _count = 0

def increase_counter(n):
    global _count
    _count = _count + n

@atexit.register
def save_counter():
    with open("counterfile", "w") as outfile:
        outfile.write("%d" % _count)


increase_counter(15)