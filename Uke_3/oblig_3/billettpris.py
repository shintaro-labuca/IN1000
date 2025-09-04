"""
Billetter, prosedyrer, if/else setning
"""

def main():

    #1.
    def billett(alder):     #Prosedyre med alder som parameter
        barn = 0 < alder < 18
        voksen = 18 <= alder < 67
        senior = 67 <= alder < 100

        if barn:
            print("Du kan kjøpe barnebillett til 20 kr.")
        elif voksen:
            print("Du kan kjøpe voksenbillett til 45 kr")
        elif senior:
            print("Du kan seniorbillett til 20 kr")
            
    #2. 
    for i in range(3):      #Kaller prosedyren tre ganger for å teste ulike aldre
        alder = int(input("Hvor gammel er du?\n> "))
        billett(alder)

main()