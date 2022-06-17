import random

thisdict={"strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"}
number=[]
for x in range(6):
        R = random.randint(1, 20)
        for R in thisdict.values():
            print(R)
thisdict2=number.copy()
print(thisdict2)
all={
    thisdict,thisdict2
}
for a, b in all:
    print(a, ":", b)