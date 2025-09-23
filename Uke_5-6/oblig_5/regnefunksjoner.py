def addisjon(tall1, tall2):
    return tall1 + tall2

def subtraksjon(tall1, tall2):
    return tall1 - tall2

def divisjon(tall1, tall2):
    return tall1 / tall2

assert addisjon(6, 7) == 13
assert subtraksjon(6, 7) == -1
assert divisjon(10, 5) == 2

def tommer_til_cm(tall):
    if tall > 0:
        return tall * 2.54
    else:
        return "Ugyldig input"
    
def gyldig_tall(prompt):
    while True:
        bruker_input = input(prompt)
        try:
            return float(bruker_input)
        except ValueError:
            print("Det må være et tall, prøv igjen!")

def skriv_beregninger():
    brukertall1 = gyldig_tall("Skriv et tall\n> ")
    brukertall2 = gyldig_tall("Skriv et til tall\n> ")

    print(f"Resultater -\nSummering: {addisjon(brukertall1, brukertall2)}\n"
            f"Subtraksjon: {subtraksjon(brukertall1, brukertall2)}\n"
            f"Divisjon: {divisjon(brukertall1, brukertall2)}\n")
            
    bruker_tommer = float(input("Konvertering av tommer til cm - skriv et tall\n> "))
    print(f"Resultat: {tommer_til_cm(bruker_tommer)}")

# MENY FUNKSJON UNFINISHED
