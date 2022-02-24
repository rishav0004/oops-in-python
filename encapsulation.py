class A:
    _p = 'protected'
    __a = 'private'

obj = A
print(obj._p)
print(obj.__a)