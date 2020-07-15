class Employee:
    no_of_leaves = 8
    pass

nadeem = Employee()
irfan = Employee()

nadeem.name='Nadeem'
nadeem.salary =1234
nadeem.role ='Student'
irfan.name='Nadeem'
irfan.salary = 12345
irfan.role ='INstructor'
print(nadeem.no_of_leaves)
print("Instance and class variables")

# nadeem.no_of_leaves =10
print(nadeem.no_of_leaves)
Employee.no_of_leaves=23
print(Employee.no_of_leaves)
print(nadeem.no_of_leaves)
