class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole



    def printdetails(self):
        return f"My Name is {self.name}. my salary is {self.salary} and my role is {self.role}"


nadeem = Employee("Nadeem",1234,"Student")
irfan = Employee("Irfan",12345,"Instructor")

# nadeem.name='Nadeem'
# nadeem.salary =1234
# nadeem.role ='Student'
# irfan.name='Nadeem'
# irfan.salary = 12345
# irfan.role ='INstructor'

print(nadeem.printdetails())