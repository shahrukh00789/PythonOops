class A:
    def meth(self):
        print("This is a method from class A")

class B(A):
    def meth(self):
        print("This is a method from class B")

class C(A):
    pass

class D(B,C):
    pass


a= A()
b= B()
c= C()
d= D()


d.meth()