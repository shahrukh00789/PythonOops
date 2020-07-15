class Employee:
    def __init__(self,fname,lname):
        self.fname= fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    def explain(self):
        return f"this employee firsname is {self.fname} and last name is {self.lname} and email id {self.email}"

    def printemail(self):
        pass

    @email.setter
    def email(self,string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.fname = names.split(".")[1]



shahrukh = Employee("Shahrukh","khan")
sam = Employee("sam","khan")

print(shahrukh.email)
shahrukh.fname ="asif"

print(shahrukh.email)

shahrukh.email ="this.that@gmail.com"

print(shahrukh.fname)