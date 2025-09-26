"""
Program som registrerer nye brukere og produserer e-postadresser for dem.
"""

# # 1.
# def lag_brukernavn(navn):
#     navn_liste = navn.split()
#     brukernavn = navn_liste[0].lower()  # Blir "kari" ved "Kari Nordmann"
#     for bokstav in navn_liste[1].lower():
#         brukernavn = brukernavn + bokstav   # Legger til første bokstav i siste navnet "karin"
#         break
#     return brukernavn
# assert lag_brukernavn("Kari Nordmann") == "karin"

bruker_ordbok = {"olan": "ifi.uio.no", "karin": "student.matnat.uio.no"}

# 6. Oppdatert funksjon for unike brukernavn
def lag_unikt_brukernavn(navn, eksisterende_ordbok):
    navn_liste = navn.split()
    fornavn = navn_liste[0].lower()
    etternavn = navn_liste[-1].lower()
    for i in range(1, len(etternavn) + 1):  # Itererer gjennom hvert bokstav i etternavnet
        brukernavn = fornavn + etternavn[:i]    # Lager en brukernavn fra første bokstav i etternavn
        if brukernavn not in eksisterende_ordbok:   # Hvis brukernavn allerede eksisterer så fortsetter den for løkken
            return brukernavn
        
assert lag_unikt_brukernavn("Ola Nordmann", bruker_ordbok) == "olano"

# 2.
def lag_epost(brukernavn, suffix):
    return brukernavn + "@" + suffix    # Returnerer en ferdig epost

assert lag_epost("karin", "student.matnat.uio.no") == "karin@student.matnat.uio.no"

# 3.
def skriv_ut_eposter(ordbok):
    for brukernavn, suffix in ordbok.items():
        print(lag_epost(brukernavn, suffix))

skriv_ut_eposter(bruker_ordbok)


# 4.
def main():
    print("Velkommen til e-postfunksjoner.")
    brukere = {}
    fortsette = True
    while fortsette:
        print("Tast:\n\
        1 - For å tilføye et nytt navn og e-post suffix i en ordbok og lage en e-post\n\
        2 - For å skrive ut alle e-postadresser i nåværende bruker ordbok\n\
        x - For å avslutte programmet.")
        bruker_input = input("> ")

        if bruker_input == "1":
            navn = input("Hva heter du? (Fornavn og etternavn)\n> ")
            suffix = input("Hva er din e-post suffix?\n> ")
            brukernavn = lag_unikt_brukernavn(navn)
            brukere[brukernavn] = suffix    # Lagrer brukernavn og suffix i ordbok

            print(f"\nBrukernavn - {brukernavn} med suffix - {suffix} er lagt til i ordboken.\n")
            
        elif bruker_input == "2":
            print("Her er alle e-postadressene lagd:")
            skriv_ut_eposter(brukere)

        elif bruker_input != "x":
            print("\nUkjent kommando.\n")
        else:
            print("Programmet er avsluttet.")
            fortsette = False

main()



