class employee:
    no_of_leaves = 10
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role= arole

class player:
    no_of_games = 4


    def __init__(self,aname,askilss):
        self.name = aname
        self.skill = askilss

    def printnoofgames(self):
        return f"{self.name} can play this much of games {self.no_of_games}"


    def printskills(self):
        print(f"{self.name}  can play these game {self.skill}")

class coolprogrammer(employee,player):
    game = ["Cricket"]

    def printdetails(self):
        return f"{self.name} is having salary {self.salary} and role is {self.role} and also playes {self.game}"

shahrukh = employee("Shahrukh",10000,"Developer")
asif  = player("Nadeem",["Football","PubG","Cricket"])
nadeem = coolprogrammer("Shahrukh",10000,"Developer")

# print(shahrukh.name)

# print(nadeem.printdetails())


# asif.printskills()

print(nadeem.printnoofgames())