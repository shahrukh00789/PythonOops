class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def change_leaves(cls,days):
        Employee.no_of_leaves = days

    @classmethod
    def from_str(cls,string):
        # params = string.split("-")
        # return  cls(params[0],params[1],params[2])
        return cls(*string.split("-"))


    def printdetails(self):
        return f"My Name is {self.name}. my salary is {self.salary} and my role is {self.role}"

    @staticmethod
    def print_good(string):
        print(f"This is static method {string}")


nadeem = Employee("Nadeem",1234,"Student")
irfan = Employee("Irfan",12345,"Instructor")
sam =Employee.from_str("Sam-1234-Student")



nadeem.change_leaves(34)

# print(nadeem.no_of_leaves)

# print(sam.salary)

nadeem.print_good("shahrukh")