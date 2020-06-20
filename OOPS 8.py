# Multi Level Inheritance In Python(Overriding:- check left side of margin for blue concetric circles and an arrow)

class Father:
    musician = "Yes"
    genre = "Rock n Roll"

class Son(Father): # This class inherits all the attributes of class Father
    instrument = "Guitar"
    genre = "Emo Rock"
    def music(self):
        return "Son is a musician"

class Grandson(Son): # This class inherits all the attributes of Classes Father & Son
    instrument = "Guitar + Violin"
    def music(self):
        return "Grandson is a musician"

# Above is an Example of Multi Level Inheritance
SPD = Father()
VPD = Son()
TD = Grandson()
# Conclusions:-
print(TD.musician)
print(TD.genre)
print(TD.instrument)
print(TD.music())
print(VPD.musician)
print(VPD.genre)
print(VPD.instrument)
print(VPD.music())
print(SPD.musician)
print(SPD.genre)

#Quiz Of The Day(by codewithharry):-

class Electronics():
    elec_itm = "Yes"
    ex = "T.V."
    def check(self):
        return f"{self.ex} is an electronic item"

class Pocket_Electronics(Electronics):
    pok_elec_itm = "Yes"
    ex = "MP3 Player"
    def check(self):
        return f"{self.ex} is a pocket electronic item"

class Mobile(Pocket_Electronics):
    mobile = "Yes"
    ex = "Yu Yureka Plus"

    def check(self):
        return f"{self.ex} is a Mobile Phone"

elec = Electronics()
poel = Pocket_Electronics()
mob = Mobile()

# Conclusions:-

print(elec.elec_itm)
print(elec.ex)
print(elec.check())

print(poel.elec_itm)
print(poel.pok_elec_itm)
print(poel.ex)
print(poel.check())

print(mob.elec_itm)
print(mob.pok_elec_itm)
print(mob.mobile)
print(mob.ex)
print(mob.check())