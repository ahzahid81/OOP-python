# len() being used for a string or a list
#print(len('Phitron'))
#print(len([10, 15, 20]))

# def add(a, b, c=0):
#     return a+b+c

# print(add(5,6))
# print(add(5,6,7))

class Phitron():
    def JhankarMahbub(self):
        print("Jhankar Mahbub is the founder of phitron")

    def AimOfCourse(self):
        print("Software Engineer")

    def type(self):
        print("Special group name is XPSC")

class ProgrammingHero():
    def JhankarMahbub(self):
        print("Jhankar Mahbub is the founder of Programming Hero")

    def AimOfCourse(self):
        print("Web Devoloper")

    def type(self):
        print("Special group name is SCIC")

phi = Phitron()
ph = ProgrammingHero()

for zahid in (phi, ph):
    zahid.JhankarMahbub()
    zahid.AimOfCourse()
    zahid.type()