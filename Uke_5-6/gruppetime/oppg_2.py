# Sum mellom to verdier i en ordbok

def summer_rabbatt(vareliste, førpris, nypris):
    sum = 0
    
    for vare in vareliste:
        sum += førpris[vare] - nypris[vare]
    
    return sum

vareliste = ["laptop", "ryggsekk"]
førpris = {"laptop": 5000, "ryggsekk": 900}
nypris = {"laptop": 4000, "ryggsekk": 600}

print(summer_rabbatt(vareliste, førpris, nypris))