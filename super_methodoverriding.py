class A:
    classvar1 ="I am a class variable in class A"

    def __init__(self):
        self.var1 = "I am in inside A's constructor"
        self.classvar1 ="Instance var in class A"
        self.special ="Special"

class B(A):
    classvar1 = "I am a class variable in class B"

    def __init__(self):


        self.var1 = "I am in inside B's constructor"
        self.classvar1 ="Instance var in class B"
        super().__init__()
a= A()
b=B()

print(b.var1)
print(b.classvar1)
print(b.special)