"""
Matplan, 
"""

oversikt = {"Johan": ["Brød", "Egg", "Pølser"],     #Ordbok med navn som nøkkel og liste av mat som verdi
            "Markus": ["Knekkebrød", "Salat", "Biff"],
            "Karen": ["Yoghurt", "Gulrot", "Fisk"],
            "Ahmed": ["Melk", "Sandwich", "Grateng"],
            "Dan": ["Proteinmelk", "Proteinpannekake", "Proteintaco"]}

print("Her er listen av beboere:")
for key in oversikt.keys():     #Printer navnene i ordboka
    print(key)

beboer = input("Skriv navnet til en beboer for å se en oversikt på deres matplan\n> ")
if beboer in oversikt: #Skriver ut verdien til beboer dersom det finnes i ordboka
    print("Her er deres matplan:")
    print(oversikt[beboer])
    
else:
    print("Beboeren er ikke registrert.")

"""
2.
Brukernavn på alle IN1000 studentene - Her ville jeg brukt en liste,
da man kan lagre alle verdier, aksessere og endre ved vilje

Brukernavn og antall studiepoeng dette semesteret for hver student på
IN1000 - Her bruker man en ordbok, for å kalle en student og deretter antall studiepoeng som verdi

Alle vinnere i Lotto siste år (kun navn) - Her kan man bruke en liste, da man kan bare lagre navnet deres

All mat noen gjester i et selskap er allergisk mot (for å planlegge
menyen) - Her bruker jeg en liste for å samle data om allergier, hvis det er spesfikke
allergier som spesfikke gjester er allergist mot så bruker jeg ordbok.
"""