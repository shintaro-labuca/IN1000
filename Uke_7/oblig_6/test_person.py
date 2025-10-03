from person import Person

def main():
    navn = input("Hva heter du?\n> ")
    alder = int(input("Hvor gammel er du?\n> "))

    person = Person(navn, alder)

    
    def kommando():
        bruker_hobby = input("Legg til hobby\n> ")
        person.legg_til_hobby(bruker_hobby)
    kommando()
    
    fortsette = True
    while fortsette:
        legge_til = input("Ønsker du å legge til flere hobbyer? ja/nei\n> ").lower()
        if legge_til == "ja":
            kommando()
        elif legge_til != "nei":
            print("Ugyldig input")
        else:
            print("Her er all informasjonen lagret:")
            person.skriv_ut()
            print("Programmet avsluttes.")
            fortsette = False
main()