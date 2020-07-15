class A:
    _prot = 123
    __private = 10

class b(A):
    b= 10

shahrukh = A()


nadeem = b()

print(A._prot)

print(shahrukh._A__private)
