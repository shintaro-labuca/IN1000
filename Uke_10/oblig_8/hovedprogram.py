from verden import Verden

def hovedprogram():
    rad = int(input("Hvor mange rader skal det være på spillbrettet: "))
    kol = int(input("Hvor mange kolonner skal det være på spillbrettet: "))
    verden = Verden(rad, kol)
    verden.tegn()

    while True:
        svar = input("Press enter for å fortsette. Skriv inn q og trykk enter for å avslutte:\n")
        if svar == "":
            verden.oppdatering()
            verden.tegn()
        elif svar.lower() == "q":
            break
        else:
            print("Ugyldig input")

# starte hovedprogrammet
hovedprogram()
