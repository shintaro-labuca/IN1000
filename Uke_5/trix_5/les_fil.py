fil = open("navn.txt", "r")

navneliste = []

for linje in fil:
    navneliste.append(linje.strip())

print(navneliste)