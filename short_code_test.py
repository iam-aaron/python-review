#jjj = {'chuck':1,'fred':2, 'jan':100}
#print("list(jjj)->   ",list(jjj))
#print("jjj.keys()->   ",jjj.keys())
#print("jjj.values()->   ",jjj.values())
#print("jjj.items()->   ",jjj.items())

class PartyAnimal:
    x=0
    name = ""

    def __init__(self,n):
        print('I am constructed!')
        self.name = n

    def party(self):
        self.x = self.x+1
        print("so far", self.x)

    def __del__(self):
        print('I am destructued')

    def getName(self):
        return self.name

class FootballFan(PartyAnimal):
    points = 0

    def touchdown(self):
        self.points = self.points+7
        print("so far", self.points)
        self.party()


an = PartyAnimal("test1")
am = PartyAnimal("test2")
al = FootballFan("test3")

#an.party()
#an.party()
#am.party()
#an.party()
al.party()
al.touchdown()
print(al.points)
print(an.getName())
print(am.getName())
