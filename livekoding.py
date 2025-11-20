def felles(tall_lister: list[list[int]]):
    ordbok = {}
    resultat = []

    for tall_liste in tall_lister:  # Ordbok av nøstet liste
        for tall in tall_liste:
            if tall in ordbok:
                ordbok[tall] += 1
            else:
                ordbok[tall] = 1
    

    for tall, forekomst in ordbok.items():
        if forekomst > 1:
            resultat.append(tall)
    return resultat

# print(felles([[1,5,1], [3,4], [2,3]]))

def jages(dyreliste: list[str]):
    for dyr in dyreliste:
        if "katt" in dyreliste and "mus" in dyreliste:
            return True
        elif "hund" in dyreliste and "katt" in dyreliste:
            return True
        else:
            return False
        
def utvidet_jages(dyreliste: list[str], jaging: dict): #str:str

    for rovdyr, bytte in jaging.items():
        if rovdyr in dyreliste and bytte in dyreliste:
            return True
    return False


def flertall(dyreliste: list[str]):
    ordbok = {}
    
    
    for dyr in dyreliste:
        if dyr in ordbok:
            ordbok[dyr] += 1
        else:
            ordbok[dyr] = 1
            
    maks = 0
    dyr_navn = []


    
    for dyr in ordbok:
        if ordbok[dyr] > maks:
            maks = ordbok[dyr]
            dyr_navn = [dyr]
        elif ordbok[dyr] == maks:
            dyr_navn.append(dyr)
        
    if len(dyr_navn) > 1:
        return "uavgjort" 
    return dyr_navn[0]
        
# print(flertall(["hund", "katt", "hund", "fugl", "katt", "hund"]))
# print(flertall(["hund", "katt", "hund", "fugl", "katt"]))
        

     

tekst1 = "1"
tekst2 = "2"
tekst3 = "3"
tall = int(tekst1 + tekst2) + int(tekst3)
print(tall)

tall = 10
tall = tall + 2
print(tall*2)


tall = 9
if tall < 10:
    tall = tall + 2
    tall = tall + 1
else:
    tall = tall - 10
print(tall)


