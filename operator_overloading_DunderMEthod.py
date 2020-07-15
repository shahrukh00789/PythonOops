class Employee:
    def __init__(self,aname,asalary):
        self.name = aname
        self.salary = asalary

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary


emp1 = Employee("Shahrukh khan",10000)
emp2 = Employee("Nadeem",20000)

print(emp1.salary,emp1.name)

print(emp1+emp2)
print(emp1/emp2)
