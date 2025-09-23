# Tre boolske argumenter, returner True dersom kun to av tre argumenter er True

def badminton(per_vil, palle_vil, espen_vil):
    liste_argumenter = [per_vil, palle_vil, espen_vil]
    antall = 0
    for argument in liste_argumenter:
        if argument:
            antall += 1
    if antall == 2:
        return True
    else:
        return False

en = badminton(True, True, False)
to = badminton(False, False, True)
tre = badminton(True, True, True)
fire = badminton(False, False, False)
fem = badminton(True, False, True)

assert en == True
assert to == False
assert tre == False
assert fire == False
assert fem == True

print(en, to, tre, fire, fem)