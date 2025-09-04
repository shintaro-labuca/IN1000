"""
Programmet går gjennom ordbok, indeksering og aksessering
"""

def main():
    #1.
    samling = {"melk": "kr 14.90",      #Velger ordbok fordi det gir mening å ha nøkkel og tilhørende verdi
                "brød": "kr 24.90",
                  "yoghurt": "kr 12.90",
                    "pizza": "kr 39.90"}
    print(samling)

    #2.
    def legg_inn_vare():        #Prosedyre for å legge inn varer til samlingen
        vare = input("Skriv inn en vare for å legge det til i samlingen.\n> ")
        pris = input("Hva er prisen på varen?\n> ")
        samling[vare] = pris
        print(f"Du har lagt til {vare} for {pris}")
    legg_inn_vare()
    legg_inn_vare()
    print(samling)

    #3.
    kjøp = input("Hvilken butikkvare vil du kjøpe?\n> ")
    if kjøp in samling:
        print(f"Det koster {samling[kjøp]}")
    else:
        print("Det finnes ikke i samlingen")

main()