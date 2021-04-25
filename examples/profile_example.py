import hashlib
import cProfile

cProfile.run("hashlib.md5(b'abcdefghijkl').digest()")
