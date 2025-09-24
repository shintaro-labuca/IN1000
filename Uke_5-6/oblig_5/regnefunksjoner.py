# 1.
def addisjon(tall1, tall2):
    return tall1 + tall2

def subtraksjon(tall1, tall2):
    return tall1 - tall2

def divisjon(tall1, tall2):
    return tall1 / tall2

assert addisjon(6, 7) == 13
assert subtraksjon(6, 7) == -1
assert divisjon(10, 5) == 2

def tommer_til_cm(tall):    # 2.
    if tall > 0:
        return tall * 2.54
    else:
        return "Ugyldig input"
    
def gyldig_tall(prompt):    # Funksjonen gjør at inputs annet enn tall blir fanget
    while True:
        try:
            return float((input(prompt))) # Returner float
        except ValueError: # Fanger alt som ikke kan gjøres til float (kan ha problemer ved inf/nan)
            print("Det må være et tall, prøv igjen!")

def skriv_beregninger():    # Oppgave 3
    brukertall1 = gyldig_tall("Skriv et tall\n> ")
    brukertall2 = gyldig_tall("Skriv et til tall\n> ")

    print(f"Resultater -\nSummering: {addisjon(brukertall1, brukertall2)}\n"
            f"Subtraksjon: {subtraksjon(brukertall1, brukertall2)}\n"
            f"Divisjon: {divisjon(brukertall1, brukertall2)}\n")
            
    bruker_tommer = gyldig_tall("Konvertering av tommer til cm - skriv et tall\n> ")
    print(f"Resultat: {tommer_til_cm(bruker_tommer)}")

# Oppgave 4.
def meny():
    print("Velkommen til regnefunksjoner! \n\
    Tast:\n\
        1 - For å summere,\n\
        2 - For å subtrahere,\n\
        3 - For å dividere,\n\
        4 - For konvertering av tommer til cm,\n\
        x - For å avslutte.")

def kommandoer():
    bruker_input = input("> ")
    if bruker_input == "1":
        brukertall1 = gyldig_tall("Skriv et tall\n> ")
        brukertall2 = gyldig_tall("Skriv et til tall\n> ")
        print(f"Resultater av summering: {addisjon(brukertall1, brukertall2)}")

    elif bruker_input == "2":
        brukertall1 = gyldig_tall("Skriv et tall\n> ")
        brukertall2 = gyldig_tall("Skriv et til tall\n> ")
        print(f"Resultater av subtraksjon: {subtraksjon(brukertall1, brukertall2)}")

    elif bruker_input == "3":
        brukertall1 = gyldig_tall("Skriv et tall\n> ")
        brukertall2 = gyldig_tall("Skriv et til tall\n> ")
        print(f"Resultater av divisjon: {divisjon(brukertall1, brukertall2)}")

    elif bruker_input == "4":
        brukertall = gyldig_tall("Skriv et tall\n> ")
        print(f"Resultater av konvertering: {tommer_til_cm(brukertall)}")

    elif bruker_input != "x":
        print("Ukjent kommando, prøver igjen\n")
        meny()
        kommandoer()
    else:
        print("Ha en fin dag videre!")

meny()
kommandoer()

