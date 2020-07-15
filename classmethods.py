class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls,days):
        Employee.no_of_leaves = days

    def printdetails(self):
        return f"My Name is {self.name}. my salary is {self.salary} and my role is {self.role}"


nadeem = Employee("Nadeem",1234,"Student")
irfan = Employee("Irfan",12345,"Instructor")

nadeem.change_leaves(34)

print(nadeem.no_of_leaves)