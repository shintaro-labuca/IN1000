"""
Regning med løkker, finne max og min ved løkker
"""
def main():
    print("Dette programmet leser tall fra bruker og regner")

    sjekk = None
    tall_liste = []

    while sjekk != 0:       #Kjører så lenge sjekk ikke er 0
        svar = int(input("Skriv tall, eller skriv 0 for å avslutte\n> "))
        if svar != 0:
            tall_liste.append(svar)    
        sjekk = svar
   
    print(f"Program avsluttet, her er listen med tall:")
    for tall in tall_liste:     #Iterer for hvert tall og printer
        print(tall)
    

    sum = 0
    for tall in tall_liste:
        sum += tall     #Legger til alle tall i listen
    print(f"Summen av alle tall i listen: {sum}")


    
    størst = tall_liste[0]      #Tar utgangspunkt i første tall
    for tall in tall_liste:     #Finner største tall og oppdaterer størst
        if tall > størst:
            størst = tall   
    print(f"Størst tall i listen er: {størst}")

    minst = tall_liste[0]
    for tall in tall_liste:
        if tall < minst:
            minst = tall
    print(f"Minst tall i listen er: {minst}")


main()