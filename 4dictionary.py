import random

thisdict={}
R = random.randint(1, 20)
thisdict["strength"]=R
R = random.randint(1, 20)
thisdict["dexterity"]=R
R = random.randint(1, 20)
thisdict["constitution"]=R
R = random.randint(1, 20)
thisdict["intelligence"]=R
R = random.randint(1, 20)
thisdict["wisdom"]=R
R = random.randint(1, 20)
thisdict["charisma"]=R
for item in thisdict:
  print(item, ":", thisdict[item])

print(thisdict.get("strength"))
print(thisdict.get("spped"))